"""Semantic validator for the core/reference economy contract."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"

VALID_RELATIONSHIPS = {"required", "proportional", "preferred", "alternative", "optional", "supply"}
VALID_EFFECTS = {"productivity", "capacity", "reliability", "efficiency"}
VALID_ROLES = {"extraction", "processing", "manufacturing", "supply_production", "service", "logistics"}
VALID_ECONOMIC_LIFECYCLES = {"persistent", "transforming", "emerging", "declining", "phase_out"}
VALID_ENDPOINT_ACTIONS = {"continue", "transform", "decline", "phase_out"}


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def main():
    economy = load("economy.json")
    recipes = load("recipes.json")
    materials = load("materials.json")
    industries = load("industries.json")
    modules = load("modules.json")
    lifecycle = load("industry-lifecycle.json")
    endpoints = load("industry-endpoints.json")
    errors = []

    cargoes = set(economy["cargoes"])
    recipe_ids = set(economy["recipes"])
    industry_ids = set(economy["industries"])
    module_ids = set(economy["modules"])
    sectors = set(economy["sectors"])
    eras = economy["eras"]
    horizon = lifecycle.get("horizon", {})
    horizon_start = horizon.get("start")
    horizon_end = horizon.get("end")

    if economy.get("version") != "0.4.1":
        errors.append(f"expected economy version 0.4.1, found {economy.get('version')}")
    if len(sectors) != len(economy["sectors"]):
        errors.append("duplicate sectors in economy manifest")
    if len(eras) != 4:
        errors.append(f"expected 4 eras, found {len(eras)}")
    expected_bounds = [(1700, 1849), (1850, 1999), (2000, 2149), (2150, 2299)]
    actual_bounds = [(e.get("start"), e.get("end")) for e in eras]
    if actual_bounds != expected_bounds:
        errors.append(f"era bounds mismatch: expected {expected_bounds}, found {actual_bounds}")
    if (horizon_start, horizon_end) != (1700, 2299):
        errors.append(f"lifecycle horizon must be 1700-2299, found {horizon_start}-{horizon_end}")

    material_ids = {x["id"] for x in materials}
    if material_ids - cargoes:
        errors.append(f"materials missing from cargo manifest: {sorted(material_ids - cargoes)}")

    if len(modules) != len(module_ids):
        errors.append("duplicate module ids")
    for module in modules:
        mid = module.get("id")
        if mid not in module_ids:
            errors.append(f"module definition not declared in manifest: {mid}")
        for dep in module.get("depends_on", []):
            if dep not in module_ids:
                errors.append(f"module {mid}: unknown dependency {dep}")

    seen = set()
    produced = set()
    recipe_by_output = {}
    for r in recipes:
        rid = r.get("id")
        if not rid or rid in seen:
            errors.append(f"duplicate/missing recipe: {rid}")
        seen.add(rid)
        if rid not in recipe_ids:
            errors.append(f"recipe not declared in manifest: {rid}")
        out = r.get("output")
        produced.add(out)
        recipe_by_output.setdefault(out, []).append(r)
        if out not in cargoes:
            errors.append(f"recipe {rid}: unknown output cargo {out}")
        if r.get("output_amount", 0) <= 0:
            errors.append(f"recipe {rid}: output_amount must be positive")
        for item in r.get("inputs", []):
            cargo = item.get("cargo")
            rel = item.get("relationship")
            if cargo not in cargoes:
                errors.append(f"recipe {rid}: unknown input cargo {cargo}")
            if item.get("amount", 0) <= 0:
                errors.append(f"recipe {rid}: input amount must be positive")
            if rel not in VALID_RELATIONSHIPS:
                errors.append(f"recipe {rid}: invalid relationship {rel}")
            if rel == "alternative" and not item.get("group"):
                errors.append(f"recipe {rid}: alternative input missing group")

    if recipe_ids - seen:
        errors.append(f"manifest recipes missing definitions: {sorted(recipe_ids - seen)}")
    for material in materials:
        if material["id"] not in produced:
            errors.append(f"material has no producing recipe: {material['id']}")

    seen_industries = set()
    outputs_by_industry = {}
    by_id = {}
    for ind in industries:
        iid = ind.get("id")
        if not iid or iid in seen_industries:
            errors.append(f"duplicate/missing industry: {iid}")
        seen_industries.add(iid)
        by_id[iid] = ind
        if iid not in industry_ids:
            errors.append(f"industry not declared in manifest: {iid}")
        role = ind.get("role")
        if role not in VALID_ROLES:
            errors.append(f"industry {iid}: invalid role {role}")
        if ind.get("sector") not in sectors:
            errors.append(f"industry {iid}: unknown sector {ind.get('sector')}")
        if ind.get("module") not in module_ids:
            errors.append(f"industry {iid}: unknown module {ind.get('module')}")
        era = ind.get("era", {})
        if era.get("start") is None or era.get("end") is None or era["start"] > era["end"]:
            errors.append(f"industry {iid}: invalid era")
        for item in ind.get("hard_inputs", []):
            if item.get("cargo") not in cargoes:
                errors.append(f"industry {iid}: unknown hard input {item.get('cargo')}")
            if item.get("amount", 0) <= 0:
                errors.append(f"industry {iid}: hard input amount must be positive")
            if item.get("relationship") not in VALID_RELATIONSHIPS:
                errors.append(f"industry {iid}: invalid hard-input relationship {item.get('relationship')}")
            if item.get("relationship") == "alternative" and not item.get("group"):
                errors.append(f"industry {iid}: alternative hard input missing group")
        for item in ind.get("operational_supplies", []):
            if item.get("cargo") not in cargoes:
                errors.append(f"industry {iid}: unknown operational supply {item.get('cargo')}")
            if item.get("effect") not in VALID_EFFECTS:
                errors.append(f"industry {iid}: invalid operational supply effect {item.get('effect')}")
        for item in ind.get("outputs", []):
            cargo = item.get("cargo")
            outputs_by_industry.setdefault(cargo, []).append(iid)
            if cargo not in cargoes:
                errors.append(f"industry {iid}: unknown output cargo {cargo}")
            if item.get("amount", 0) <= 0:
                errors.append(f"industry {iid}: output amount must be positive")
        for link in ("predecessor", "successor"):
            if ind.get(link) and ind[link] not in industry_ids:
                errors.append(f"industry {iid}: unknown {link} {ind[link]}")

    if industry_ids - seen_industries:
        errors.append(f"manifest industries missing definitions: {sorted(industry_ids - seen_industries)}")

    # The separate economic lifecycle map must cover exactly the manifest IDs.
    lifecycle_ids = set(lifecycle.get("industries", {}))
    if lifecycle_ids - industry_ids:
        errors.append(f"lifecycle map contains unknown industries: {sorted(lifecycle_ids - industry_ids)}")
    if industry_ids - lifecycle_ids:
        errors.append(f"lifecycle map missing industries: {sorted(industry_ids - lifecycle_ids)}")
    for iid, value in lifecycle.get("industries", {}).items():
        if value not in VALID_ECONOMIC_LIFECYCLES:
            errors.append(f"industry {iid}: invalid economic lifecycle {value}")

    # Every succession chain must terminate in an explicit 2299 endpoint contract.
    terminal_ids = set(endpoints.get("terminal_industries", {}))
    if terminal_ids - industry_ids:
        errors.append(f"endpoint contract contains unknown industries: {sorted(terminal_ids - industry_ids)}")
    if industry_ids and not terminal_ids:
        errors.append("endpoint contract contains no terminal industries")
    for iid, spec in endpoints.get("terminal_industries", {}).items():
        if not isinstance(spec, dict):
            errors.append(f"endpoint {iid}: endpoint spec must be an object")
            continue
        action = spec.get("action")
        coverage_end = spec.get("coverage_end")
        if action not in VALID_ENDPOINT_ACTIONS:
            errors.append(f"endpoint {iid}: invalid action {action}")
        if coverage_end != horizon_end:
            errors.append(f"endpoint {iid}: coverage_end must be {horizon_end}, found {coverage_end}")

    for iid, ind in by_id.items():
        seen_chain = set()
        current = iid
        while by_id.get(current, {}).get("successor"):
            if current in seen_chain:
                errors.append(f"industry {iid}: successor cycle detected at {current}")
                break
            seen_chain.add(current)
            current = by_id[current]["successor"]
        else:
            if current not in terminal_ids:
                errors.append(f"industry {iid}: succession chain terminates at {current}, which lacks a 2299 endpoint contract")

    # The endpoint contract is authoritative campaign-horizon coverage. A legacy
    # industry record may have an earlier era end, but its terminal family must
    # explicitly declare coverage through the campaign horizon.
    for iid, spec in endpoints.get("terminal_industries", {}).items():
        ind = by_id.get(iid)
        if not ind:
            continue
        coverage_end = spec.get("coverage_end")
        record_end = ind.get("era", {}).get("end")
        if record_end is None or record_end > coverage_end:
            errors.append(f"industry {iid}: record era end {record_end} exceeds endpoint coverage {coverage_end}")

    # Every recipe output must have an industry producer. For processed outputs,
    # at least one producer must also accept one of the recipe's actual inputs.
    for rid in recipe_ids:
        recipe = next((r for r in recipes if r.get("id") == rid), None)
        if not recipe:
            continue
        producers = outputs_by_industry.get(recipe.get("output"), [])
        if not producers:
            errors.append(f"recipe {rid}: no industry produces {recipe.get('output')}")
            continue
        recipe_inputs = {x.get("cargo") for x in recipe.get("inputs", [])}
        if recipe_inputs and not any(
            recipe_inputs & {x.get("cargo") for x in next(i for i in industries if i["id"] == pid).get("hard_inputs", [])}
            for pid in producers
        ):
            errors.append(f"recipe {rid}: no producing industry accepts a recipe input")

    # Succession links must be reciprocal where both sides declare the relationship.
    for ind in industries:
        iid = ind["id"]
        succ = ind.get("successor")
        pred = ind.get("predecessor")
        if succ and by_id.get(succ, {}).get("predecessor") not in (None, iid):
            errors.append(f"industry {iid}: successor {succ} does not reciprocate predecessor")
        if pred and by_id.get(pred, {}).get("successor") not in (None, iid):
            errors.append(f"industry {iid}: predecessor {pred} does not reciprocate successor")
        if ind.get("lifecycle") == "successor" and not (succ or pred):
            errors.append(f"industry {iid}: successor lifecycle has no succession link")

    # Guard the explicit carbon-materials decision: Coke is persistent and is not
    # allowed to be replaced by a fictional direct coal -> synthetic-diamond chain.
    if lifecycle.get("industries", {}).get("PRC_COKE") != "persistent":
        errors.append("PRC_COKE must remain economic_lifecycle=persistent")
    forbidden_direct_diamond = {"coal", "coke"}
    for recipe in recipes:
        if recipe.get("output") in {"synthetic_diamond", "diamond"}:
            inputs = {x.get("cargo") for x in recipe.get("inputs", [])}
            if inputs & forbidden_direct_diamond:
                errors.append(f"recipe {recipe.get('id')}: direct coal/coke to diamond is forbidden")

    if len(industry_ids) != len(economy["industries"]):
        errors.append("duplicate industry ids in economy manifest")
    if len(recipe_ids) != len(economy["recipes"]):
        errors.append("duplicate recipe ids in economy manifest")
    if len(module_ids) != len(economy["modules"]):
        errors.append("duplicate module ids in economy manifest")

    if errors:
        print("ECONOMY VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print("ECONOMY VALIDATION PASSED")
    print(f"version: {economy['version']}")
    print(f"cargoes: {len(cargoes)}")
    print(f"materials: {len(materials)}")
    print(f"recipes: {len(recipes)}")
    print(f"industries: {len(industries)}")
    print(f"modules: {len(modules)}")
    print(f"sectors: {len(sectors)}")
    print(f"horizon: {horizon_start}-{horizon_end}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

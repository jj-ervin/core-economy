"""Semantic validator for the core/reference economy contract."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"

EXPECTED_SECTORS = {
    "energy", "materials", "industrials", "consumer_discretionary",
    "consumer_staples", "health_care", "financials",
    "information_technology", "communication_services", "utilities",
    "real_estate",
}

VALID_RELATIONSHIPS = {"required", "proportional", "preferred", "alternative", "optional", "supply"}
VALID_EFFECTS = {"productivity", "capacity", "reliability", "efficiency"}
VALID_ROLES = {"extraction", "processing", "manufacturing", "supply_production", "service", "logistics"}


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def main():
    economy = load("economy.json")
    recipes = load("recipes.json")
    materials = load("materials.json")
    industries = load("industries.json")
    modules = load("modules.json")
    errors = []

    cargoes = set(economy["cargoes"])
    recipe_ids = set(economy["recipes"])
    industry_ids = set(economy["industries"])
    module_ids = set(economy["modules"])
    sectors = economy["sectors"]
    eras = economy["eras"]

    if economy.get("version") != "0.4.0":
        errors.append(f"expected economy version 0.4.0, found {economy.get('version')}")
    if len(sectors) != 11:
        errors.append(f"expected 11 sectors, found {len(sectors)}")
    if len(set(sectors)) != len(sectors):
        errors.append("duplicate sectors in economy manifest")
    if set(sectors) != EXPECTED_SECTORS:
        errors.append(f"sector taxonomy mismatch: expected {sorted(EXPECTED_SECTORS)}, found {sorted(set(sectors))}")

    era_ids = set()
    for era in eras:
        eid = era.get("id")
        if not eid or eid in era_ids:
            errors.append(f"duplicate/missing era id: {eid}")
        era_ids.add(eid)
        if era.get("start") is None or era.get("end") is None or era["start"] > era["end"]:
            errors.append(f"invalid era bounds: {eid}")

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
    for ind in industries:
        iid = ind.get("id")
        if not iid or iid in seen_industries:
            errors.append(f"duplicate/missing industry: {iid}")
        seen_industries.add(iid)
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
    by_id = {i["id"]: i for i in industries}
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

    # Reference economy must declare every manifest object exactly once.
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
    return 0


if __name__ == "__main__":
    sys.exit(main())

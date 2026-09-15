"""Graph-level validator for the canonical Core Economy.

This complements validate_economy.py. It validates economic reachability and
producer/consumer relationships rather than only schema/reference integrity.
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"

# These cargoes are transport flows/endpoints, not industrial products.
FLOW_CARGOES = {"passengers", "personnel", "mail"}

# These cargoes terminate in settlement/market demand rather than another
# industrial processor. They are legitimate graph sinks, so they are not
# expected to appear as hard inputs on another industry.
FINAL_CONSUMER_CARGOES = {"food", "manufactured_goods", "advanced_goods"}

# These are expected to originate at extraction industries rather than recipes.
PRIMARY_CARGOES = {
    "grain", "livestock", "timber", "fish", "coal", "iron_ore", "stone",
    "clay", "oil", "gas", "copper_ore", "sand", "bauxite", "titanium_ore",
    "gold_ore", "silver_ore", "rare_earth_ore",
}


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def main():
    economy = load("economy.json")
    recipes = load("recipes.json")
    industries = load("industries.json")
    endpoints = load("industry-endpoints.json")
    errors = []

    cargoes = set(economy["cargoes"])
    industry_ids = set(economy["industries"])
    recipe_ids = set(economy["recipes"])

    if not FLOW_CARGOES <= cargoes:
        errors.append(f"flow cargoes missing from manifest: {sorted(FLOW_CARGOES - cargoes)}")

    if not FINAL_CONSUMER_CARGOES <= cargoes:
        errors.append(
            f"final consumer cargoes missing from manifest: {sorted(FINAL_CONSUMER_CARGOES - cargoes)}"
        )

    by_id = {i["id"]: i for i in industries}
    recipe_by_id = {r["id"]: r for r in recipes}

    producers = {}
    consumers = {}
    operational_consumers = {}

    for ind in industries:
        iid = ind["id"]
        for item in ind.get("outputs", []):
            cargo = item.get("cargo")
            producers.setdefault(cargo, set()).add(iid)
        for item in ind.get("hard_inputs", []):
            cargo = item.get("cargo")
            consumers.setdefault(cargo, set()).add(iid)
        for item in ind.get("operational_supplies", []):
            cargo = item.get("cargo")
            operational_consumers.setdefault(cargo, set()).add(iid)

    for recipe in recipes:
        output = recipe.get("output")
        for item in recipe.get("inputs", []):
            consumers.setdefault(item.get("cargo"), set()).add(f"recipe:{recipe['id']}")
        producers.setdefault(output, set())

    # Every primary resource must have an extraction producer. This deliberately
    # excludes transport-flow cargoes, which originate at endpoints/transport flows.
    for cargo in sorted(PRIMARY_CARGOES):
        if cargo not in cargoes:
            errors.append(f"primary cargo missing from manifest: {cargo}")
            continue
        extraction_producers = [
            iid for iid in producers.get(cargo, set())
            if by_id.get(iid, {}).get("role") == "extraction"
        ]
        if not extraction_producers:
            errors.append(f"primary cargo has no extraction source: {cargo}")

    # Every non-flow recipe output must be produced by an industry.
    for recipe in recipes:
        output = recipe.get("output")
        if output in FLOW_CARGOES:
            errors.append(f"recipe {recipe['id']}: transport-flow cargo cannot be an industrial recipe output: {output}")
            continue
        if not producers.get(output):
            errors.append(f"recipe {recipe['id']}: no industry produces {output}")

        producer_ids = producers.get(output, set())
        recipe_inputs = {x.get("cargo") for x in recipe.get("inputs", [])}
        if recipe_inputs and producer_ids:
            compatible = False
            for pid in producer_ids:
                ind = by_id.get(pid)
                if not ind:
                    continue
                accepted = {x.get("cargo") for x in ind.get("hard_inputs", [])}
                if recipe_inputs <= accepted:
                    compatible = True
                    break
                groups = {}
                for item in ind.get("hard_inputs", []):
                    if item.get("relationship") == "alternative":
                        groups.setdefault(item.get("group"), set()).add(item.get("cargo"))
                if len(recipe_inputs) == 1 and any(recipe_inputs <= members for members in groups.values()):
                    compatible = True
                    break
            if not compatible:
                errors.append(
                    f"recipe {recipe['id']}: no producer of {output} accepts the recipe's complete input set"
                )

    # Detect non-flow cargoes with no downstream use. Primary/intermediate
    # materials must feed another industrial or operational path; final consumer
    # cargoes terminate in settlement/market demand and are explicit exceptions.
    for cargo in sorted(cargoes - FLOW_CARGOES - FINAL_CONSUMER_CARGOES):
        if cargo not in consumers and cargo not in operational_consumers:
            errors.append(f"cargo has no downstream consumer or operational use: {cargo}")

    # Detect industrial outputs that are only human-flow placeholders.
    for cargo in sorted(FLOW_CARGOES):
        for iid in sorted(producers.get(cargo, set())):
            role = by_id.get(iid, {}).get("role")
            if role not in {"logistics", "service"}:
                errors.append(f"flow cargo {cargo} is produced by non-flow industry {iid}")

    terminal_ids = set(endpoints.get("terminal_industries", {}))
    for iid, ind in by_id.items():
        successor = ind.get("successor")
        if not successor or successor not in by_id:
            continue
        old_outputs = {x.get("cargo") for x in ind.get("outputs", [])}
        new_outputs = {x.get("cargo") for x in by_id[successor].get("outputs", [])}
        if old_outputs and new_outputs and not (old_outputs & new_outputs):
            if successor not in terminal_ids:
                errors.append(
                    f"successor flow discontinuity: {iid} -> {successor} changes all output cargoes without terminal transform"
                )

    if errors:
        print("ECONOMIC GRAPH VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("ECONOMIC GRAPH VALIDATION PASSED")
    print(f"cargoes: {len(cargoes)}")
    print(f"recipes: {len(recipe_ids)}")
    print(f"industries: {len(industry_ids)}")
    print(f"flow cargoes: {sorted(FLOW_CARGOES)}")
    print(f"final consumer cargoes: {sorted(FINAL_CONSUMER_CARGOES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Semantic validator for the reference economy manifest and recipes."""
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"
def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)
def main():
    economy = load("economy.json")
    recipes = load("recipes.json")
    materials = load("materials.json")
    errors = []
    cargoes = set(economy["cargoes"])
    recipe_ids = set(economy["recipes"])
    sectors = economy["sectors"]
    material_ids = {x["id"] for x in materials}
    if len(sectors) != 11:
        errors.append(f"expected 11 sectors, found {len(sectors)}")
    if len(set(sectors)) != len(sectors):
        errors.append("duplicate sectors in economy manifest")
    if material_ids - cargoes:
        errors.append(f"materials missing from cargo manifest: {sorted(material_ids - cargoes)}")
    seen = set()
    produced = set()
    for r in recipes:
        rid = r.get("id")
        if rid in seen:
            errors.append(f"duplicate recipe: {rid}")
        seen.add(rid)
        if rid not in recipe_ids:
            errors.append(f"recipe not declared in manifest: {rid}")
        out = r.get("output")
        produced.add(out)
        if out not in cargoes:
            errors.append(f"recipe {rid}: unknown output cargo {out}")
        if r.get("output_amount", 0) <= 0:
            errors.append(f"recipe {rid}: output_amount must be positive")
        for item in r.get("inputs", []):
            cargo = item.get("cargo")
            if cargo not in cargoes:
                errors.append(f"recipe {rid}: unknown input cargo {cargo}")
            if item.get("amount", 0) <= 0:
                errors.append(f"recipe {rid}: input amount must be positive")
            if item.get("relationship") == "alternative" and not item.get("group"):
                errors.append(f"recipe {rid}: alternative input missing group")
    if recipe_ids - seen:
        errors.append(f"manifest recipes missing definitions: {sorted(recipe_ids - seen)}")
    for material in materials:
        if material["id"] not in produced:
            errors.append(f"material has no producing recipe: {material['id']}")
    if errors:
        print("ECONOMY VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1
    print("ECONOMY VALIDATION PASSED")
    print(f"cargoes: {len(cargoes)}")
    print(f"materials: {len(materials)}")
    print(f"recipes: {len(recipes)}")
    print(f"sectors: {len(sectors)}")
    return 0
if __name__ == "__main__":
    sys.exit(main())

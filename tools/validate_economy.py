"""Semantic validator for the reference economy."""
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
    errors = []

    cargoes = set(economy["cargoes"])
    recipe_ids = set(economy["recipes"])
    sector_ids = set(economy["sectors"])

    if len(sector_ids) != 11:
        errors.append(f"expected 11 sectors, found {len(sector_ids)}")

    if len(recipe_ids) != len(economy["recipes"]):
        errors.append("duplicate recipe IDs in economy manifest")

    seen_recipes = set()
    for recipe in recipes:
        rid = recipe.get("id")
        if rid in seen_recipes:
            errors.append(f"duplicate recipe: {rid}")
        seen_recipes.add(rid)
        if rid not in recipe_ids:
            errors.append(f"recipe not declared in manifest: {rid}")
        out = recipe.get("output")
        if out not in cargoes:
            errors.append(f"recipe {rid}: unknown output cargo {out}")
        for item in recipe.get("inputs", []):
            cargo = item.get("cargo")
            if cargo not in cargoes:
                errors.append(f"recipe {rid}: unknown input cargo {cargo}")
            if item.get("relationship") == "alternative" and not item.get("group"):
                errors.append(f"recipe {rid}: alternative input missing group")
        if recipe.get("output_amount", 0) <= 0:
            errors.append(f"recipe {rid}: output_amount must be positive")

    if errors:
        print("ECONOMY VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("ECONOMY VALIDATION PASSED")
    print(f"cargoes: {len(cargoes)}")
    print(f"recipes: {len(recipes)}")
    print(f"sectors: {len(sector_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Validate the Stage 3C Coal -> Coke -> Steel implementation slice.

The economic contract remains authoritative in data/reference-economy. This
validator only checks that the NML adapter explicitly contains the canonical
cargo and recipe endpoints for the focused playable chain.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"
NML = ROOT / "games" / "openttd" / "newgrf"


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    cargoes = load_json("cargoes.json")
    recipes = load_json("recipes.json")
    industries = load_json("industries.json")

    cargo_by_id = {c["id"]: c for c in cargoes}
    recipe_by_id = {r["id"]: r for r in recipes}
    industry_by_id = {i["id"]: i for i in industries}

    required_cargoes = {"coal", "coke", "iron_ore", "steel"}
    required_recipes = {"coal_to_coke", "iron_ore_coke_to_steel"}
    required_industries = {"MIN_COAL_EARLY", "MIN_IRON", "PRC_COKE", "PRC_STEEL"}

    assert required_cargoes <= cargo_by_id.keys(), "canonical chain cargo missing"
    assert required_recipes <= recipe_by_id.keys(), "canonical chain recipe missing"
    assert required_industries <= industry_by_id.keys(), "canonical chain industry missing"

    cargo_nml = (NML / "cargoes.nml").read_text(encoding="utf-8")
    production_nml = (NML / "production.nml").read_text(encoding="utf-8")
    industries_nml = (NML / "industries.nml").read_text(encoding="utf-8")

    for label in ("COAL", "IORE", "COKE", "STEL"):
        assert label in cargo_nml or label in (NML / "core_economy.nml").read_text(encoding="utf-8"), f"NML cargo label missing: {label}"

    for token in ("coke_works_produce_cb", "steel_mill_produce_cb", '"COAL"', '"COKE"', '"IORE"', '"STEL"'):
        assert token in production_nml, f"production adapter missing: {token}"

    for token in ("ind_coal_mine", "ind_iron_mine", "ind_coke_works", "ind_steel_mill", "current_year >= 1750"):
        assert token in industries_nml, f"industry adapter missing: {token}"

    print("PLAYABLE CHAIN VALIDATION: PASS")
    print("canonical chain: coal -> coke; iron_ore + coke -> steel")
    print("industries: MIN_COAL_EARLY, MIN_IRON, PRC_COKE, PRC_STEEL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

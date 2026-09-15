"""Validate the Stage 3C playable chain and canonical cargo adapter.

The economic contract remains authoritative in data/reference-economy. This
validator checks the NML adapter for the focused playable chain plus the cargo
slot/translation invariants required by OpenTTD's cargo model.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reference-economy"
NML = ROOT / "games" / "openttd" / "newgrf"

BUILTIN_LABELS = {
    "GRAI", "LVST", "WOOD", "COAL", "IORE", "OIL_", "CORE", "STEL",
    "GOLD", "FOOD", "PASS", "MAIL",
}

CANONICAL_LABELS = [
    "GRAI", "LVST", "WOOD", "FISH", "COAL", "IORE", "STON", "CLAY",
    "OIL_", "GAS_", "CORE", "SAND", "BAUX", "TIO_", "GORE", "SORE",
    "REOR", "COKE", "STEL", "COPP", "GLAS", "CERA", "ALUM", "TITN",
    "GOLD", "SILV", "REMT", "LIME", "CEMT", "FOOD", "LUMB", "PETR",
    "MACH", "CHEM", "MNFG", "ELEC", "ADVG", "HARD", "INDE", "CNST",
    "AGRI", "TECH", "FUEL", "PASS", "PERS", "MAIL",
]


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def validate_cargo_adapter(cargo_nml: str, entrypoint_nml: str) -> None:
    """Validate custom slots and the stable canonical translation table."""
    table_match = re.search(r"cargotable\s*\{(.*?)\}", entrypoint_nml, re.DOTALL)
    assert table_match, "canonical cargotable missing from generated entrypoint"
    table_labels = re.findall(r"\b[A-Z][A-Z0-9_]{3}\b", table_match.group(1))
    assert table_labels == CANONICAL_LABELS, "canonical cargotable order/content drifted"

    item_pattern = re.compile(
        r"item\(FEAT_CARGOS,\s*cargo_([a-z0-9_]+),\s*(\d+)\)\s*\{\s*"
        r"property\s*\{(.*?)\}\s*\}",
        re.DOTALL,
    )
    items = item_pattern.findall(cargo_nml)
    assert items, "no custom cargo definitions found"

    ids = []
    labels = []
    for cargo_id, item_id_text, properties in items:
        item_id = int(item_id_text)
        number_match = re.search(r"\bnumber\s*:\s*(\d+)\s*;", properties)
        label_match = re.search(r'\bcargo_label\s*:\s*"([A-Z0-9_]{4})"\s*;', properties)
        assert number_match, f"custom cargo {cargo_id} missing explicit number"
        assert label_match, f"custom cargo {cargo_id} missing cargo_label"
        number = int(number_match.group(1))
        label = label_match.group(1)

        assert item_id >= 12, f"custom cargo {label} illegally occupies original slot {item_id}"
        assert number == item_id, f"custom cargo {label} number {number} != item ID {item_id}"
        assert item_id < 64, f"custom cargo {label} exceeds OpenTTD cargo slot limit"
        assert label not in BUILTIN_LABELS, f"built-in cargo {label} must not be redefined"
        assert label in CANONICAL_LABELS, f"non-canonical cargo label defined: {label}"
        ids.append(item_id)
        labels.append(label)

    assert len(ids) == len(set(ids)), "duplicate custom cargo item IDs"
    assert len(labels) == len(set(labels)), "duplicate custom cargo labels"

    represented = set(BUILTIN_LABELS) | set(labels)
    assert represented == set(CANONICAL_LABELS), (
        "canonical cargo coverage mismatch: "
        f"missing={sorted(set(CANONICAL_LABELS) - represented)} "
        f"extra={sorted(represented - set(CANONICAL_LABELS))}"
    )


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
    entrypoint_nml = (NML / "core_economy.nml").read_text(encoding="utf-8")
    production_nml = (NML / "production.nml").read_text(encoding="utf-8")
    industries_nml = (NML / "industries.nml").read_text(encoding="utf-8")

    validate_cargo_adapter(cargo_nml, entrypoint_nml)

    # Match the actual production expressions, not merely cargo-label presence.
    # These are the canonical 1:1 recipes in recipes.json.
    assert (
        'COAL: incoming_cargo_waiting("COAL");' in production_nml
        and 'COKE: incoming_cargo_waiting("COAL");' in production_nml
    ), "coke production callback does not implement canonical 1:1 coal -> coke"

    assert (
        'IORE: min(incoming_cargo_waiting("IORE"), incoming_cargo_waiting("COKE"));' in production_nml
        and 'COKE: min(incoming_cargo_waiting("IORE"), incoming_cargo_waiting("COKE"));' in production_nml
        and 'STEL: min(incoming_cargo_waiting("IORE"), incoming_cargo_waiting("COKE"));' in production_nml
    ), "steel production callback does not implement canonical 1:1 iron ore + coke -> steel"

    for token in ("ind_coal_mine", "ind_iron_mine", "ind_coke_works", "ind_steel_mill", "current_year >= 1750"):
        assert token in industries_nml, f"industry adapter missing: {token}"

    print("PLAYABLE CHAIN VALIDATION: PASS")
    print("cargo adapter: canonical translation table + safe custom slots")
    print("canonical chain: coal -> coke; iron_ore + coke -> steel")
    print("industries: MIN_COAL_EARLY, MIN_IRON, PRC_COKE, PRC_STEEL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# OpenTTD NewGRF Adapter — Core Economy Cargo/Industry Mapping

## Overview

This adapter implements the OpenTTD representation of the Core Economy model.
The Stage 2 JSON contracts remain authoritative for cargoes, recipes, industries,
and historical dates.

The first playable slice is:
- **Coal Mine** (`MIN_COAL_EARLY`) → `coal`
- **Iron Mine** (`MIN_IRON`) → `iron_ore`
- **Coke Works** (`PRC_COKE`): `coal` → `coke`
- **Steel Mill** (`PRC_STEEL`): `iron_ore` + `coke` → `steel`

## Cargo Mapping

The canonical translation table preserves the Core Economy label order. Its
order is independent of the local item IDs used for custom cargo definitions.

### Reused OpenTTD built-in cargoes

The adapter reuses existing OpenTTD cargo labels where the built-in semantic
cargo is the same canonical cargo:

| Core Economy ID | OpenTTD Label |
| :--- | :--- |
| `grain` | `GRAI` |
| `livestock` | `LVST` |
| `timber` | `WOOD` |
| `coal` | `COAL` |
| `iron_ore` | `IORE` |
| `oil` | `OIL_` |
| `copper_ore` | `CORE` |
| `steel` | `STEL` |
| `gold` | `GOLD` |
| `food` | `FOOD` |
| `passengers` | `PASS` |
| `mail` | `MAIL` |

These labels are present in `cargotable` but are **not** redefined with
`item(FEAT_CARGOS, ...)`.

### Custom cargoes

OpenTTD reserves original cargo slots 0–11. Core Economy therefore allocates
all custom cargo items from slot 12 upward, with an explicit `number` property
matching the item ID. Current allocation:

| Slot range | Canonical cargoes |
| :--- | :--- |
| `12–21` | `fish`, `stone`, `clay`, `gas`, `sand`, `bauxite`, `titanium_ore`, `gold_ore`, `silver_ore`, `rare_earth_ore` |
| `22–31` | `coke`, `copper`, `glass`, `ceramics`, `aluminum`, `titanium`, `silver`, `rare_earth_materials`, `lime`, `cement` |
| `32–41` | `lumber`, `petroleum_products`, `machinery`, `chemicals`, `manufactured_goods`, `electronics`, `advanced_goods`, `tools_hardware`, `industrial_equipment`, `construction_materials` |
| `42–45` | `agricultural_supplies`, `technology_systems`, `fuel`, `personnel` |

`coke` is therefore a valid custom cargo slot and is no longer assigned to an
original/default cargo slot.

## Canonical Translation Table

The generated `core_economy.nml` must contain this exact stable order:

```text
GRAI, LVST, WOOD, FISH, COAL, IORE, STON, CLAY, OIL_, GAS_, CORE, SAND,
BAUX, TIO_, GORE, SORE, REOR, COKE, STEL, COPP, GLAS, CERA, ALUM, TITN,
GOLD, SILV, REMT, LIME, CEMT, FOOD, LUMB, PETR, MACH, CHEM, MNFG, ELEC,
ADVG, HARD, INDE, CNST, AGRI, TECH, FUEL, PASS, PERS, MAIL
```

Every canonical label must be represented either by an OpenTTD built-in
label above or by exactly one custom cargo item. The validation gate enforces
this invariant.

## Industry Mapping & Date Gating

| Core Economy ID | Industry Name | Role | Era Start | Built-in Substitution Constant |
| :--- | :--- | :--- | :--- | :--- |
| `MIN_COAL_EARLY` | Coal Mine | Extraction | 1700 | `INDUSTRYTYPE_COAL_MINE` |
| `MIN_IRON` | Iron Mine | Extraction | 1700 | `INDUSTRYTYPE_IRON_ORE_MINE` |
| `PRC_COKE` | Coke Works | Processing | 1750 | `INDUSTRYTYPE_TEMPERATE_FACTORY` |
| `PRC_STEEL` | Steel Mill | Processing | 1750 | `INDUSTRYTYPE_STEEL_MILL` |

OpenTTD industry introduction is handled by the existing construction
probability/date callback. The economic dates in the JSON contract are not
changed by the cargo adapter.

## Recipe & Production Mechanics

### Coke Works (`coal_to_coke`)

- Canonical recipe: `1 coal → 1 coke`.
- NML production callback consumes waiting `COAL` and produces the same amount
  of `COKE`.

### Steel Mill (`iron_ore_coke_to_steel`)

- Canonical recipe: `1 iron_ore + 1 coke → 1 steel`.
- NML production callback computes the minimum waiting amount of `IORE` and
  `COKE`, consumes that amount of each, and produces the same amount of `STEL`.

## Technical Invariants

1. Stage 2 economic JSON is the source of truth.
2. Original OpenTTD cargo slots 0–11 are never occupied by custom items.
3. Every custom cargo has `number == item ID`.
4. No built-in cargo label is redefined as a custom cargo.
5. The canonical translation table contains every canonical label exactly once
   and preserves its stable order.
6. Custom cargo item IDs remain below OpenTTD's 64-cargo maximum.
7. The cargo adapter does not alter recipes, industry IDs, or historical dates.

## OpenTTD / NewGRF Technical Notes

- `nmlc` compiles the generated `core_economy.nml` entry point.
- Modular NML source remains split into cargo, graphics, production, and
  industry fragments.
- GameScript and other deferred systems remain outside this adapter slice.

# OpenTTD NewGRF Adapter — Core Economy v0.4.0 Vertical Slice Mapping

## Overview

This adapter implements the first vertical slice of **Core Economy v0.4.0** for OpenTTD using NML/NewGRF.

The vertical slice represents the core heavy industry coal/coke/steel production chain:
- **Coal Mine** (`MIN_COAL_EARLY`) → `coal`
- **Iron Mine** (`MIN_IRON`) → `iron_ore`
- **Coke Works** (`PRC_COKE`): `coal` → `coke`
- **Steel Mill** (`PRC_STEEL`): `iron_ore` + `coke` → `steel`

---

## Canonical ID to OpenTTD Representation Mapping

### 1. Cargo Mapping

| Core Economy ID | OpenTTD Cargo Label | Cargo Type Category | OpenTTD Cargo Class | Introduced | NML Definition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `coal` | `"COAL"` | Built-in Cargo | `CC_BULK` | 1700 | `cargotable` entry |
| `iron_ore` | `"IORE"` | Built-in Cargo | `CC_BULK` | 1700 | `cargotable` entry |
| `coke` | `"COKE"` | Custom Cargo | `CC_BULK` | 1750 | `cargotable` entry + `item(FEAT_CARGOS, cargo_coke, 2)` |
| `steel` | `"STEL"` | Built-in Cargo | `CC_PIECE_GOODS` | 1750 | `cargotable` entry |

### 2. Industry Mapping & Date Gating

| Core Economy ID | Industry Name | Role | Era Start | Built-in Substitution Constant | Cargo Types Declaration (`cargo_types`) | Date Gating Callback |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MIN_COAL_EARLY` | Coal Mine | Extraction | 1700 | `INDUSTRYTYPE_COAL_MINE` | `[produce_cargo("COAL", 10)]` | Always available (1700+) |
| `MIN_IRON` | Iron Mine | Extraction | 1700 | `INDUSTRYTYPE_IRON_ORE_MINE` | `[produce_cargo("IORE", 10)]` | Always available (1700+) |
| `PRC_COKE` | Coke Works | Processing | 1750 | `INDUSTRYTYPE_TEMPERATE_FACTORY` | `[accept_cargo("COAL", produce_cargo("COKE", 0))]` | `location_check: current_year >= 1750 ? CB_RESULT_LOCATION_ALLOW : CB_RESULT_LOCATION_DISALLOW;` |
| `PRC_STEEL` | Steel Mill | Processing | 1750 | `INDUSTRYTYPE_STEEL_MILL` | `[accept_cargo("IORE", produce_cargo("STEL", 0)), accept_cargo("COKE", produce_cargo("STEL", 0))]` | `location_check: current_year >= 1750 ? CB_RESULT_LOCATION_ALLOW : CB_RESULT_LOCATION_DISALLOW;` |

---

## Recipe & Production Mechanics

### 1. Coke Works (`coal_to_coke`)
- **Canonical Recipe**: 1 unit `coal` → 1 unit `coke`
- **NML Implementation**: Custom `produce` callback (`coke_works_produce_cb`) wired to `produce_cargo_arrival` callback in graphics block. Consumes 100% of waiting `COAL` cargo and outputs an equal quantity of `COKE`.

### 2. Steel Mill (`iron_ore_coke_to_steel`)
- **Canonical Recipe**: 1 unit `iron_ore` + 1 unit `coke` → 1 unit `steel`
- **NML Implementation**: Custom `produce` callback (`steel_mill_produce_cb`) wired to `produce_cargo_arrival` callback in graphics block. Computes $M = \min(\text{waiting } \text{IORE}, \text{waiting } \text{COKE})$, consumes $M$ units of `IORE` and $M$ units of `COKE`, and outputs $M$ units of `STEL`.

---

## Graphics & Testability

Custom graphics sprites are deferred for this slice per specification. The adapter uses tile substitution (`substitute` property) referencing default OpenTTD industry sprites and tile layouts:
- Coal Mine uses default OpenTTD Coal Mine tiles (`0x08`–`0x0B`).
- Iron Mine uses default OpenTTD Iron Ore Mine tiles (`0x12`–`0x15`).
- Coke Works uses default OpenTTD Factory tiles (`0x1E`–`0x21`).
- Steel Mill uses default OpenTTD Steel Mill tiles (`0x00`–`0x03`).

---

## OpenTTD / NewGRF Technical Limitations & Design Decisions

1. **Standalone Compilation Requirement**: `nmlc` parses a single NML file per execution and does not provide native `#include` pre-processing. The combined entry point file `core_economy.nml` concatenates the modular blocks for compilation.
2. **Built-in vs Custom Cargoes**: Standard cargoes (`COAL`, `IORE`, `STEL`) are declared in `cargotable` without re-defining them as custom cargo items, avoiding cargo table duplication. Custom cargoes (`COKE`) are defined using `item(FEAT_CARGOS, cargo_coke, <id>)`.
3. **Industry Introduction Dates**: OpenTTD `FEAT_INDUSTRIES` lacks an `intro_year` property. Date gating is enforced dynamically via `construction_probability` graphics callback checking `current_year >= 1750`.
4. **GameScript Separation**: GameScript is omitted in this vertical slice. Dynamic state, settlement growth, and complex contract policy will be overlaid in the GameScript layer.


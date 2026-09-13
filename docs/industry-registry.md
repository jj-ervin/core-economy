# OpenTTD Economic Framework — Industry Registry

**Status:** Draft v0.2 — normalized reference registry  
**Timeline:** 1700–2150

## 1. Purpose

This registry defines the economic locations and activities used by the reference economy. The framework defines the rules; this document defines one coherent playable implementation of those rules.

> **The economy comes first. Vehicles serve the economy.**  
> **Simple rules. Deep logistics.**

This is a design registry, not yet a NewGRF/NML implementation specification.

## 2. Registry conventions

Each entry defines:

- **ID:** stable industry identity.
- **Role:** `extraction`, `processing`, `manufacturing`, `supply_production`, `service`, or `logistics`.
- **Module:** owning economic module.
- **New construction:** period when new construction is historically appropriate.
- **Hard inputs:** materials directly involved in production.
- **Operational supplies:** service inputs that normally improve productivity, capacity, reliability, or efficiency; they are not universal shutdown conditions.
- **Personnel:** labor intensity and whether a return trip is meaningful.
- **Outputs:** stable cargo identities.
- **Succession:** predecessor and successor within a historical family.
- **Geography and scale:** placement and economic significance.

A new-construction range does not automatically delete or invalidate an existing industry.

## 3. Canonical cargo vocabulary

### Primary resources

`Grain`, `Livestock`, `Timber`, `Fish`, `Coal`, `Iron Ore`, `Stone`, `Clay`, `Oil`, `Gas`, `Copper Ore`

### Products

`Food`, `Lumber`, `Steel`, `Copper`, `Petroleum Products`, `Machinery`, `Manufactured Goods`, `Electronics`, `Advanced Goods`

### Operational supplies

`Tools & Hardware`, `Industrial Equipment`, `Construction Materials`, `Agricultural Supplies`, `Technology Systems`, `Fuel`, `Chemicals`

`Chemicals` is intentionally multi-role: it is both a manufactured product and an operational supply. `Fuel` is a stable operational-energy cargo distributed from petroleum products through fuel depots or terminals.

## 4. Input semantics

The registry must not use ambiguous `and/or` recipes.

- **Required:** every listed input is required.
- **Proportional:** output scales with delivered input.
- **Alternative group:** one or more members of a named group may satisfy the same functional requirement. The validator must define whether the group means *at least one*, *exactly one*, or a weighted substitution.
- **Preferred:** improves the preferred production path but is not mandatory.
- **Optional:** may be used without becoming a universal requirement.
- **Supply:** operational-service relationship, not a production recipe.

Where an industry accepts several food feedstocks, the registry uses the explicit group `food_feedstock` with relationship `alternative`.

## 5. Historical industry families

### 5.1 Agriculture

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `AGR_FARM_TRAD` | Traditional Farm | extraction | Agriculture | 1700–1850 | — | Agricultural Supplies | High / returnable | Grain, Livestock | — | `AGR_FARM_MECH` | Fertile rural land | Small–Medium |
| `AGR_FARM_MECH` | Mechanized Farm | extraction | Agriculture | 1800–1950 | — | Agricultural Supplies; Tools & Hardware | Medium / returnable | Grain, Livestock | `AGR_FARM_TRAD` | `AGR_FARM_PREC` | Productive rural regions | Medium–Large |
| `AGR_FARM_PREC` | Precision Farm | extraction | Agriculture | 1980–2045 | — | Agricultural Supplies; Technology Systems | Low–Medium / returnable | Grain, Livestock | `AGR_FARM_MECH` | `AGR_FARM_AUTO` | Productive agricultural regions | Medium–Large |
| `AGR_FARM_AUTO` | Automated Farm | extraction | Agriculture | 2035–2150 | — | Technology Systems; Agricultural Supplies | Low / returnable | Grain, Livestock | `AGR_FARM_PREC` | — | Productive regions / controlled environments | Large |

### 5.2 Forestry

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `FOR_TRAD` | Traditional Forestry | extraction | Forestry | 1700–1850 | — | Tools & Hardware | High / returnable | Timber | — | `FOR_IND` | Forest regions | Small |
| `FOR_IND` | Industrial Forestry | extraction | Forestry | 1800–1950 | — | Tools & Hardware; Industrial Equipment | Medium / returnable | Timber | `FOR_TRAD` | `FOR_MECH` | Accessible forest regions | Medium |
| `FOR_MECH` | Mechanized Forestry | extraction | Forestry | 1920–2000 | — | Industrial Equipment; Tools & Hardware | Low–Medium / returnable | Timber | `FOR_IND` | `FOR_PREC` | Managed/commercial forests | Medium–Large |
| `FOR_PREC` | Precision / Sustainable Forestry | extraction | Forestry | 1980–2150 | — | Industrial Equipment; Technology Systems | Low / returnable | Timber | `FOR_MECH` | — | Managed forests | Medium–Large |

### 5.3 Fisheries

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `FIS_COAST` | Coastal Fishery | extraction | Fisheries | 1700–1900 | — | Tools & Hardware | High / returnable | Fish | — | `FIS_COMM` | Coastal waters | Small |
| `FIS_COMM` | Commercial Fishery | extraction | Fisheries | 1850–1970 | — | Industrial Equipment; Tools & Hardware | Medium / returnable | Fish | `FIS_COAST` | `FIS_ADV` | Coastal/offshore waters | Medium–Large |
| `FIS_ADV` | Advanced Fishery | extraction | Fisheries | 1970–2150 | — | Industrial Equipment; Technology Systems | Low–Medium / returnable | Fish | `FIS_COMM` | — | Coastal/offshore waters | Large |

### 5.4 Mining and quarrying

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MIN_COAL_EARLY` | Coal Mine | extraction | Heavy Industry | 1700–1900 | — | Tools & Hardware | Very High / returnable | Coal | — | `MIN_COAL_MECH` | Coal-bearing regions | Small–Large |
| `MIN_COAL_MECH` | Mechanized Coal Mine | extraction | Heavy Industry | 1850–2000 | — | Industrial Equipment; Tools & Hardware | Medium / returnable | Coal | `MIN_COAL_EARLY` | `MIN_COAL_MOD` | Coal-bearing regions | Medium–Large |
| `MIN_COAL_MOD` | Modern Coal Mine | extraction | Heavy Industry | 1950–2150 | — | Industrial Equipment; Technology Systems | Low–Medium / returnable | Coal | `MIN_COAL_MECH` | — | Coal-bearing regions | Large |
| `MIN_IRON` | Iron Mine | extraction | Heavy Industry | 1700–1950 | — | Tools & Hardware | High / returnable | Iron Ore | — | `MIN_IRON_MECH` | Iron-bearing regions | Small–Large |
| `MIN_IRON_MECH` | Mechanized Iron Mine | extraction | Heavy Industry | 1850–2150 | — | Industrial Equipment; Technology Systems | Medium–Low / returnable | Iron Ore | `MIN_IRON` | — | Iron-bearing regions | Medium–Large |
| `MIN_COPPER` | Copper Mine | extraction | Heavy Industry | 1850–2150 | — | Tools & Hardware; Industrial Equipment | Medium / returnable | Copper Ore | — | `MIN_COPPER_AUTO` | Copper-bearing regions | Medium |
| `MIN_COPPER_AUTO` | Automated Copper Mine | extraction | Heavy Industry | 2030–2150 | — | Industrial Equipment; Technology Systems | Low / returnable | Copper Ore | `MIN_COPPER` | — | Copper-bearing regions | Large |
| `MIN_QUARRY` | Quarry | extraction | Construction | 1700–2150 | — | Tools & Hardware; Industrial Equipment | Medium / returnable | Stone | — | — | Rock formations | Small–Large |
| `MIN_CLAY` | Clay Pit | extraction | Construction | 1700–2150 | — | Tools & Hardware; Industrial Equipment | Medium / returnable | Clay | — | — | Clay-bearing regions | Small–Medium |

### 5.5 Oil, gas, and offshore extraction

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MIN_OIL_ON` | Oil Field | extraction | Energy | 1850–2150 | — | Industrial Equipment; Technology Systems | Medium–Low / returnable | Oil | — | — | Petroleum-bearing regions | Medium–Large |
| `MIN_GAS_ON` | Gas Field | extraction | Energy | 1900–2150 | — | Industrial Equipment; Technology Systems | Medium–Low / returnable | Gas | — | — | Gas-bearing regions | Medium–Large |
| `OFF_PLATFORM_OIL` | Offshore Oil Platform | extraction | Offshore | 1930–2100 | Industrial Equipment + Construction Materials | Technology Systems; Industrial Equipment; Fuel | High / returnable | Oil | — | `OFF_PLATFORM_ADV` | Offshore petroleum fields | Large |
| `OFF_PLATFORM_ADV` | Advanced Offshore Platform | extraction | Offshore | 2000–2150 | Industrial Equipment + Construction Materials | Technology Systems; Fuel | Medium / returnable | Oil, Gas | `OFF_PLATFORM_OIL` | — | Offshore petroleum fields | Large |

Offshore sites create a deliberate round-trip logistics pattern: Personnel, Industrial Equipment, Construction Materials, and Fuel outbound; Oil/Gas and returning Personnel inbound.

## 6. Processing registry

### 6.1 Food processing

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PRC_FOOD` | Food Processing Plant | processing | Food | 1700–2150 | `food_feedstock` alternative group: Grain, Livestock, Fish | Tools & Hardware; Industrial Equipment; Fuel | Medium / returnable | Food | — | `PRC_FOOD_ADV` | Farms, fisheries, rail/port corridors | Small–Large |
| `PRC_FOOD_ADV` | Automated Food Processor | processing | Food | 2000–2150 | `food_feedstock` alternative group: Grain, Livestock, Fish | Technology Systems; Industrial Equipment; Fuel | Low / returnable | Food | `PRC_FOOD` | — | Major food/logistics regions | Large |

### 6.2 Timber processing

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PRC_SAWMILL` | Sawmill | processing | Forestry | 1700–2150 | Timber | Tools & Hardware; Industrial Equipment; Fuel | Medium / returnable | Lumber | — | `PRC_SAWMILL_AUTO` | Timber regions | Small–Large |
| `PRC_SAWMILL_AUTO` | Automated Sawmill | processing | Forestry | 1990–2150 | Timber | Industrial Equipment; Technology Systems; Fuel | Low / returnable | Lumber | `PRC_SAWMILL` | — | Timber/logistics regions | Large |

### 6.3 Steel

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PRC_STEEL` | Steel Mill | processing | Heavy Industry | 1750–2150 | Iron Ore + Coal | Industrial Equipment; Construction Materials; Fuel | High–Medium / returnable | Steel | — | `PRC_STEEL_ADV` | Ore/coal regions or rail/water corridors | Large |
| `PRC_STEEL_ADV` | Advanced Steel Works | processing | Heavy Industry | 1980–2150 | Iron Ore + Coal or explicitly enabled Energy alternative | Industrial Equipment; Technology Systems; Fuel | Medium–Low / returnable | Steel | `PRC_STEEL` | — | Major industrial regions | Large |

### 6.4 Petroleum and chemicals

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PRC_REFINERY` | Refinery | processing | Energy | 1850–2150 | Oil | Industrial Equipment; Construction Materials; Fuel | Medium / returnable | Petroleum Products | — | `PRC_REFINERY_ADV` | Oil regions, ports, pipeline/rail hubs | Large |
| `PRC_REFINERY_ADV` | Advanced Refinery | processing | Energy | 1980–2150 | Oil | Technology Systems; Industrial Equipment; Fuel | Low–Medium / returnable | Petroleum Products | `PRC_REFINERY` | — | Major energy/industrial hubs | Large |
| `PRC_CHEM` | Chemical Works | processing | Chemicals | 1850–2150 | Explicitly defined chemical feedstock: Petroleum Products, or Gas where the Gas-feedstock option is enabled | Industrial Equipment; Technology Systems; Fuel | Medium / returnable | Chemicals | — | `PRC_CHEM_ADV` | Industrial/refinery corridors | Medium–Large |
| `PRC_CHEM_ADV` | Advanced Chemical Works | processing | Chemicals | 2000–2150 | Explicitly defined chemical feedstock group | Technology Systems; Industrial Equipment; Fuel | Low / returnable | Chemicals | `PRC_CHEM` | — | Advanced industrial regions | Large |

**Canonical separation:** `PRC_REFINERY` produces `Petroleum Products`; `PRC_CHEM` produces `Chemicals`. Gas may be used by Chemical Works only through an explicit gas-feedstock recipe, never through implied `and/or` wording.

## 7. Manufacturing registry

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MFG_MACH` | Machinery Works | manufacturing | Manufacturing | 1800–2150 | Steel + Copper + Chemicals | Industrial Equipment; Technology Systems; Fuel | Medium–High / returnable | Machinery | — | `MFG_MACH_ADV` | Industrial regions | Medium–Large |
| `MFG_MACH_ADV` | Advanced Machinery Works | manufacturing | Manufacturing | 1950–2150 | Steel + Copper + Chemicals | Technology Systems; Industrial Equipment; Fuel | Medium–Low / returnable | Machinery | `MFG_MACH` | — | Advanced industrial regions | Large |
| `MFG_FACTORY` | Factory | manufacturing | Manufacturing | 1850–2150 | Steel + Lumber | Industrial Equipment; Tools & Hardware; Fuel | Medium / returnable | Manufactured Goods | — | `MFG_FACTORY_ADV` | Industrial/urban regions | Medium–Large |
| `MFG_FACTORY_ADV` | Advanced Factory | manufacturing | Manufacturing | 1980–2150 | Steel + Lumber + Machinery | Technology Systems; Industrial Equipment; Fuel | Low–Medium / returnable | Manufactured Goods | `MFG_FACTORY` | — | Major industrial regions | Large |
| `MFG_ELECTRONICS` | Electronics Works | manufacturing | Technology | 1950–2150 | Copper + Chemicals | Technology Systems; Industrial Equipment; Fuel | Medium–Low / returnable | Electronics | — | `MFG_ELECTRONICS_ADV` | Technology/industrial regions | Medium–Large |
| `MFG_ELECTRONICS_ADV` | Advanced Electronics Works | manufacturing | Technology | 2000–2150 | Copper + Chemicals + Machinery | Technology Systems; Industrial Equipment; Fuel | Low / returnable | Electronics | `MFG_ELECTRONICS` | — | Advanced technology regions | Large |
| `MFG_ADVANCED` | Advanced Goods Works | manufacturing | Advanced Technology | 2000–2150 | Electronics + Chemicals + Machinery | Technology Systems; Industrial Equipment; Fuel | Low–Medium / returnable | Advanced Goods | — | — | Advanced technology regions | Large |

No `processed copper` cargo exists. The canonical copper chain is `Copper Ore → Copper Works → Copper`.

## 8. Supply-production registry

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|
| `SUP_COPPER` | Copper Works | processing | Heavy Industry | 1850–2150 | Copper Ore | Industrial Equipment; Fuel | Medium / returnable | Copper | Copper-bearing/industrial regions | Medium–Large |
| `SUP_CONSTRUCTION` | Construction Materials Works | supply_production | Construction | 1700–2150 | Stone + Clay + Lumber + Steel | Industrial Equipment; Fuel | Medium / returnable | Construction Materials | Construction/industrial regions | Medium–Large |
| `SUP_AGRICULTURE` | Agricultural Supplies Works | supply_production | Agriculture | 1800–2150 | Chemicals + Food-processing or approved agricultural feedstock | Industrial Equipment; Technology Systems; Fuel | Medium / returnable | Agricultural Supplies | Agricultural/industrial regions | Medium–Large |
| `SUP_FUEL` | Fuel Depot / Terminal | logistics | Energy | 1850–2150 | Petroleum Products | Industrial Equipment; Fuel | Low / returnable | Fuel | Ports, rail hubs, truck hubs, airports | Small–Large |

`Fuel Depot / Terminal` is a logistics and distribution node, not a refinery or chemical-manufacturing substitute.

## 9. Ports and logistics

Ports are economic organisms with changing roles, not merely interchangeable station graphics.

| ID | Name | Role | Module | New construction | Hard inputs | Operational supplies | Personnel | Outputs/flows | Geography |
|---|---|---|---|---|---|---|---|---|---|
| `POR_TRADING` | Trading Wharf | logistics | Maritime | 1700–1850 | — | Fuel; Tools & Hardware | Low / returnable | General trade flows | Rivers/coasts |
| `POR_COMMERCIAL` | Commercial Harbor | logistics | Maritime | 1800–1950 | — | Fuel; Construction Materials | Medium / returnable | Passenger, Mail, general cargo | Commercial coasts |
| `POR_INDUSTRIAL` | Industrial Port | logistics | Maritime | 1850–2150 | — | Fuel; Industrial Equipment; Construction Materials | Medium / returnable | Bulk and industrial cargo | Industrial coasts |
| `POR_FISHING` | Fishing Harbor | logistics | Fisheries | 1700–2150 | — | Fuel; Tools & Hardware; Industrial Equipment | Medium / returnable | Fish and fishing logistics | Fishing coasts |
| `POR_DEEPWATER` | Deepwater Port | logistics | Maritime | 1900–2150 | — | Fuel; Construction Materials; Technology Systems | High / returnable | Long-distance bulk cargo | Deepwater coasts |
| `POR_CONTAINER` | Container Port | logistics | Global Logistics | 1960–2150 | — | Fuel; Industrial Equipment; Technology Systems | High / returnable | Manufactured Goods, Electronics, Advanced Goods | Global trade corridors |
| `POR_MEGA` | Smart / Mega Port | logistics | Global Logistics | 2000–2150 | — | Fuel; Industrial Equipment; Technology Systems | Medium / returnable | High-volume integrated cargo flows | Major global hubs |
| `OFF_SUPPLY_BASE` | Offshore Supply Base | logistics | Offshore | 1930–2150 | — | Fuel; Industrial Equipment; Construction Materials; Technology Systems | High / returnable | Offshore personnel/equipment supply | Offshore-support coasts |

## 10. Service and town relationships

- **Towns** accept `Food`, `Manufactured Goods`, and other explicitly enabled consumer flows.
- **Passengers** represent ordinary travel and are not interchangeable with `Personnel`.
- **Personnel** is sent to productive sites because those sites need labor.
- **Returning Personnel** may be implemented as a state or adapter behavior rather than a separate cargo identity.
- **Mail** represents physical communication and parcels.

## 11. Succession rules

Succession is represented here as one predecessor/successor relationship per industry family. A future machine-readable definition should make this relationship the single source of truth rather than duplicating competing succession records in multiple files.

Successors may change:

- base capacity;
- labor intensity;
- operational-supply profile;
- geography;
- storage;
- accepted hard-input recipes;
- technology state.

They should not create duplicate cargo identities merely because technology changed.

## 12. Registry guardrails

1. Do not use `and/or` in a production definition.
2. Do not describe Refinery as producing `Chemicals`.
3. Do not use `processed copper`; use `Copper`.
4. Do not treat Fuel Depot / Terminal as a manufacturing industry.
5. Do not make every operational supply a universal hard input.
6. Do not make `optional` the only semantic cargo class for an economically active cargo.
7. Do not create duplicate cargoes for historical technology states when the economic identity is stable.
8. Do not introduce a successor without documenting its predecessor and transition logic.
9. Do not introduce a module dependency that is not explicitly declared.
10. Validate source coverage, consumer coverage, recipe semantics, cycles, dependency depth, era consistency, and module isolation before implementation.

## 13. Implementation boundary

This registry is the human-readable reference economy. It must eventually be represented as machine-readable economy data and checked by the validation engine before NewGRF/NML generation.

```text
Industry Registry
      ↓
Machine-readable Economy Definition
      ↓
Validation
      ↓
NewGRF / NML adapter
```

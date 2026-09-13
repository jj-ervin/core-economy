# Industry Registry: 1700–2150

## 1. Purpose

This document is the concrete industry registry for the OpenTTD Economic Framework reference economy.

The framework defines the economic grammar. The reference economy defines one playable economy. This registry defines the **places where that economy happens**.

It is intended to expose contradictions before NewGRF implementation begins.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

This is a design registry, not yet a NewGRF implementation specification.

---

# 2. Registry Rules

Each industry entry defines:

- **ID** — stable machine-readable identity.
- **Name** — player-facing name; may vary by technology state.
- **Role** — extraction, processing, manufacturing, infrastructure/supply production, or service/logistics.
- **Module** — core or optional economic module.
- **Era** — first meaningful appearance and broad historical availability.
- **Technology state** — the economic/technical character of the industry.
- **Hard inputs** — inputs required for production. Keep these limited.
- **Operational supplies** — productivity inputs that improve output but normally do not hard-stop production.
- **Personnel** — labor demand and whether workers can return.
- **Outputs** — primary products and resources.
- **Predecessor / successor** — industry succession family.
- **Geography** — location logic.
- **Scale** — approximate economic scale.
- **Storage** — important stockpiling characteristics.
- **Notes** — special rules or unresolved design questions.

### Era notation

- **T** = Transformation, 1700–1850
- **A** = Acceleration, 1851–2000
- **C** = Convergence, 2001–2150

A range describes the period in which **new construction** is appropriate, not necessarily the date an existing industry disappears.

---

# 3. Industry ID Convention

IDs use stable semantic families rather than names tied to a single historical technology.

```text
AGR_     Agriculture
FOR_     Forestry
FIS_     Fisheries
MIN_     Mining / extraction
PRC_     Processing
MFG_     Manufacturing
SUP_     Operational-input production
POR_     Ports
SHP_     Shipbuilding / maritime industry
OFF_     Offshore
LOG_     Logistics / distribution
SRV_     Service / market infrastructure
FIN_     Finance (optional)
TEC_     Advanced technology (optional)
```

A successor should normally receive a new industry ID when its production behavior, construction rules, or technology state materially changes. Cargo identities should remain stable where possible.

---

# 4. Core Agriculture Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGR_FARM_TRAD | Traditional Farm | Extraction | Agriculture | 1700–1850 | — | Agricultural Supplies | High / returnable | Grain, Livestock | — | AGR_FARM_MECH | Rural fertile land | Small–Medium |
| AGR_FARM_MECH | Mechanized Farm | Extraction | Agriculture | 1800–1950 | — | Agricultural Supplies, Tools & Hardware | Medium / returnable | Grain, Livestock | AGR_FARM_TRAD | AGR_FARM_PREC | Rural fertile land | Medium–Large |
| AGR_FARM_PREC | Precision Farm | Extraction | Agriculture | 1980–2045 | — | Agricultural Supplies, Technology Systems | Low–Medium / returnable | Grain, Livestock | AGR_FARM_MECH | AGR_FARM_AUTO | Productive agricultural regions | Medium–Large |
| AGR_FARM_AUTO | Automated Farm | Extraction | Agriculture | 2035–2150 | — | Technology Systems, Agricultural Supplies | Low / returnable | Grain, Livestock | AGR_FARM_PREC | — | Productive regions / controlled environments | Large |

**Design note:** Farm output identities remain stable across the timeline. Technology changes labor intensity and supply dependence rather than creating separate cargoes for mechanized or precision agriculture.

---

# 5. Forestry Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FOR_TRAD | Traditional Forestry | Extraction | Forestry | 1700–1850 | — | Tools & Hardware | High / returnable | Timber | — | FOR_IND | Forest regions | Small |
| FOR_IND | Industrial Forestry | Extraction | Forestry | 1800–1950 | — | Tools & Hardware, Industrial Equipment | Medium / returnable | Timber | FOR_TRAD | FOR_MECH | Forest regions with transport access | Medium |
| FOR_MECH | Mechanized Forestry | Extraction | Forestry | 1920–2000 | — | Industrial Equipment, Tools & Hardware | Low–Medium / returnable | Timber | FOR_IND | FOR_PREC | Managed / commercial forests | Medium–Large |
| FOR_PREC | Precision / Sustainable Forestry | Extraction | Forestry | 1980–2150 | — | Industrial Equipment, Technology Systems | Low / returnable | Timber | FOR_MECH | — | Managed forests / sustainable production regions | Medium–Large |

Optional forestry modules may add biomass, paper, pulp, or ecological services without changing the core Timber chain.

---

# 6. Fisheries Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FIS_COAST | Coastal Fishery | Extraction | Fisheries | 1700–1900 | — | Tools & Hardware | High / returnable | Fish | — | FIS_COMM | Coastal waters | Small |
| FIS_COMM | Commercial Fishery | Extraction | Fisheries | 1850–1970 | — | Industrial Equipment, Tools & Hardware | Medium / returnable | Fish | FIS_COAST | FIS_ADV | Coastal / offshore waters | Medium–Large |
| FIS_ADV | Advanced Fishery | Extraction | Fisheries | 1970–2150 | — | Industrial Equipment, Technology Systems | Low–Medium / returnable | Fish | FIS_COMM | — | Coastal / offshore waters | Large |

Refrigerated logistics is represented primarily through vehicle, storage, and technology progression rather than a separate refrigerated-fish cargo.

---

# 7. Mining and Extraction Registry

## 7.1 Coal

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN_COAL_EARLY | Coal Mine | Extraction | Heavy Industry | 1700–1900 | — | Tools & Hardware | Very High / returnable | Coal | — | MIN_COAL_MECH | Coal-bearing regions | Small–Large |
| MIN_COAL_MECH | Mechanized Coal Mine | Extraction | Heavy Industry | 1850–2000 | — | Industrial Equipment, Tools & Hardware | Medium / returnable | Coal | MIN_COAL_EARLY | MIN_COAL_MOD | Coal-bearing regions | Medium–Large |
| MIN_COAL_MOD | Modern Coal Mine | Extraction | Heavy Industry | 1950–2150 | — | Industrial Equipment, Technology Systems | Low–Medium / returnable | Coal | MIN_COAL_MECH | — | Coal-bearing regions | Large |

Existing coal mines may continue beyond the period of new construction as long as economically viable. Their production can decline through demand and technology rather than forced deletion.

## 7.2 Iron

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN_IRON | Iron Mine | Extraction | Heavy Industry | 1700–1950 | — | Tools & Hardware | High / returnable | Iron Ore | — | MIN_IRON_MECH | Iron-bearing regions | Small–Large |
| MIN_IRON_MECH | Mechanized Iron Mine | Extraction | Heavy Industry | 1850–2150 | — | Industrial Equipment, Technology Systems | Medium–Low / returnable | Iron Ore | MIN_IRON | — | Iron-bearing regions | Medium–Large |

## 7.3 Copper

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN_COPPER | Copper Mine | Extraction | Heavy Industry | 1850–2150 | — | Tools & Hardware, Industrial Equipment | Medium / returnable | Copper Ore | — | MIN_COPPER_AUTO | Copper-bearing regions | Medium |
| MIN_COPPER_AUTO | Automated Copper Mine | Extraction | Heavy Industry | 2030–2150 | — | Industrial Equipment, Technology Systems | Low / returnable | Copper Ore | MIN_COPPER | — | Copper-bearing regions | Large |

## 7.4 Stone and Clay

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN_QUARRY | Quarry | Extraction | Construction | 1700–2150 | — | Tools & Hardware, Industrial Equipment | Medium / returnable | Stone | — | — | Rock formations / construction regions | Small–Large |
| MIN_CLAY | Clay Pit | Extraction | Construction | 1700–2150 | — | Tools & Hardware, Industrial Equipment | Medium / returnable | Clay | — | — | Clay-bearing regions | Small–Medium |

---

# 8. Oil and Gas Extraction Registry

## 8.1 Onshore Petroleum

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIN_OIL_ON | Oil Field | Extraction | Energy / Petroleum | 1850–2150 | — | Industrial Equipment, Technology Systems | Medium–Low / returnable | Oil | — | — | Petroleum-bearing regions | Medium–Large |
| MIN_GAS_ON | Gas Field | Extraction | Energy / Petroleum | 1900–2150 | — | Industrial Equipment, Technology Systems | Medium–Low / returnable | Gas | — | — | Gas-bearing regions | Medium–Large |

## 8.2 Offshore Petroleum

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OFF_PLATFORM_OIL | Offshore Oil Platform | Extraction | Offshore | 1930–2100 | Industrial Equipment, Construction Materials | Technology Systems, Industrial Equipment | High / returnable | Oil | — | OFF_PLATFORM_ADV | Offshore petroleum fields | Large |
| OFF_PLATFORM_ADV | Advanced Offshore Platform | Extraction | Offshore | 2000–2150 | Industrial Equipment, Construction Materials | Technology Systems | Medium / returnable | Oil, Gas | OFF_PLATFORM_OIL | — | Offshore petroleum fields | Large |

Offshore platforms are intentionally supply-intensive. The player can build a logistics network around personnel, equipment, construction materials, and returning workers rather than merely shipping Oil.

---

# 9. Processing Registry

## 9.1 Food Processing

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRC_FOOD | Food Processing Plant | Processing | Food | 1700–2150 | Grain and/or Livestock and/or Fish | Tools & Hardware, Industrial Equipment | Medium / returnable | Food | — | PRC_FOOD_ADV | Near farms, fisheries, rail/port corridors, cities | Small–Large |
| PRC_FOOD_ADV | Automated Food Processor | Processing | Food | 2000–2150 | Grain and/or Livestock and/or Fish | Technology Systems, Industrial Equipment | Low / returnable | Food | PRC_FOOD | — | Major food regions / logistics hubs | Large |

Regional variants may specialize in fewer accepted inputs. This should be a configuration choice, not a new cargo family.

## 9.2 Sawmill

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRC_SAWMILL | Sawmill | Processing | Forestry | 1700–2150 | Timber | Tools & Hardware, Industrial Equipment | Medium / returnable | Lumber | — | PRC_SAWMILL_AUTO | Forest / timber regions | Small–Large |
| PRC_SAWMILL_AUTO | Automated Sawmill | Processing | Forestry | 1990–2150 | Timber | Industrial Equipment, Technology Systems | Low / returnable | Lumber | PRC_SAWMILL | — | Timber / logistics regions | Large |

## 9.3 Steel Mill

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRC_STEEL | Steel Mill | Processing | Heavy Industry | 1750–2150 | Iron Ore + Coal | Industrial Equipment, Construction Materials | High–Medium / returnable | Steel | — | PRC_STEEL_ADV | Near ore/coal or major rail/water corridors | Large |
| PRC_STEEL_ADV | Advanced Steel Works | Processing | Heavy Industry | 1980–2150 | Iron Ore + energy pathway | Industrial Equipment, Technology Systems | Medium–Low / returnable | Steel | PRC_STEEL | — | Major industrial regions | Large |

The advanced steel pathway deliberately leaves energy sourcing open. An optional Energy module may later provide electricity, hydrogen, or other industrial energy inputs.

## 9.4 Refinery

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRC_REFINERY | Refinery | Processing | Petroleum | 1850–2150 | Oil | Industrial Equipment, Construction Materials | Medium / returnable | Chemicals | — | PRC_REFINERY_ADV | Oil regions, ports, pipeline/rail hubs | Large |
| PRC_REFINERY_ADV | Advanced Refinery | Processing | Petroleum | 1980–2150 | Oil | Technology Systems, Industrial Equipment | Low–Medium / returnable | Chemicals | PRC_REFINERY | — | Major energy / industrial hubs | Large |

Fuel is intentionally not a core cargo in this first registry. It can be introduced as an optional Energy/Transport module if gameplay demonstrates a meaningful reason to distinguish it from the broad Chemicals category.

## 9.5 Chemical Works

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRC_CHEM | Chemical Works | Processing | Chemicals | 1850–2150 | Oil and/or Gas | Industrial Equipment, Technology Systems | Medium / returnable | Chemicals | — | PRC_CHEM_ADV | Industrial regions / refinery corridors | Medium–Large |
| PRC_CHEM_ADV | Advanced Chemical Works | Processing | Chemicals | 2000–2150 | Chemicals feedstocks | Technology Systems, Industrial Equipment | Low / returnable | Chemicals | PRC_CHEM | — | Advanced industrial regions | Large |

---

# 10. Manufacturing Registry

## 10.1 Machinery

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MFG_MACH | Machinery Works | Manufacturing | Manufacturing | 1800–2150 | Steel + Copper Ore/processed copper + Chemicals | Industrial Equipment, Technology Systems | Medium–High / returnable | Machinery | — | MFG_MACH_ADV | Industrial regions | Medium–Large |
| MFG_MACH_ADV | Advanced Machinery Works | Manufacturing | Manufacturing | 1950–2150 | Steel + Chemicals + Electronics | Technology Systems, Industrial Equipment | Medium–Low / returnable | Machinery | MFG_MACH | — | Major industrial / technology regions | Large |

Where the core economy does not provide a dedicated copper-processing industry, Copper Ore may be accepted directly by selected manufacturing industries. This is an intentional simplification pending a dedicated metal-processing module.

## 10.2 Manufactured Goods

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MFG_FACTORY | Factory | Manufacturing | Manufacturing | 1800–2150 | Steel + Lumber + Chemicals + Machinery | Industrial Equipment, Technology Systems | Medium / returnable | Manufactured Goods | — | MFG_FACTORY_ADV | Industrial / urban regions | Large |
| MFG_FACTORY_ADV | Automated Factory | Manufacturing | Manufacturing | 1980–2150 | Steel + Lumber + Chemicals + Machinery + Electronics | Technology Systems | Low–Medium / returnable | Manufactured Goods | MFG_FACTORY | — | Major manufacturing / logistics hubs | Large |

## 10.3 Electronics

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MFG_ELECTRONICS | Electronics Factory | Manufacturing | Technology | 1950–2150 | Copper Ore/processed copper + Chemicals + Machinery | Technology Systems, Industrial Equipment | Medium / returnable | Electronics | — | MFG_ELECTRONICS_ADV | Technology / industrial clusters | Medium–Large |
| MFG_ELECTRONICS_ADV | Advanced Electronics Factory | Manufacturing | Technology | 1990–2150 | Electronics feedstock + Chemicals | Technology Systems | Low–Medium / returnable | Electronics | MFG_ELECTRONICS | — | Major technology clusters | Large |

## 10.4 Advanced Goods

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MFG_ADV | Advanced Manufacturing Facility | Manufacturing | Advanced Technology | 2000–2150 | Electronics + Chemicals + Machinery | Technology Systems, Industrial Equipment | Medium–Low / returnable | Advanced Goods | — | — | Major technology / research regions | Medium–Large |

Advanced Goods remain intentionally broad. A future module may split them into semiconductors, robotics, aerospace components, or other specialized categories only if the additional logistics creates meaningful gameplay.

---

# 11. Operational Supply Production Registry

Operational inputs are products in the economic model, but they are represented here as broad production capabilities rather than five mandatory dedicated industries in every map.

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|
| SUP_WORKS | General Works / Workshop | Supply Production | Core | 1700–1900 | Lumber and/or Steel | Tools & Hardware | Medium / returnable | Tools & Hardware | Town / industrial regions | Small–Medium |
| SUP_INDUSTRIAL | Industrial Equipment Works | Supply Production | Heavy Industry | 1850–2150 | Steel + Machinery | Industrial Equipment | Medium / returnable | Industrial Equipment | Industrial regions | Medium–Large |
| SUP_CONSTRUCTION | Construction Materials Works | Supply Production | Construction | 1700–2150 | Stone + Lumber + Steel | Industrial Equipment | Medium / returnable | Construction Materials | Near cities / infrastructure corridors | Medium–Large |
| SUP_AGRI | Agricultural Supply Works | Supply Production | Agriculture | 1800–2150 | Chemicals + Machinery | Technology Systems | Medium / returnable | Agricultural Supplies | Agricultural / chemical regions | Medium |
| SUP_TECH | Technology Systems Works | Supply Production | Technology | 1950–2150 | Electronics + Machinery + Chemicals | Technology Systems | Medium / returnable | Technology Systems | Technology / industrial hubs | Medium–Large |

### Supply simplification rule

These outputs are **service categories**, not necessarily separate visible industries in the first playable implementation. Several may originate from general factories or specialized industrial clusters.

The purpose is to preserve the economic role without forcing the player to build a five-industry supply chain before the main economy can function.

---

# 12. Port Registry

Ports are economic industries, not merely vehicle stations.

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs / Services | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| POR_WHARF | Trading Wharf | Service / Logistics | Maritime | 1700–1800 | Construction Materials | Tools & Hardware | Medium / returnable | Passenger, Mail, cargo transfer | — | POR_HARBOR | Rivers / sheltered coast | Small |
| POR_HARBOR | Commercial Harbor | Service / Logistics | Maritime | 1750–1900 | Construction Materials | Tools & Hardware, Industrial Equipment | Medium / returnable | Passenger, Mail, cargo transfer | POR_WHARF | POR_STEAM | Coastal cities / river mouths | Medium |
| POR_STEAM | Steam Harbor | Service / Logistics | Maritime | 1800–1900 | Construction Materials + Industrial Equipment | Industrial Equipment | Medium / returnable | Passenger, Mail, bulk cargo | POR_HARBOR | POR_INDUSTRIAL | Coastal / major rivers | Medium–Large |
| POR_INDUSTRIAL | Industrial Port | Service / Logistics | Maritime | 1850–1950 | Construction Materials + Industrial Equipment | Industrial Equipment | Medium / returnable | Bulk cargo, Passenger, Mail | POR_STEAM | POR_DEEP | Industrial coast | Large |
| POR_DEEP | Deepwater Port | Service / Logistics | Maritime | 1950–1970 | Construction Materials + Industrial Equipment | Industrial Equipment, Technology Systems | Medium / returnable | Bulk cargo, Passenger, Mail | POR_INDUSTRIAL | POR_CONTAINER | Deepwater coast | Large |
| POR_CONTAINER | Container Port | Service / Logistics | Global Logistics | 1965–2150 | Construction Materials + Industrial Equipment | Technology Systems | Low–Medium / returnable | Containerized / generalized cargo transfer | POR_DEEP | POR_SMART | Strategic deepwater coast | Very Large |
| POR_SMART | Smart / Mega Port | Service / Logistics | Global Logistics | 2000–2150 | Construction Materials + Industrial Equipment + Technology Systems | Technology Systems | Low / returnable | High-throughput cargo, Passenger, Mail | POR_CONTAINER | — | Global logistics hubs | Very Large |

The port succession describes **new construction technology and capability**. Existing ports can continue operating and can be upgraded where the implementation permits.

---

# 13. Specialized Port Registry

| ID | Name | Role | Module | Era | Hard Inputs | Supplies | Personnel | Services | Geography |
|---|---|---|---|---|---|---|---|---|---|
| POR_FISH | Fishing Harbor | Service / Logistics | Fisheries | 1700–2150 | Construction Materials | Industrial Equipment | Medium / returnable | Fish logistics, vessel service | Fishing coasts |
| POR_OIL | Oil Port | Service / Logistics | Petroleum | 1900–2150 | Construction Materials + Industrial Equipment | Technology Systems | Medium / returnable | Oil logistics | Petroleum coast |
| POR_SHIP | Shipbuilding Port | Manufacturing / Service | Maritime | 1750–2150 | Lumber + Steel + Machinery | Industrial Equipment, Technology Systems | High–Medium / returnable | Vessel construction / repair | Industrial coasts |
| POR_OFFSHORE | Offshore Supply Base | Service / Logistics | Offshore | 1930–2150 | Construction Materials + Industrial Equipment | Technology Systems | Medium / returnable | Personnel, equipment, construction logistics | Offshore-support coast |

Specialized ports should be implemented only where the service distinction creates a meaningful routing decision. They should not become cosmetic station variants.

---

# 14. Shipbuilding Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHP_YARD_SAIL | Sailing Shipyard | Manufacturing | Maritime | 1700–1850 | Timber + Lumber + Construction Materials | Tools & Hardware | High / returnable | Ships / maritime service capacity | — | SHP_YARD_STEAM | Coastal cities | Medium |
| SHP_YARD_STEAM | Steam Shipyard | Manufacturing | Maritime | 1800–1950 | Steel + Lumber + Machinery | Industrial Equipment | High / returnable | Ships / maritime service capacity | SHP_YARD_SAIL | SHP_YARD_MOD | Industrial coast | Large |
| SHP_YARD_MOD | Modern Shipyard | Manufacturing | Maritime | 1950–2150 | Steel + Machinery + Electronics | Industrial Equipment, Technology Systems | Medium / returnable | Ships / maritime service capacity | SHP_YARD_STEAM | — | Major ports | Very Large |

Ships themselves remain vehicles. Shipyards represent the economic industry that consumes industrial inputs and supports maritime network growth.

---

# 15. Offshore Energy Registry

Offshore energy is an optional Convergence module.

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Predecessor | Successor | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OFF_WIND_FIXED | Fixed Offshore Wind Farm | Energy Production | Offshore Energy | 2000–2060 | Industrial Equipment + Construction Materials | Technology Systems | Medium / returnable | Electricity* | — | OFF_WIND_FLOAT | Shallow / moderate offshore zones | Large |
| OFF_WIND_FLOAT | Floating Offshore Wind Farm | Energy Production | Offshore Energy | 2030–2150 | Industrial Equipment + Construction Materials | Technology Systems | Low–Medium / returnable | Electricity* | OFF_WIND_FIXED | OFF_ENERGY_COMPLEX | Deepwater offshore zones | Large |
| OFF_ENERGY_COMPLEX | Integrated Offshore Energy Complex | Energy Production / Service | Offshore Energy | 2050–2150 | Industrial Equipment + Construction Materials + Technology Systems | Technology Systems | Low–Medium / returnable | Electricity*, Hydrogen*, optional desalination/data services | OFF_WIND_FLOAT | — | Deepwater strategic zones | Very Large |

`*` Optional Energy module cargo/system.

The historical core economy must remain playable without Electricity or Hydrogen as physical cargoes.

---

# 16. Optional Research / Advanced Technology Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Outputs | Geography | Scale |
|---|---|---|---|---|---|---|---|---|---|---|
| TEC_RESEARCH | Research Facility | Service / Manufacturing | Advanced Technology | 1950–2150 | Electronics + Manufactured Goods | Technology Systems | High / returnable | Advanced Goods / technology capability | University / technology hubs | Medium–Large |
| TEC_ADV_RESEARCH | Advanced Research Complex | Service / Manufacturing | Advanced Technology | 2000–2150 | Electronics + Advanced Goods | Technology Systems | Medium / returnable | Advanced Goods / technology capability | Major research regions | Large |
| TEC_SPACE | Space Infrastructure Complex | Service / Manufacturing | Space | 2050–2150 | Advanced Goods + Machinery + Electronics | Technology Systems | High / returnable | Space services / optional cargoes | Specialized launch regions | Very Large |

Space remains optional and should not be required to complete the historical economy.

---

# 17. Town / Market Interface

Towns are not ordinary industries, but they are critical economic endpoints.

### Core town functions

```text
Passengers  ←→  Town
Mail        ←→  Town
Food        →    Town
Manufactured Goods → Town
Advanced Goods → Town (late era / optional)
```

Towns also act as major Personnel sources.

The first implementation should avoid turning towns into giant multi-input industries. Their primary purpose is to create demand, population, passenger flows, mail flows, and personnel supply.

---

# 18. Industry Lifecycle Rules

Every registry industry follows the same broad lifecycle:

```text
NOT AVAILABLE
      ↓
INTRODUCED
      ↓
GROWING
      ↓
MATURE
      ↓
LEGACY
      ↓
NO NEW CONSTRUCTION
```

### Important distinction

**No new construction does not mean no operation.**

A 1750 mine should not disappear simply because a 1900 mining technology becomes available.

Instead:

- old industry continues operating
- successor becomes available for new construction
- old industry may have different productivity
- old industry may have higher Personnel demand
- old industry may use more basic supplies
- new industry may have higher capacity or better supply efficiency

This creates historical progression without destroying the player's existing network.

---

# 19. Cross-Registry Economic Spines

The registry should preserve the five major production spines from `reference-economy.md`.

## Food

```text
AGR_FARM_* ──┐
             ├→ PRC_FOOD → Food → Towns
FIS_* ───────┘
```

## Industrialization

```text
FOR_* → PRC_SAWMILL → Lumber ─────┐
MIN_QUARRY → Stone ───────────────┼→ SUP_CONSTRUCTION / MFG
MIN_IRON_* + MIN_COAL_* → PRC_STEEL ┘
```

## Machinery

```text
Steel + Copper + Chemicals
          ↓
      MFG_MACH
          ↓
 Farms / Mines / Factories / Ports
```

## Petroleum / Chemicals

```text
MIN_OIL_* + MIN_GAS_*
          ↓
 PRC_REFINERY / PRC_CHEM
          ↓
       Chemicals
          ↓
Agriculture / Manufacturing / Technology
```

## Electronics / Automation

```text
Copper + Chemicals + Machinery
              ↓
        MFG_ELECTRONICS
              ↓
       SUP_TECH / MFG_ADV
              ↓
Automation / Advanced Industry
```

---

# 20. Contradiction Audit

This registry exposes several items that must be resolved before implementation.

## 20.1 Copper processing

**Status: OPEN**

Copper Ore currently enters selected manufacturing/electronics chains directly. A dedicated copper/metal processor would improve realism but risks adding another mandatory industry.

**Decision for reference implementation:** keep Copper Ore broad initially. Add a Copper Works only if network testing demonstrates a meaningful routing benefit.

## 20.2 Refinery output

**Status: OPEN**

The framework lists Chemicals as a broad product and the reference economy mentions petroleum/fuels. A dedicated Fuel cargo would increase realism but also complexity.

**Decision for reference implementation:** Chemicals remains the core refinery output. Fuel is optional.

## 20.3 Construction Materials source

**Status: OPEN**

The category currently represents a broad bundle of infrastructure materials. It may eventually deserve a dedicated processor.

**Decision for reference implementation:** allow SUP_CONSTRUCTION to consume Stone, Lumber, and Steel and produce Construction Materials. This creates a useful industrial spine without splitting cement, glass, brick, etc. into separate cargoes.

## 20.4 Agricultural Supplies source

**Status: RESOLVED FOR CORE**

Agricultural Supplies are produced by a broad Agricultural Supply Works rather than separate fertilizer, seed, pesticide, and equipment cargoes.

## 20.5 Technology Systems source

**Status: RESOLVED FOR CORE**

Technology Systems are produced by a broad Technology Systems Works. Electronics remains a general product that feeds this system.

## 20.6 Electricity

**Status: OPTIONAL**

Electricity should not become a mandatory physical cargo until an Energy module demonstrates a gameplay reason to transport it.

## 20.7 Personnel returnability

**Status: CORE RULE**

Personnel is returnable when an industry is designed around work assignments. The registry does not require every passenger-producing destination to generate Personnel continuously; Personnel demand is tied to industry capacity and labor intensity.

## 20.8 Port proliferation

**Status: CONTROLLED**

Port types should represent genuine economic specialization or capability. Do not create separate cargo classes merely because a port looks different.

---

# 21. Hard-Input Budget

A central balancing rule is that most industries should have **one to four meaningful hard inputs**.

Recommended ranges:

| Industry Type | Typical Hard Inputs |
|---|---:|
| Primary extraction | 0 |
| Simple processing | 1–2 |
| Heavy processing | 2–3 |
| Manufacturing | 2–4 |
| Advanced manufacturing | 3–5, only when justified |
| Ports / logistics | 0–3 construction inputs |
| Offshore construction | 2–4 |

Operational supplies do not count against the normal hard-input budget because they are productivity modifiers rather than universal production blockers.

---

# 22. Personnel Intensity Bands

Personnel demand is expressed as a relative intensity rather than a fixed universal number.

| Band | Meaning | Typical Industries |
|---|---|---|
| Very High | Labor is central to operation | Early mines, traditional farms, sailing shipyards |
| High | Large recurring workforces | Steel mills, traditional forestry, offshore construction |
| Medium | Significant but increasingly mechanized labor | Factories, modern farms, ports |
| Low–Medium | Mostly technical / maintenance labor | Advanced mines, automated factories |
| Low | Oversight and specialized intervention | Automated farms, smart ports |

Technology progression should generally reduce Personnel intensity while increasing demand for Industrial Equipment and Technology Systems.

---

# 23. Supply Progression

A typical industry family should evolve approximately like this:

```text
EARLY
Tools & Hardware
       ↓
INDUSTRIAL
Tools + Industrial Equipment
       ↓
MODERN
Industrial Equipment + Technology Systems
       ↓
AUTOMATED
Technology Systems + reduced Personnel
```

This lets the player experience technological change through logistics rather than a giant technology tree.

---

# 24. Geography Rules

Industry placement should create economic geography rather than random cargo sources.

### Primary resources

Strongly geography-dependent:

- farms → fertile land
- forests → forest regions
- fish → coast / water
- coal → coal geology
- iron → iron-bearing geology
- copper → copper-bearing geology
- stone → quarry geology
- clay → clay-bearing regions
- oil/gas → petroleum geology / offshore fields

### Processing

Should tend toward:

- resource proximity
- transport corridors
- energy availability where relevant
- existing industrial clusters
- ports
- cities / labor pools

### Advanced industry

Should increasingly cluster around:

- large cities
- educated labor pools
- major logistics hubs
- research centers
- reliable infrastructure

This produces natural regional specialization without hard-coding every possible industry location.

---

# 25. Network Complexity Target

The reference economy should feel interconnected but remain readable.

Target characteristics:

- most primary resources have at least one meaningful consumer
- most major products have at least two economic uses where justified
- operational inputs support many industries
- Personnel creates a human logistics layer
- ports create long-distance consolidation opportunities
- optional modules add depth without becoming mandatory
- no single industry should require a chain of six or more mandatory intermediate cargoes merely to function

The player should be able to understand a chain by following it visually.

---

# 26. Cargo Coverage Audit

### Primary resources with clear consumers

- Grain → Food Processing
- Livestock → Food Processing
- Timber → Sawmill
- Fish → Food Processing
- Coal → Steel / optional Energy
- Iron Ore → Steel
- Stone → Construction Materials
- Clay → Construction / optional ceramics
- Oil → Refinery
- Gas → Chemical Works / optional Energy
- Copper Ore → Machinery / Electronics

### Core products with clear consumers

- Food → Towns
- Lumber → Construction / Manufacturing
- Steel → Machinery / Manufacturing / Shipbuilding
- Machinery → Industrial operations / Manufacturing
- Chemicals → Agriculture / Manufacturing / Technology
- Manufactured Goods → Towns / markets
- Electronics → Technology Systems / Advanced Goods
- Advanced Goods → Towns / advanced industry / optional space

### Operational inputs with broad consumers

- Tools & Hardware → early and general maintenance
- Industrial Equipment → industrial modernization
- Construction Materials → expansion and infrastructure
- Agricultural Supplies → farms
- Technology Systems → late-era automation and advanced industry

No core cargo is intentionally left without a plausible source or consumer, subject to later production-balance testing.

---

# 27. Open Questions Before NewGRF Implementation

These should be resolved through a small playable prototype rather than speculative design alone.

1. Should Copper Works become a core processor?
2. Should Fuel become a core cargo?
3. Should Construction Materials be a visible cargo or an abstract construction cost?
4. How should OpenTTD represent Personnel returnability technically?
5. How should supply service levels be exposed to players?
6. How much industry upgrading can be represented without deleting/replacing existing industries?
7. Should ports have distinct production/acceptance behavior or primarily infrastructure capabilities?
8. How should industry geography be generated?
9. How should optional Energy cargo interact with vehicle loading and network economics?
10. What is the smallest viable industry subset that proves the framework works?

These are **implementation questions**, not reasons to expand the cargo vocabulary prematurely.

---

# 28. Recommended Prototype Slice

Before implementing all 1700–2150 industries, build a narrow vertical slice:

```text
Farm
  ↓
Grain
  ↓
Food Processing
  ↓
Food
  ↓
Town

Iron Mine + Coal Mine
          ↓
       Steel Mill
          ↓
         Steel
          ↓
      Machinery
          ↓
       Factory
          ↓
 Manufactured Goods
          ↓
         Town

Town
  ↓
Personnel
  ↓
Mine / Farm / Factory
  ↓
Returning Personnel
```

This slice proves:

- cargo ontology
- production inputs
- operational supplies
- Personnel
- returnable Personnel
- industry geography
- historical succession
- town demand
- productive round trips

Only after this works should the registry expand into the full reference economy.

---

# 29. Source-of-Truth Hierarchy

When documents disagree, use this hierarchy:

1. `docs/economic-model.md` — economic philosophy and roles
2. `docs/cargo-ontology.md` — cargo semantics
3. `docs/industry-model.md` — industry semantics
4. `docs/production-model.md` — production mechanics
5. `docs/personnel-model.md` — human logistics
6. `docs/era-model.md` — historical progression
7. `docs/reference-economy.md` — concrete economic design
8. `docs/industry-registry.md` — concrete industry instances
9. NewGRF implementation — technical adaptation

If implementation constraints force a deviation, record the deviation rather than silently changing the economic model.

---

# 30. Guiding Principle

The industry registry exists to make the economic model concrete without making it unnecessarily complicated.

> **An industry is a place where economic activity happens. A good industry creates a reason for a network to exist.**

The player should look at an industry and immediately understand:

- what it produces
- what keeps it productive
- where its workers come from
- where its output wants to go
- how its role changes through history
- why transporting something there can make money

If an industry cannot answer those questions clearly, it probably does not belong in the core economy.

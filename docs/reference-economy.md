# Reference Economy: 1700–2150

## 1. Purpose

This document defines the first concrete reference economy built on the OpenTTD Economic Framework.

The framework defines the grammar. This document defines one economy that speaks that grammar.

The reference economy spans **1700–2150** and is designed around three principles:

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

It is intended to be:

- historically recognizable
- modular
- interconnected without becoming cargo soup
- understandable to players
- deep enough to reward network design
- compatible with date-gated industry succession
- suitable for future OpenTTD/NewGRF implementation

This is a **reference design**, not yet an implementation specification.

---

# 2. Economic Architecture

The reference economy uses five economic roles:

```text
PRIMARY RESOURCES
        ↓
     PRODUCTS
        ↓
   MARKETS / INDUSTRIES

OPERATIONAL INPUTS ───────┐
                          ↓
                     INDUSTRIES
                          ↑
PERSONNEL ────────────────┘
```

Financial flows are optional and modular.

The economy is intentionally built around a limited number of stable cargo identities. Historical and technological change is represented primarily through industry states, production behavior, operational inputs, personnel demand, and transportation niches.

---

# 3. Core Cargo Set

The initial reference economy should begin with a deliberately constrained cargo vocabulary.

## Primary Resources

- Grain
- Livestock
- Timber
- Fish
- Coal
- Iron Ore
- Stone
- Clay
- Oil
- Gas
- Copper Ore

## Products

- Food
- Lumber
- Steel
- Machinery
- Chemicals
- Manufactured Goods
- Electronics
- Advanced Goods

## Operational Inputs

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems

## Human Flows

- Passengers
- Personnel
- Mail

## Optional Financial Flows

- Gold
- Bullion
- Coins / Cash
- Securities / Financial Documents

The final implementation may adjust this list after network testing. A cargo should be added only when it creates a meaningful economic distinction.

---

# 4. Primary Resource Families

## 4.1 Agriculture

Primary outputs:

```text
Farm → Grain
Farm → Livestock
```

Agriculture is one of the foundational economic systems across the entire timeline.

Industry succession:

```text
Traditional Farm
      ↓
Mechanized Farm
      ↓
Modern / Precision Farm
      ↓
Automated Farm
```

Operational inputs evolve from primarily Agricultural Supplies toward combinations of Agricultural Supplies, Industrial Equipment, and Technology Systems.

Personnel demand declines as mechanization and automation increase.

---

## 4.2 Forestry

```text
Forest
  ↓
Timber
  ↓
Sawmill
  ↓
Lumber
```

Forestry supports:

- construction
- shipbuilding
- furniture/manufacturing
- paper-related optional modules
- fuel/biomass optional modules

Industry succession:

```text
Traditional Forestry
      ↓
Industrial Forestry
      ↓
Mechanized Forestry
      ↓
Precision / Sustainable Forestry
```

---

## 4.3 Fisheries

```text
Fishing Grounds
      ↓
     Fish
      ↓
Food Processing
      ↓
     Food
```

Fishing begins as a coastal activity and later develops into larger commercial and offshore operations.

Transportation progression may include:

- fishing boats
- coastal fishing vessels
- commercial fishing fleets
- refrigerated logistics
- advanced fishing vessels

---

## 4.4 Coal

```text
Coal Mine
    ↓
   Coal
    ↓
Steel / Energy / Industrial Uses
```

Coal is especially important during the Transformation and Acceleration eras.

Its economic importance should decline as electricity, petroleum, and later cleaner energy systems expand, but existing coal industries should not simply vanish on a date.

---

## 4.5 Iron Ore

```text
Iron Mine
    ↓
Iron Ore
    ↓
Steel Mill
    ↓
Steel
```

Iron and steel form a major backbone of industrialization.

---

## 4.6 Stone and Clay

```text
Quarry → Stone
Clay Pit → Clay
```

These resources support:

- Construction Materials
- ceramics
- infrastructure
- industrial processing

They provide useful short- and medium-distance bulk transport opportunities.

---

## 4.7 Oil and Gas

```text
Oil Field / Offshore Platform
              ↓
             Oil
              ↓
          Refinery
              ↓
        Chemicals / Fuels
```

Gas can support:

- Chemicals
- electricity/energy modules
- industrial processes
- future hydrogen pathways

Oil becomes increasingly important during the Acceleration era and remains economically relevant even as alternatives emerge.

---

## 4.8 Copper Ore

```text
Copper Mine
     ↓
Copper Ore
     ↓
Metal / Component Processing
     ↓
Electronics / Machinery
```

Copper becomes increasingly important with electrification and electronics.

---

# 5. Processing Industries

## 5.1 Mill / Food Processing

```text
Grain + Livestock + Fish
            ↓
      Food Processing
            ↓
           Food
```

Not every location needs to accept every input. Regional specialization can be introduced through industry variants without creating new cargo types.

---

## 5.2 Sawmill

```text
Timber
  ↓
Sawmill
  ↓
Lumber
```

Lumber feeds construction and manufacturing.

---

## 5.3 Steel Mill

```text
Iron Ore + Coal
          ↓
      Steel Mill
          ↓
         Steel
```

Later technology may reduce coal dependence or introduce alternative processing pathways through optional energy/industrial modules.

---

## 5.4 Refinery

```text
Oil
 ↓
Refinery
 ↓
Chemicals
```

The refinery is a major industrial hub and becomes increasingly connected to manufacturing, transport, agriculture, and energy.

---

## 5.5 Chemical Works

```text
Oil / Gas + Industrial Inputs
              ↓
        Chemical Works
              ↓
          Chemicals
```

Chemicals support:

- Agriculture
- Manufacturing
- advanced materials
- future energy systems

---

# 6. Manufacturing Core

The reference economy uses a small number of broad manufacturing outputs rather than a huge catalog of finished goods.

## 6.1 Machinery

Inputs may include:

```text
Steel
Lumber
Copper / processed metals
Chemicals
Personnel
Industrial Equipment
```

Output:

```text
Machinery
```

Machinery supports farms, mines, factories, ports, and infrastructure.

---

## 6.2 Manufactured Goods

```text
Steel + Lumber + Chemicals + Machinery + Personnel
                    ↓
               Factory
                    ↓
          Manufactured Goods
```

Manufactured Goods represent a broad market category and should not be subdivided without a strong gameplay reason.

---

## 6.3 Electronics

Electronics become important primarily during the late Acceleration and Convergence eras.

Possible inputs:

```text
Copper / processed metals
Chemicals
Machinery
Technology Systems
Personnel
```

Output:

```text
Electronics
```

Electronics then support advanced manufacturing, automation, logistics, and optional future systems.

---

## 6.4 Advanced Goods

Advanced Goods are a deliberately broad late-era category.

Potential inputs:

- Electronics
- Chemicals
- Advanced materials
- Machinery
- Technology Systems
- Personnel

They should not become a catch-all cargo for every futuristic object. Their purpose is to represent economically meaningful high-complexity manufactured outputs without exploding the cargo list.

---

# 7. Operational Input Economy

Operational inputs are central to the framework because they make industries into maintained economic systems rather than static production boxes.

## 7.1 Tools & Hardware

Represents:

- hand tools
- replacement parts
- basic hardware
- maintenance materials
- workshop supplies

Broadly available from the early economy onward.

Likely consumers:

- farms
- mines
- forestry
- workshops
- ports
- factories

---

## 7.2 Industrial Equipment

Represents:

- heavy machinery
- production equipment
- pumps
- industrial systems
- replacement machinery

Its importance grows with industrialization.

Typical consumers:

- mines
- factories
- ports
- shipyards
- offshore facilities
- large farms

---

## 7.3 Construction Materials

Represents a broad infrastructure/construction input category.

Possible source industries include:

- sawmills
- steel mills
- quarries
- cement/construction-material processors in an optional detailed module

Consumers include:

- farms
- mines
- factories
- ports
- rail infrastructure
- offshore construction
- urban development

---

## 7.4 Agricultural Supplies

Represents:

- fertilizer
- seed/input packages
- agricultural chemicals
- crop treatment supplies
- farm consumables

Its technology changes through time while its economic identity remains stable.

---

## 7.5 Technology Systems

Represents:

- control systems
- sensors
- computing hardware
- communications equipment
- automation systems
- advanced industrial electronics

Technology Systems become increasingly important during the Convergence era.

---

# 8. Personnel Economy

Personnel connects population geography to industrial capacity.

The reference economy treats Personnel as labor transport, not ordinary passenger movement.

Examples:

```text
Town → Personnel → Mine
Town → Personnel → Farm
City → Personnel → Factory
Coastal City → Personnel → Offshore Platform
Research Hub → Personnel → Research Facility
```

Personnel demand generally declines as automation increases, but remote and specialized operations retain meaningful labor requirements.

Returnable Personnel can create productive round trips:

```text
Personnel + Supplies
        ↓
     Worksite
        ↓
Product + Returning Personnel
```

---

# 9. The Core Production Web

The reference economy is built around several major economic spines.

## Spine A — Food

```text
Grain ─────┐
Livestock ─┼→ Food Processing → Food → Towns
Fish ──────┘
```

## Spine B — Construction / Industrialization

```text
Timber → Lumber ─────┐
                     ├→ Construction / Manufacturing
Stone ───────────────┤
Iron Ore + Coal → Steel ─┘
```

## Spine C — Machinery

```text
Steel + Copper + Chemicals
            ↓
         Machinery
            ↓
 Farms / Mines / Factories / Ports
```

## Spine D — Petroleum / Chemicals

```text
Oil + Gas
   ↓
Refinery / Chemical Works
   ↓
Chemicals
   ↓
Agriculture / Manufacturing / Advanced Industry
```

## Spine E — Electronics / Automation

```text
Copper + Chemicals + Machinery
              ↓
          Electronics
              ↓
       Technology Systems
              ↓
Automation / Advanced Industry
```

These spines intersect but do not require every cargo to feed every industry.

---

# 10. Productive Round Trips

A major design objective is to create routes where outbound and return cargoes both make economic sense.

## Mine

```text
OUT
Personnel + Tools & Hardware
          ↓
        Mine
          ↓
RETURN
Coal + Returning Personnel
```

## Farm

```text
OUT
Personnel + Agricultural Supplies
          ↓
         Farm
          ↓
RETURN
Grain / Livestock + Returning Personnel
```

## Factory

```text
OUT
Personnel + Industrial Equipment
          ↓
       Factory
          ↓
RETURN
Manufactured Goods + Returning Personnel
```

## Offshore Platform

```text
OUT
Personnel + Industrial Equipment + Construction Materials
                         ↓
                  Offshore Platform
                         ↓
RETURN
Oil / Gas + Returning Personnel
```

Not every route must be balanced. Empty returns remain legitimate.

---

# 11. Historical Economy: 1700–1850

## Core network

```text
Farms / Forests / Fisheries / Mines
              ↓
        Local Processing
              ↓
        Towns / Ports
```

Major cargoes:

- Grain
- Livestock
- Timber
- Fish
- Coal
- Iron Ore
- Stone
- Clay
- Food
- Lumber
- Steel
- Tools & Hardware
- Construction Materials
- Personnel

Technology characteristics:

- manual labor
- animal power
- sailing
- canals
- early steam
- early rail

Personnel demand is generally high.

---

# 12. Historical Economy: 1851–1900

The industrial web expands.

New emphasis:

- Steel
- Machinery
- Coal
- Petroleum
- Chemicals
- industrial ports
- rail corridors
- steamships

Representative chain:

```text
Coal + Iron Ore
       ↓
     Steel
       ↓
   Machinery
       ↓
Industrial Expansion
```

Personnel remains important, while mechanization begins reducing labor intensity in selected industries.

---

# 13. Historical Economy: 1901–1950

The economy enters mass production.

Major developments:

- petroleum refining
- chemicals
- motor transport
- modern factories
- electrical systems
- aviation
- large ports
- offshore petroleum

Representative web:

```text
Oil → Refinery → Chemicals
                    ↓
Steel → Machinery → Factory → Manufactured Goods
                    ↑
                Personnel
```

---

# 14. Historical Economy: 1951–1970

The economy becomes highly industrialized and increasingly global.

Key systems:

- containerization
- deepwater ports
- diesel transport
- large offshore platforms
- modern logistics
- mass consumer manufacturing

The port becomes a major economic organism rather than simply a place where ships stop.

---

# 15. Historical Economy: 1971–2000

Global logistics becomes a central economic feature.

Representative network:

```text
Resource Region
      ↓
Global Transport
      ↓
Specialized Processing
      ↓
Manufacturing Hub
      ↓
Container Port
      ↓
Global Market
```

Electronics begin to become a major product category.

Technology Systems emerge as an increasingly important operational input.

---

# 16. Convergence Economy: 2001–2030

Major transitions:

- digital logistics
- renewable energy
- precision agriculture
- automated warehouses
- advanced manufacturing
- offshore wind
- batteries
- increasingly autonomous transport

Representative agriculture progression:

```text
Traditional / Modern Farm
        ↓
Precision Farm
        ↓
Lower Personnel demand
        ↓
Higher Technology Systems dependence
```

---

# 17. Convergence Economy: 2031–2050

Major systems may include:

- electric transport
- autonomous logistics
- advanced batteries
- offshore wind
- hydrogen systems
- highly automated factories
- remote industrial operations

Potential chain:

```text
Industrial Equipment + Technology Systems
                 ↓
          Offshore Wind Farm
                 ↓
             Electricity
                 ↓
       Hydrogen / Industry
```

Electricity may be introduced as an optional dedicated cargo/system module rather than automatically becoming a core cargo.

---

# 18. Convergence Economy: 2051–2100

The economy becomes increasingly autonomous.

Representative industries:

- automated mines
- autonomous farms
- robotic factories
- smart ports
- offshore energy complexes
- advanced research facilities

Personnel remains relevant for:

- oversight
- maintenance
- engineering
- research
- exceptional operations
- remote-site work

---

# 19. Convergence Economy: 2101–2150

This is the most speculative reference period.

Possible systems:

- highly autonomous industrial networks
- advanced energy systems
- integrated offshore complexes
- advanced materials
- large-scale space infrastructure
- autonomous logistics

These should remain modular.

The historical core should remain fully playable without them.

---

# 20. Industry Succession Families

The reference economy uses succession families rather than isolated date-gated replacements.

## Agriculture

```text
Traditional Farm
 → Mechanized Farm
 → Precision Farm
 → Automated Farm
```

## Forestry

```text
Traditional Forestry
 → Industrial Forestry
 → Mechanized Forestry
 → Precision Forestry
```

## Mining

```text
Traditional Mine
 → Industrial Mine
 → Mechanized Mine
 → Automated Mine
```

## Manufacturing

```text
Workshop
 → Factory
 → Mass-Production Factory
 → Automated Factory
 → Advanced Manufacturing
```

## Port

```text
Trading Wharf
 → Commercial Harbor
 → Steam Harbor
 → Industrial Port
 → Deepwater Port
 → Container Port
 → Smart / Mega Port
```

## Offshore

```text
Coastal Fishing
 → Offshore Petroleum
 → Large Offshore Complex
 → Offshore Wind
 → Floating Wind
 → Integrated Offshore Energy
```

---

# 21. Industry Availability Windows

Approximate reference windows:

| Industry family | First appearance | Mature period | Successor / later state |
|---|---:|---:|---|
| Traditional Farm | 1700 | 1700–1850 | Mechanized Farm |
| Mechanized Farm | 1800+ | 1850–1950 | Precision Farm |
| Precision Farm | 1950+ | 2000+ | Automated Farm |
| Traditional Mine | 1700 | 1700–1850 | Industrial Mine |
| Industrial Mine | 1800+ | 1850–1950 | Mechanized Mine |
| Mechanized Mine | 1900+ | 1950–2000 | Automated Mine |
| Automated Mine | 2000+ | 2030+ | Advanced/Autonomous |
| Workshop | 1700 | 1700–1850 | Factory |
| Factory | 1800+ | 1850–1950 | Mass Production |
| Mass-Production Factory | 1900+ | 1950–2000 | Automated Factory |
| Automated Factory | 1970+ | 2000+ | Advanced Manufacturing |
| Trading Wharf | 1700 | 1700–1800 | Commercial Harbor |
| Commercial Harbor | 1750+ | 1800s | Industrial Port |
| Industrial Port | 1850+ | 1900s | Deepwater Port |
| Deepwater Port | 1950+ | 1950–1970 | Container Port |
| Container Port | 1970+ | 1980+ | Smart / Mega Port |
| Offshore Petroleum | 1900+ | 1950–2000 | Advanced Offshore |
| Offshore Wind | 2000+ | 2010+ | Floating Wind |
| Floating Wind | 2030+ | 2050+ | Integrated Energy |

Dates are gameplay design windows and should be tuned during implementation and testing.

---

# 22. Port Economy

Ports connect local, regional, and global economies.

## General progression

```text
Trading Wharf
    ↓
Commercial Harbor
    ↓
Industrial Port
    ↓
Deepwater Port
    ↓
Container Port
    ↓
Smart / Mega Port
```

## Specialized ports

- Fishing Harbor
- Industrial Port
- Oil Port
- Shipbuilding Port
- Offshore Supply Base
- Container Port

A specialized port should create a meaningful network role.

---

# 23. Offshore Economy

Offshore operations create high-value remote logistics.

## Petroleum

```text
Engineering Works
       ↓
Industrial Equipment
       ↓
Supply Port
       ↓
Offshore Transport
       ↓
Offshore Platform
       ↓
Oil / Gas
       ↓
Refinery
```

## Offshore Wind

```text
Component / Equipment Factory
          ↓
Offshore Equipment
          ↓
Construction Port
          ↓
Heavy-Lift Vessel
          ↓
Offshore Wind Farm
          ↓
Electricity
```

Electricity may remain an optional energy module until implementation testing establishes whether a dedicated energy cargo improves gameplay.

---

# 24. Finance Module

Finance is optional but can provide a distinctive high-value logistics layer.

Potential progression:

```text
1700 → Gold / Coins
1850 → Gold / Coins / Banknotes / Documents
1950 → Cash / Securities / Documents
2000 → Secure high-value logistics
2050+ → Digital finance + physical high-value assets
```

Systemic money remains systemic.

Physical financial cargo represents the logistics of moving valuable physical assets, not the creation of money.

---

# 25. Mail

Mail is a supporting economic flow across the timeline.

Mail should primarily represent:

- communications
- documents
- commercial correspondence
- administrative information
- later high-value information logistics

Mail is distinct from Personnel and Passengers.

---

# 26. Passenger Economy

Passengers represent ordinary human travel.

The passenger economy is connected to industrial growth but is not the same as the Personnel economy.

Industrialization can increase passenger demand through:

- urbanization
- commuting
- commerce
- education
- tourism
- migration

Personnel represents labor assigned to productive worksites.

This distinction allows one city to simultaneously be:

```text
Passenger Source
Personnel Source
Mail Source
Industrial Market
```

---

# 27. Economic Geography

The reference economy should generate geographic specialization.

Examples:

```text
Agricultural Region
      ↓
Grain / Livestock
      ↓
Food Processing Hub
      ↓
Cities
```

```text
Mining Region
      ↓
Ore / Coal
      ↓
Steel / Machinery Hub
      ↓
Manufacturing Region
```

```text
Coastal City
      ↓
Personnel + Equipment
      ↓
Offshore Industry
      ↓
Oil / Gas / Energy
      ↓
Port
```

Geography is therefore part of the economy rather than decoration.

---

# 28. Network Complexity Targets

The reference economy should be **moderately interconnected**.

Target characteristics:

- most primary resources have at least one meaningful processing destination
- important products feed multiple economic sectors
- operational inputs create return and support traffic
- Personnel connects population centers to worksites
- ports connect regional and global networks
- some industries support multiple industries
- no single cargo should become a universal prerequisite

The target is:

```text
Deep enough to reward planning
Simple enough to understand
```

---

# 29. Dependency Limits

Avoid chains where every industry requires many unrelated inputs.

Preferred:

```text
Mine
├── Personnel
├── Tools & Hardware
└── Industrial Equipment
      ↓
    Ore
```

Avoid:

```text
Mine
├── Personnel
├── Food
├── Mail
├── Chemicals
├── Electronics
├── Construction Materials
├── Machinery
├── Fuel
├── Financial Documents
└── five other mandatory cargos
```

The latter produces cargo soup and obscures the economic purpose of the industry.

---

# 30. Supply Service Philosophy

Operational supplies should generally behave as productivity services.

Conceptually:

```text
No supply      → Base production
Regular supply → Enhanced production
Excellent      → Maximum intended productivity
```

This should usually apply to:

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems

Not every industry accepts every supply.

---

# 31. Personnel Service Philosophy

Personnel is similar to an operational service but remains economically distinct because it represents labor.

Conceptually:

```text
No Personnel       → constrained operation
Partial Personnel  → reduced capacity
Regular Personnel  → normal capacity
Excellent Staffing → intended maximum
```

Automation changes the amount of Personnel needed for a given capacity.

---

# 32. Technology Progression Matrix

| Period | Labor | Machinery | Technology Systems | Logistics |
|---|---|---|---|---|
| 1700–1850 | High | Low/medium | Minimal | Local/regional |
| 1851–1900 | High/medium | Rising | Low | National/regional |
| 1901–1950 | Medium | High | Emerging | National/global |
| 1951–1970 | Medium | High | Rising | Global |
| 1971–2000 | Medium/low | High | High | Global/containerized |
| 2001–2030 | Lower | High | Very high | Digital/global |
| 2031–2050 | Low | High | Very high | Increasingly autonomous |
| 2051–2100 | Low | Very high | Dominant | Autonomous |
| 2101–2150 | Very low routine labor | Very high | Dominant | Highly autonomous |

This is a directional model, not a numerical balance table.

---

# 33. What Changes Through Time

The reference economy should change through five primary dimensions:

### 1. Industry availability

New industry types and successors appear.

### 2. Production technology

Existing economic activities become more productive or differently structured.

### 3. Personnel demand

Automation reduces routine labor requirements.

### 4. Operational inputs

Industries increasingly depend on equipment and technology systems.

### 5. Transportation niches

Vehicles evolve to serve different combinations of capacity, speed, geography, cost, and cargo.

These five dimensions should do most of the historical work.

---

# 34. What Does Not Automatically Change

The following should remain stable unless a gameplay reason exists to change them:

- core cargo identity
- economic role of cargo
- basic distinction between Passenger and Personnel
- distinction between products and operational inputs
- industry economic identity
- existence of systemic money
- framework modularity

Stability prevents historical evolution from becoming semantic chaos.

---

# 35. Core vs Optional Economy

## Core

The first implementation should prioritize:

- Agriculture
- Forestry
- Fisheries
- Coal
- Iron
- Stone / Clay
- Oil / Gas
- Steel
- Food
- Lumber
- Machinery
- Chemicals
- Manufactured Goods
- Personnel
- Passengers
- Mail
- Operational supplies
- Ports

## Optional

Later modules may add:

- Copper/electronics depth
- Energy grid
- Recycling
- Finance
- Advanced Technology
- Offshore Wind
- Hydrogen
- Space
- advanced materials

The core economy must remain coherent without optional modules.

---

# 36. Implementation Order

The reference economy should be implemented incrementally.

### Phase 1 — Economic skeleton

Implement:

- core primary resources
- core processing
- basic products
- Passengers
- Personnel
- basic operational supplies

### Phase 2 — Industrial depth

Add:

- Machinery
- Chemicals
- Manufacturing
- expanded ports
- industrial equipment

### Phase 3 — Historical succession

Add:

- industry technology states
- date gates
- overlap
- legacy industries
- automation progression

### Phase 4 — Global logistics

Add:

- containerization
- specialized ports
- advanced maritime logistics
- aviation niches

### Phase 5 — Convergence

Add:

- Electronics
- Technology Systems
- automation
- autonomous transport
- offshore wind

### Phase 6 — Optional future modules

Evaluate:

- energy
- hydrogen
- recycling
- finance
- advanced technology
- space

Each phase should be playable and testable before the next layer is added.

---

# 37. Validation Tests

Before considering the reference economy stable, test:

## Cargo test

- Does every cargo have a clear economic role?
- Is any cargo redundant?
- Are too many cargos required by one industry?

## Industry test

- Does every industry have a reason to exist?
- Does it create meaningful transport decisions?
- Does it fit an industry succession family?

## Personnel test

- Is Personnel genuinely different from Passengers?
- Does it create geographic labor logistics?
- Are return trips useful without being mandatory?

## Era test

- Do new industries appear naturally?
- Do old industries persist appropriately?
- Are date gates understandable?

## Vehicle test

- Does each major vehicle type have a niche?
- Is the newest vehicle always the best?
- Are older vehicles still useful in some circumstances?

## Network test

- Are there productive round trips?
- Are there regional and long-distance opportunities?
- Is the economy moderately interconnected?
- Can a player understand why a route is profitable?

---

# 38. Anti-Patterns

The reference economy should reject:

### Cargo soup

Too many cargos with weak distinctions.

### Dependency soup

Every industry requiring everything.

### Chronological replacement

New technology automatically destroying old technology.

### Profession explosion

Separate cargo for every occupation.

### Vehicle ladder

Newer vehicle = universally better vehicle.

### Technology bonus spam

Every advancement represented as a generic production multiplier.

### Mandatory futurism

Speculative systems becoming required for the core economy.

### Geographic teleportation

Resources, workers, or products appearing at economically impossible locations without transport.

### Pointless round trips

Return cargo added solely to make a vehicle load both ways without an economic reason.

---

# 39. Reference Economy Design Checklist

For each new industry or cargo:

- What economic role does it serve?
- Which module owns it?
- Which era introduces it?
- What predecessor/successor does it have?
- Which stable cargo identities does it use?
- What are its hard production inputs?
- Which operational supplies improve it?
- How much Personnel does it need?
- How does automation change that requirement?
- Where can it geographically exist?
- What transportation modes naturally serve it?
- Can it participate in a productive round trip?
- Does it create a meaningful network decision?
- Does it increase depth without creating cargo soup?
- Can it coexist with older industries?
- Can the player understand it without reading the specification?

---

# 40. Guiding Model

The reference economy can be summarized as:

```text
RESOURCES
   ↓
PROCESSING
   ↓
PRODUCTS
   ↓
MARKETS

        ↕

OPERATIONAL INPUTS
        ↕
INDUSTRIAL CAPACITY
        ↕
PERSONNEL
        ↕
TRANSPORTATION
        ↕
GEOGRAPHY
        ↕
TIME / TECHNOLOGY
```

The economy evolves because these relationships change through time.

The player succeeds by building transportation networks that respond to those changes.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

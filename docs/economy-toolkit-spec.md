# OpenTTD Economy Toolkit / Economy Authoring Specification

## 1. Purpose

This document defines the architecture and authoring model for a reusable **economy-building toolkit for OpenTTD**.

The project is not limited to one historical economy. The historical 1700–2150 economy is the **Reference Economy**: a concrete implementation used to prove that the toolkit's rules produce a playable, understandable, moderately interconnected economy.

The toolkit should allow another developer to create, fork, or replace the reference economy without rewriting the underlying economic framework.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

---

# 2. Architectural Separation

The project has three conceptual layers.

```text
┌──────────────────────────────────────────────┐
│              ECONOMY TOOLKIT                 │
│                                              │
│  Schema • Authoring Rules • Validation       │
│  Dependency Analysis • Adapters              │
└──────────────────────┬───────────────────────┘
                       │
             defines / validates
                       │
┌──────────────────────▼───────────────────────┐
│             ECONOMY DEFINITION               │
│                                              │
│  Cargo • Industries • Recipes • Eras         │
│  Geography • Supplies • Succession           │
│  Modules • Demand • Network Rules            │
└──────────────────────┬───────────────────────┘
                       │
              one implementation
                       │
┌──────────────────────▼───────────────────────┐
│             REFERENCE ECONOMY               │
│                                              │
│  Historical 1700–2150 economy                │
└──────────────────────────────────────────────┘
```

### 2.1 Toolkit

The toolkit defines **how an economy is described and validated**.

It should eventually provide:

- machine-readable schemas;
- authoring conventions;
- dependency-graph validation;
- cargo source/consumer validation;
- recipe validation;
- complexity/depth checks;
- era and succession checks;
- module-isolation checks;
- Personnel validation;
- transport-role validation;
- human-readable validation reports;
- OpenTTD/NewGRF adapter interfaces.

The toolkit does not dictate a single historical economy.

### 2.2 Economy Definition

An economy definition is the data describing a particular economic model.

A definition may contain:

- cargoes;
- industries;
- recipes;
- production rules;
- demand/endpoints;
- operational supplies;
- Personnel rules;
- eras;
- industry succession;
- geography;
- modules;
- recycling rules;
- transport niches.

### 2.3 Reference Economy

The Reference Economy is one complete, historically recognizable implementation.

It is authoritative for the project's current design decisions but is **not the schema itself**.

A fork may retain, modify, extend, or replace it.

---

# 3. Design Principles

## 3.1 Add economic relationships before adding cargoes

A new cargo should exist only when distinguishing it creates a meaningful transportation, production, geographic, historical, or strategic decision.

If two materials behave the same way economically, aggregate them.

> **Add economic relationships, not cargoes.**

## 3.2 Stable cargo identities

Prefer stable cargo identities across technological eras.

Technology should normally change:

- industry type;
- production efficiency;
- labor intensity;
- operational supply requirements;
- transport requirements;
- geographic concentration;

rather than creating unnecessary era-specific cargoes.

## 3.3 Economic activity first

Industries represent meaningful economic activities rather than merely visual buildings.

## 3.4 Optional complexity stays optional

Advanced systems should be modular. A player should be able to operate the historical/core economy without enabling every advanced module.

## 3.5 No cargo soup

Complexity should come from meaningful connections and routing decisions, not from dozens of narrowly differentiated cargoes.

## 3.6 No arbitrary perpetual loops

Circular economies such as recycling are permitted when they represent real recovery flows and have bounded recovery rates. They must not create infinite-resource loops.

---

# 4. Economy Authoring Model

An economy author should be able to define an economy through a small number of explicit objects.

Conceptually:

```text
Economy
├── Cargoes
├── Industries
├── Recipes
├── Production Rules
├── Operational Supplies
├── Personnel Rules
├── Eras
├── Succession Families
├── Geography Rules
├── Modules
├── Demand / Endpoints
└── Transport Roles
```

The final machine-readable format is implementation-dependent. YAML/JSON are preferred candidates because they are human-readable, diffable, and straightforward to validate.

---

# 5. Cargo Authoring

Every cargo should have a stable machine-readable ID.

Conceptual example:

```yaml
cargo:
  id: copper
  name: Copper
  class: product
  introduced: 1850
  tags:
    - metal
    - manufacturing_input
```

### Cargo classes

The framework recognizes these broad classes:

- `primary` — extracted, harvested, caught, mined, or pumped;
- `product` — processed or manufactured outputs;
- `operational_supply` — materials/services physically represented as cargo and consumed to improve operations;
- `human_flow` — Passengers, Personnel, and related human movement;
- `financial` — optional physical high-value financial cargoes;
- `optional` — module-specific cargoes.

A cargo should not be assigned multiple identities merely because its real-world composition varies.

---

# 6. Industry Authoring

Each industry should define at minimum:

- stable ID;
- player-facing name;
- role;
- module;
- availability era;
- geography;
- hard inputs;
- operational supplies;
- outputs;
- Personnel demand;
- predecessor/successor relationships where applicable.

Conceptual example:

```yaml
industry:
  id: copper_works
  name: Copper Works
  role: processing
  module: heavy_industry
  era:
    start: 1850
    end: 2150
  hard_inputs:
    - cargo: copper_ore
      amount: 1
      relationship: required
  outputs:
    - cargo: copper
      amount: 1
```

An industry ID should change when production behavior, construction rules, or technology state materially changes.

A player-facing name may remain similar across successors.

---

# 7. Recipe Semantics

The toolkit must never use ambiguous `and/or` recipe language.

Every relationship must have an explicit semantic type.

Supported relationship concepts:

- **required** — production cannot occur without the input;
- **proportional** — output/input quantity follows a defined ratio;
- **preferred** — input improves or prioritizes a production pathway but is not universally required;
- **alternative** — one of several defined inputs/pathways may satisfy the requirement;
- **optional** — input is accepted but does not define the base production rule;
- **supply** — operational input affecting productivity, capacity, reliability, or efficiency rather than being a hard production ingredient.

A recipe may contain multiple explicit relationships.

Example:

```text
Grain OR Livestock OR Fish
        ↓
  Food Processing
```

must be encoded as explicit alternatives, not as the literal phrase `Grain and/or Livestock and/or Fish`.

---

# 8. Operational Supply Model

Operational supplies are normally **productivity modifiers**, not universal hard prerequisites.

Default service model:

```text
None       → base production
Regular    → production bonus
Excellent  → maximum intended productivity
```

The provisional reference targets remain approximately:

- None: 100%;
- Regular: 115–125%;
- Excellent: 135–150%.

These are balance targets, not immutable engine constants.

### Core operational supplies

The framework may use:

- Tools & Hardware;
- Industrial Equipment;
- Construction Materials;
- Agricultural Supplies;
- Fuel;
- Chemicals;
- Technology Systems.

### Fuel

Fuel represents aggregated transportation and energy-use products rather than requiring separate cargoes for gasoline, diesel, marine fuel, aviation fuel, etc.

Fuel can support:

- road depots and fleets;
- rail operations;
- aircraft/airports;
- ships and harbors;
- fishing operations;
- industrial equipment;
- logistics hubs;
- ports and terminals.

A Fuel Depot/Fuel Terminal is primarily a **storage and distribution node**, not a second refinery.

Core petroleum relationship:

```text
Oil
 ↓
Refinery
 ↓
Petroleum Products
 ├──→ Fuel distribution
 └──→ Chemical feedstock / Chemical Works
```

Whether Fuel is enabled in a specific economy is a module/configuration decision, but the toolkit must support it as a first-class operational supply.

### Chemicals

Chemicals represent aggregated industrial/process chemicals rather than separate cargoes for grease, lubricants, solvents, coolants, reagents, and similar materials.

Depending on era and technology, Chemicals may imply:

- lubricants and greases;
- solvents;
- coolants;
- industrial reagents;
- process chemicals;
- specialty chemical inputs.

Chemicals can function as operational supplies for industries and infrastructure as technology advances.

Chemical Works therefore has two economically meaningful roles:

1. producing Chemicals as an industrial product;
2. supplying Chemicals as an operational input throughout the economy.

### Agricultural Supplies

Agricultural Supplies aggregate inputs such as:

- fertilizer;
- animal feed;
- soil amendments;
- crop treatments;
- agricultural chemicals;
- related agricultural consumables.

The same stable cargo identity may represent different real-world mixes across eras.

Agricultural Supplies may be produced from multiple pathways, including Chemical Works and other approved byproduct/recovery pathways.

Byproducts should only become explicit cargo flows when they create meaningful gameplay value.

---

# 9. Recycling and Secondary Materials

Recycling is a supported economic module and may be part of a reference economy or enabled as an optional module.

The preferred abstraction is broad rather than material-by-material.

Conceptual flow:

```text
Towns / Industry
      ↓
Scrap / Recyclables
      ↓
Recycling Center
      ↓
Recovered Materials
      ↓
Processing / Manufacturing
      ↓
Products
```

The framework should avoid immediately creating separate cargoes for:

- steel scrap;
- aluminum scrap;
- plastic waste;
- glass waste;
- paper waste;
- electronic waste;
- etc.

Those distinctions may be introduced only when they produce a meaningful gameplay distinction.

### Recycling constraints

A recycling module must define:

- source of recoverable material;
- recovery rate or bounded conversion;
- destination/use of recovered material;
- losses or unrecoverable material where appropriate;
- technology improvements over time.

A recycling loop must never permit unlimited multiplication of resources.

---

# 10. Agricultural Byproducts and Cross-Industry Inputs

The toolkit permits secondary pathways where economically or historically justified.

Examples may include:

```text
Chemical Works → Agricultural Supplies
```

or a future configured byproduct pathway such as:

```text
Industry A → useful byproduct → Industry B
```

The existence of a real-world byproduct is **not sufficient reason to create a new cargo**.

The author must demonstrate that the pathway adds meaningful logistics or strategic choice.

---

# 11. Personnel Authoring

Personnel is distinct from Passengers.

Personnel represents people transported because a productive site requires labor.

Conceptual model:

```text
Town / Personnel Source
        ↓
     Personnel
        ↓
      Worksite
        ↓
 Returning Personnel
```

Personnel demand should be configurable by:

- industry;
- scale;
- technology state;
- labor intensity;
- era.

Personnel can be returnable where appropriate.

`Returning Personnel` may remain an implementation state rather than a separate cargo identity.

The toolkit must validate the economic rule while leaving the exact NewGRF representation to the adapter layer.

---

# 12. Era Authoring

Economy authors define eras independently of vehicle rosters.

Each era may control:

- industry construction availability;
- production behavior;
- supply importance;
- Personnel intensity;
- transport niches;
- technology states;
- optional module availability.

An industry can remain in operation after its new-construction window closes.

> **No new construction does not mean existing industry disappears.**

Reference eras:

```text
Transformation   1700–1850
Acceleration     1851–2000
Convergence      2001–2150
```

Custom economies may define different eras.

---

# 13. Industry Succession

Succession allows historical or technological replacement without forcing immediate deletion of predecessors.

Conceptual model:

```text
Traditional Farm
       ↓
Mechanized Farm
       ↓
Precision Farm
       ↓
Automated Farm
```

Succession should preserve cargo identities wherever possible.

Each succession relationship may define:

- predecessor;
- successor;
- transition date/range;
- production changes;
- labor changes;
- supply changes;
- geography changes;
- construction rules.

---

# 14. Geography Authoring

Economies should be able to define geographic constraints without hard-coding them into cargo definitions.

Examples:

```text
Farm → fertile regions
Forest → forest regions
Fishery → coastal/offshore waters
Coal Mine → coal-bearing geology
Oil Field → petroleum geology
Port → navigable coast/river
```

Processing may favor:

- resource proximity;
- rail corridors;
- ports;
- cities;
- industrial clusters;
- labor pools.

Geography is a gameplay rule, not merely a visual placement rule.

---

# 15. Modules

A module is a coherent economic extension that can be enabled or disabled.

Candidate modules include:

- Agriculture;
- Forestry;
- Heavy Industry;
- Maritime;
- Offshore;
- Energy;
- Chemicals;
- Global Logistics;
- Recycling;
- Finance;
- Advanced Technology;
- Research;
- Space.

Modules must declare their dependencies.

A module should not silently create mandatory dependencies in another module.

For example, an optional Energy module may introduce electricity, hydrogen, or alternative fuel pathways without making them mandatory to complete the historical core economy.

---

# 16. Dependency and Complexity Rules

The toolkit should automatically validate the economy graph.

### 16.1 Cargo coverage

Every core cargo should have:

- at least one valid source;
- at least one valid consumer;

unless it is explicitly classified as:

- an endpoint;
- a human flow;
- a financial flow;
- an optional/module-specific cargo.

### 16.2 Dependency depth

Core chains should normally remain understandable by inspection.

Default reference constraint:

> No core production chain should require six or more mandatory intermediate cargo transformations merely to function.

Advanced industries may exceed normal input counts only when the added logistics has clear gameplay value.

### 16.3 Hard-input count

Most industries should have **0–4 meaningful hard inputs**.

Advanced industries may reach five when justified.

Operational supplies do not count as hard inputs unless a module explicitly changes that rule.

### 16.4 Cycle detection

Production and operational-supply graphs must be analyzed separately.

Legitimate recycling loops are permitted only when their conversion/recovery is bounded and explicitly classified as a circular economy module.

Operational supply dependencies must not form unbounded prerequisite cycles.

---

# 17. Transport Role Authoring

The economy toolkit does not hard-code one vehicle roster.

Instead, an economy may declare transportation roles such as:

- local bulk;
- long-distance bulk;
- regional passenger;
- long-distance passenger;
- personnel shuttle;
- coastal feeder;
- ocean freight;
- container logistics;
- high-value/time-sensitive freight;
- remote logistics;
- offshore supply;
- heavy lift;
- aviation;
- autonomous logistics.

Vehicles should then be selected to serve economic roles.

> **Vehicles serve the economy.**

A vehicle should have a meaningful niche rather than being merely a faster replacement for every predecessor.

---

# 18. Demand and Endpoints

An economy author must explicitly identify where outputs are consumed.

Typical endpoints include:

- towns;
- construction markets;
- industrial markets;
- transportation infrastructure;
- ports;
- export/import hubs;
- financial/service centers;
- optional advanced systems.

Not every cargo needs to be consumed by another production industry.

Human and financial flows may have different endpoint semantics.

---

# 19. Authoring Workflow

A new economy should be authored in this order:

```text
1. Define economic goals
        ↓
2. Define modules
        ↓
3. Define cargo vocabulary
        ↓
4. Define endpoints / demand
        ↓
5. Define industries
        ↓
6. Define explicit recipes
        ↓
7. Define operational supplies
        ↓
8. Define Personnel rules
        ↓
9. Define eras and succession
        ↓
10. Define geography
        ↓
11. Define transport roles
        ↓
12. Run validation
        ↓
13. Build a vertical slice
        ↓
14. Playtest
        ↓
15. Balance
```

Do not begin by designing vehicles and then inventing an economy around them.

---

# 20. Validation Contract

Every authored economy should be machine-checkable before NewGRF implementation.

Minimum validation categories:

1. Cargo source coverage
2. Cargo consumer coverage
3. Recipe validity
4. Recipe semantic completeness
5. Undefined cargo detection
6. Dependency graph validity
7. Operational-supply acyclicity
8. Dependency-depth limit
9. Hard-input count
10. Personnel validity
11. Era gating
12. Succession continuity
13. Geography coverage
14. Module dependency isolation
15. Recycling-loop bounds
16. Transport-role coverage
17. Town/end-point demand coverage

A validation failure should identify the exact object and rule that failed.

Example:

```text
FAIL VAL-CARGO-001
Cargo: copper
Problem: no consumer found in enabled modules
Suggested action: add a consumer or classify cargo as optional/endpoint.
```

---

# 21. Reference Economy as a Conformance Test

The historical 1700–2150 economy should eventually pass the toolkit validation suite.

This makes the Reference Economy more than content: it becomes a **conformance test** for the toolkit itself.

If a toolkit rule cannot represent the Reference Economy without special-case hacks, either:

1. the toolkit abstraction is wrong;
2. the reference economy is violating an intentional rule; or
3. a documented adapter exception is required.

Special cases should be minimized and documented.

---

# 22. Fork / Custom Economy Contract

A developer creating a custom economy should be able to:

- copy the economy definition;
- replace cargo definitions;
- add/remove industries;
- define different eras;
- change recipes;
- enable/disable modules;
- define different geographic rules;
- run the same validation suite;
- produce an OpenTTD/NewGRF implementation through the same adapter model.

The developer should **not** need to modify the core validation architecture merely because the economy is historically, geographically, or thematically different.

Example custom economies could include:

```text
Historical North America
Historical Europe
Fantasy economy
Post-apocalyptic economy
Futuristic automated economy
Regional industrial economy
Minimal/simple economy
High-complexity experimental economy
```

These are examples, not prescribed future projects.

---

# 23. Compatibility and Versioning

The toolkit and an economy definition should be versioned independently.

A toolkit release may change:

- schema capabilities;
- validation rules;
- adapter APIs;
- supported recipe semantics.

An economy release may change:

- cargoes;
- industries;
- recipes;
- balance;
- eras;
- modules.

Breaking changes must be identifiable.

Stable IDs should not be casually reused for economically different objects.

---

# 24. Minimum Viable Toolkit

The first implementation does **not** need a full graphical economy editor.

The minimum useful toolkit is:

```text
Machine-readable economy definition
        ↓
Schema validation
        ↓
Dependency graph
        ↓
Economic validation report
        ↓
Reference vertical slice
```

A GUI/editor can come later.

The first objective is proving that an economy can be authored, validated, and converted into an OpenTTD implementation without hidden contradictions.

---

# 25. Minimum Vertical Slice

The first conformance slice should demonstrate:

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
```

plus:

```text
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
```

and Personnel:

```text
Town
 ↓
Personnel
 ↓
Worksite
 ↓
Returning Personnel
```

The vertical slice should eventually demonstrate operational supplies, explicit recipes, geography, era gates, succession, and validation.

---

# 26. Definition of Done for Toolkit Architecture

The architecture is considered ready for implementation when:

- the toolkit/reference-economy separation is explicit;
- cargo and industry IDs are stable;
- recipe semantics are machine-readable;
- operational supplies are modeled separately from hard inputs;
- Fuel and Chemicals can function as operational supplies without cargo proliferation;
- Agricultural Supplies can aggregate fertilizer/feed/etc.;
- recycling can be represented as a bounded module;
- Personnel has an adapter boundary;
- modules declare dependencies;
- dependency-depth and cycle checks are defined;
- the Reference Economy can serve as a conformance test;
- a custom/forked economy can use the same validation machinery.

---

# 27. Guiding Rule

> **The toolkit should make it easier to build a good economy, not easier to build a complicated economy.**

The objective is not maximum number of cargoes, industries, or dependencies.

The objective is **meaningful economic relationships that create interesting transportation decisions while remaining understandable to the player and maintainable by the developer.**

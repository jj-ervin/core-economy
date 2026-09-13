# Reference Economy: 1700–2150

## Canonical status

This document is the normalized reference economy for the OpenTTD Economic Framework. It supersedes earlier wording where recipes or cargo identities were ambiguous.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

The economy uses stable cargo identities and historical industry succession. Technology changes production, labor intensity, supplies, and transport niches rather than creating unnecessary era-specific cargoes.

---

# 1. Core Cargo Vocabulary

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
- Copper
- Petroleum Products
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
- Returning Personnel
- Mail

`Returning Personnel` is a flow state/implementation concept, not necessarily a separate cargo identity. The canonical human-flow identity is Personnel unless the NewGRF adapter requires another representation.

## Optional Financial Flows

- Gold
- Bullion
- Coins / Cash
- Securities / Financial Documents

Financial cargo remains optional and does not automatically create money.

---

# 2. Core Production Chains

## Food

```text
Grain ─────┐
Livestock ─┼→ Food Processing → Food → Towns
Fish ──────┘
```

Food Processing uses an **alternative-feedstock** model: a configured plant may accept one or more of Grain, Livestock, and Fish. “And/or” is not a recipe type.

## Forestry / Construction

```text
Timber → Sawmill → Lumber ─────┐
Stone ─────────────────────────┤
Clay ──────────────────────────┼→ Construction Materials
Steel ─────────────────────────┘
```

Clay is a **core** resource. Construction Materials uses Clay as a defined component; exact proportions remain a balancing parameter.

## Steel

```text
Iron Ore + Coal → Steel Mill → Steel
```

Later steel technologies may use an approved alternative energy pathway through an optional Energy module.

## Copper

```text
Copper Ore → Copper Works → Copper
                              ├→ Machinery
                              └→ Electronics
```

Copper is a stable **PRODUCT**. There is no core “processed copper” cargo.

## Petroleum / Chemicals

```text
Oil → Refinery → Petroleum Products → Chemical Works → Chemicals
Gas ────────────────────────────────────────┘
```

The gas branch is allowed only through an explicitly defined gas-feedstock recipe. Raw Oil is not a normal Chemical Works input.

**Refinery and Chemical Works are distinct:**

- Refinery = petroleum processing.
- Chemical Works = chemical manufacturing from defined feedstocks.

Fuel may later be split from Petroleum Products by an optional Energy/Transport module.

## Machinery

```text
Steel + Copper
      ↓
Machinery Works
      ↓
Machinery
```

Chemicals may be an optional/preferred input in the base Machinery recipe and can become required in advanced variants.

## Manufactured Goods

```text
Steel + Lumber
      ↓
Factory
      ↓
Manufactured Goods
```

Machinery, Chemicals, and Electronics are preferred or required in later factory states rather than being universally mandatory from the beginning.

## Electronics

```text
Copper + Chemicals
       ↓
Electronics Factory
       ↓
Electronics
```

Machinery can be a preferred input. Advanced electronics increasingly depend on Technology Systems operational supply.

## Advanced Goods

```text
Electronics + Chemicals + Machinery
                ↓
Advanced Manufacturing
                ↓
Advanced Goods
```

Advanced Goods remain intentionally broad.

---

# 3. Operational Supply Economy

Operational supplies are productivity modifiers rather than universal hard prerequisites.

Typical progression:

```text
Early        → Tools & Hardware
Industrial   → Tools + Industrial Equipment
Modern       → Industrial Equipment + Technology Systems
Automated    → Technology Systems + reduced Personnel
```

Supply service levels remain:

- None → base production
- Regular → production bonus
- Excellent → maximum intended productivity

Provisional targets remain 100%, 115–125%, and 135–150% respectively and require playtesting.

### Supply producers

```text
Lumber / Steel
      ↓
General Works
      ↓
Tools & Hardware
```

```text
Steel + Machinery
      ↓
Industrial Equipment Works
      ↓
Industrial Equipment
```

```text
Stone + Clay + Lumber + Steel
      ↓
Construction Materials Works
      ↓
Construction Materials
```

```text
Chemicals + Machinery
      ↓
Agricultural Supply Works
      ↓
Agricultural Supplies
```

```text
Electronics + Machinery + Chemicals
      ↓
Technology Systems Works
      ↓
Technology Systems
```

The exact proportional recipes remain implementation/balance parameters. Supply-production graphs must remain acyclic.

---

# 4. Personnel Economy

Personnel is a human-flow layer distinct from Passengers.

```text
Town / Personnel Source
        ↓
     Personnel
        ↓
      Worksite
        ↓
 Returning Personnel
```

Personnel demand is tied to industry scale and labor intensity. It generally declines as mechanization and automation increase.

Productive round trips are encouraged:

```text
OUT: Personnel + operational inputs
             ↓
          Worksite
             ↓
RETURN: Product + Personnel
```

Not every worksite must return Personnel and not every transport route needs a return cargo.

---

# 5. Industry Families

## Agriculture

```text
Traditional Farm       1700–1850
        ↓
Mechanized Farm        1800–1950
        ↓
Precision Farm         1980–2045
        ↓
Automated Farm         2035–2150
```

## Forestry

```text
Traditional Forestry   1700–1850
        ↓
Industrial Forestry    1800–1950
        ↓
Mechanized Forestry    1920–2000
        ↓
Precision Forestry     1980–2150
```

## Fisheries

```text
Coastal Fishery        1700–1900
        ↓
Commercial Fishery     1850–1970
        ↓
Advanced Fishery       1970–2150
```

## Coal

```text
Early Coal Mine        1700–1900
        ↓
Mechanized Coal Mine   1850–2000
        ↓
Modern Coal Mine       1950–2150
```

## Copper

```text
Copper Mine             1850–2150
        ↓
Automated Copper Mine  2030–2150
```

```text
Copper Works            1850–2150
        ↓
Automated Copper Works 1980–2150
```

## Petroleum

```text
Onshore Oil Field      1850–2150
Offshore Oil Platform  1930–2100
Advanced Offshore      2000–2150
```

## Processing

```text
Food Processing
Sawmill
Steel Mill
Refinery
Chemical Works
Copper Works
```

Each has technology successors where production behavior materially changes.

---

# 6. Historical Progression

## 1700–1850 — Transformation

Core systems:

- agriculture
- forestry
- fisheries
- coal and iron
- stone and clay
- local food processing
- sawmills
- early steel
- sailing and canals
- early steam
- high Personnel intensity

The network should favor regional and short-to-medium distance bulk movements.

## 1851–2000 — Acceleration

Major additions:

- mechanized extraction
- steel and machinery at scale
- copper processing
- petroleum refining
- chemical manufacturing
- mass factories
- steamships and rail
- modern ports
- offshore petroleum
- containerization
- electronics

## 2001–2150 — Convergence

Major additions:

- precision and automated agriculture
- automated extraction
- advanced copper processing
- smart ports
- autonomous logistics
- offshore wind
- advanced manufacturing
- research
- optional hydrogen/electricity systems
- optional space systems

Future systems remain modular and cannot be required to complete the historical core economy.

---

# 7. Ports and Maritime Economy

Port succession:

```text
Trading Wharf
 → Commercial Harbor
 → Steam Harbor
 → Industrial Port
 → Deepwater Port
 → Container Port
 → Smart / Mega Port
```

Specialized ports may include Fishing Harbor, Oil Port, Shipbuilding Port, and Offshore Supply Base.

Ports create meaningful consolidation and transfer choices rather than simply being cosmetic station variants.

---

# 8. Offshore Economy

Petroleum:

```text
Engineering / Construction Inputs
          ↓
Supply Port / Offshore Base
          ↓
Offshore Platform
          ↓
Oil / Gas
```

Offshore wind:

```text
Industrial Equipment + Construction Materials
                  ↓
          Offshore Wind Farm
                  ↓
       Electricity* / Energy Service
```

`*` Electricity is optional.

Offshore facilities deliberately create personnel, equipment, construction, and return-cargo opportunities.

---

# 9. Geography

Primary resources are strongly geography-dependent:

- farms → fertile land
- forests → forest regions
- fish → coast/water
- coal → coal geology
- iron → iron-bearing geology
- copper → copper-bearing geology
- stone → quarry geology
- clay → clay-bearing regions
- oil/gas → petroleum geology/offshore fields

Processing tends toward resource proximity, transport corridors, ports, cities, and industrial clusters.

Advanced industry increasingly clusters around cities, skilled labor, logistics hubs, and research centers.

---

# 10. Network Complexity Rules

The reference economy should be moderately interconnected without becoming cargo soup.

Rules:

- Core chains should normally remain understandable by inspection.
- No core chain should require six or more mandatory intermediate cargo transformations merely to function.
- Most industries should have 0–4 meaningful hard inputs.
- Advanced industries may reach five only when the added logistics has clear gameplay value.
- Operational supplies are not counted as hard inputs unless a module explicitly changes that rule.
- Every core cargo must have a defined source and consumer, except explicit endpoints/human flows/optional cargoes.
- No undefined cargo names such as “processed copper” may appear in canonical recipes.
- Recipe relationships must use explicit semantics: required, proportional, preferred, alternative, optional.
- Supply-production dependency graphs must be acyclic.

---

# 11. Core Round-Trip Examples

## Mine

```text
Personnel + Tools & Hardware
          ↓
        Mine
          ↓
Coal / Iron Ore / Copper Ore + Personnel
```

## Farm

```text
Personnel + Agricultural Supplies
          ↓
         Farm
          ↓
Grain / Livestock + Personnel
```

## Copper

```text
Copper Ore + Personnel + Industrial Equipment service
                    ↓
              Copper Works
                    ↓
            Copper + Personnel
```

## Offshore

```text
Personnel + Industrial Equipment + Construction Materials
                         ↓
                  Offshore Platform
                         ↓
              Oil / Gas + Personnel
```

---

# 12. Optional Modules

The following may extend the reference economy without becoming mandatory:

- Energy
- Detailed construction / ceramics
- Global logistics refinements
- Recycling
- Finance
- Research / advanced technology
- Space

Modules should add meaningful routing or economic choices, not merely rename existing cargoes.

---

# 13. Canonical Decisions from Validation

| Finding | Canonical decision |
|---|---|
| Clay orphan | Keep Clay core; consume it through Construction Materials |
| Copper processing ambiguity | Add Copper Works; Copper is the stable product |
| Refinery/Chemical overlap | Refinery produces Petroleum Products; Chemical Works produces Chemicals |
| “and/or” recipes | Replace with explicit recipe semantics |
| Supply cycles | Must be validated as a directed acyclic dependency graph |
| Personnel implementation | Economic rule is canonical; OpenTTD/NewGRF representation remains an adapter concern |

---

# 14. Implementation Gate

Do not begin full NewGRF implementation until:

1. the cargo/industry dependency matrix exists;
2. every core cargo has a valid source and consumer;
3. all recipes use explicit relationship types;
4. supply-production cycles are ruled out;
5. dependency depth passes the complexity limit;
6. Personnel representation has a technical adapter design;
7. era gates and succession rules are testable;
8. the prototype slice passes the economic validation suite.

The economy is ready for implementation only when these tests pass—not merely because the prose looks coherent.

---

# 15. Guiding Principle

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

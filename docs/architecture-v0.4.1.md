# Core Economy v0.4.1 Architecture

## Purpose

This document establishes the architecture boundary for Core Economy after the v0.4.0 Historical Steelmaking Vertical Slice.

Core Economy is a historical transport economy for OpenTTD spanning **1700–2299**. The design is organized as four independently playable 150-year economic eras that can also be played as one continuous 600-year campaign.

The central design principle is:

> **Industries persist by default. Eras change their technology, recipes, productivity, inputs, outputs, scale, and economic importance. True phase-out is reserved for industries or technologies that become historically obsolete.**

## 1. Era Model

| Era | Years | Purpose |
|---|---:|---|
| `era_1` | 1700–1849 | Pre-industrial to early industrial economy |
| `era_2` | 1850–1999 | Industrialization, mass production, modern infrastructure |
| `era_3` | 2000–2149 | Advanced/global economy and technological transition |
| `era_4` | 2150–2299 | Future/advanced economy |

The year ranges are inclusive. The boundary years are therefore 1850, 2000, and 2150.

### Independent era play

Each era is a **mini-economy slice**. Starting a game in an era must provide a coherent, playable economy without requiring the player to have played an earlier era.

An era profile therefore defines the economic state that exists at its start. It is not merely a list of industries that happen to unlock during that period.

### Full campaign

A full campaign runs continuously from 1700 through 2299. Era transitions modify the existing economy rather than deleting and recreating the entire industry graph.

## 2. Industry Lifecycle

Every canonical industry belongs to one lifecycle class:

- `persistent` — expected to exist across most or all eras.
- `transforming` — the sector persists, but its technology/recipe/profile changes materially.
- `emerging` — introduced during a later era and becomes part of the continuing economy.
- `declining` — remains available but loses economic importance over time.
- `phase_out` — historically obsolete and eventually unavailable for normal new construction; existing installations may persist temporarily.

`successor` is a relationship between implementations or technology generations. It must **not** be interpreted as automatic destruction of the predecessor.

Examples:

- Agriculture: persistent/transforming.
- Forestry: persistent/transforming.
- Construction: persistent/transforming.
- Food production: persistent/transforming.
- Steel: persistent/transforming.
- Coal: persistent in early/industrial eras, then declining/possible phase-out depending on its role.
- Coke: transforming/declining and eventually phase-out as steelmaking technology changes.
- Steam locomotive production: phase-out candidate.

## 3. Sector Model

Economic sectors are persistent concepts. Individual industry implementations may change within a sector.

Initial sector families include:

- agriculture
- forestry
- fisheries
- mining
- construction
- materials
- energy
- chemicals
- food
- manufacturing
- technology
- logistics/ports
- financial/services

The sector is the stable economic identity; an industry implementation is the concrete production facility used by an era.

## 4. Construction Economy

Construction is a persistent economic pillar across the full game.

The construction economy evolves rather than disappears. Candidate material families include:

- timber/lumber
- stone
- aggregates
- lime/cement
- brick/ceramics
- glass
- steel
- advanced/engineered materials

**Cement is explicitly part of the planned construction economy.** Its exact industry, cargo identity, recipes, and era behavior will be reconciled during the canonical-data pass rather than added as an isolated cargo.

## 5. Geography and Transport

Core Economy should model economic geography as a gameplay constraint, especially in earlier eras.

The intended relationship is:

```text
resource location
      ↓
extraction
      ↓
transport network
      ↓
processing
      ↓
population / industrial demand
```

Distance, transport speed, capacity, and infrastructure should affect the practical viability of these relationships. Early eras should naturally favor shorter regional supply chains because transport is slower and lower-capacity. Later eras should support longer-distance specialization and larger markets.

This is a **design requirement**, not yet a claim that NewGRF alone implements dynamic distance economics.

## 6. Settlement Model

Vanilla OpenTTD town generation remains available.

Core Economy may later add a dynamic settlement layer supporting company-founded settlements near economically useful locations, including resource and industrial clusters.

Planned lifecycle:

```text
existing vanilla town

company-founded settlement
        ↓
settlement growth
        ↓
town
        ↓
city / major population center
```

The company should receive founder/developer benefits rather than permanent ownership of a mature town. The exact transition rules remain a Dynamics/GameScript design item.

Settlement simulation, population growth, founding, and economic geography are therefore **not part of the current NewGRF-only implementation contract**.

## 7. Runtime Boundaries

### NewGRF — Core Economy static economic layer

Owns the parts of the economy that NewGRF can reliably express:

- industry definitions
- cargo identities
- production chains
- production callbacks
- graphics
- historical availability gates
- static operating requirements
- NewGRF parameters where appropriate

### GameScript — Core Economy Dynamics

A future optional runtime layer may own:

- settlement creation and growth
- population/economic state
- dynamic events
- contracts and policy logic
- bounded resource discovery/depletion if technically appropriate
- player/company settlement interactions
- higher-level economic state that cannot be represented reliably by NewGRF

### Sidecar / Admin Port — deferred

An external sidecar is **not required for the core game economy**. It may later support server administration, telemetry, analytics, or external economic-history tooling where OpenTTD's supported interfaces make that practical.

It is explicitly deferred from the v0.4.1/v0.5 implementation path.

## 8. Vanilla Industry Strategy

The current v0.4.0 GRF uses vanilla industry `substitute`/`override` behavior for its four-industry prototype. This is retained only as a known prototype constraint.

For the next architecture phase:

1. Do not add additional vanilla overrides casually.
2. New Core Economy industries should prefer dedicated custom industry IDs once the custom-ID prototype is validated.
3. Compatibility with other industry GRFs must be tested before declaring the architecture stable.
4. The canonical economy model must distinguish design classification (`core`, `adopt`, `modify`, `suppress`, `defer`) from the actual NML implementation mechanism.

## 9. Canonical Data vs Implementation

The canonical economy describes the intended economic universe. The shipped NewGRF is a subset of that universe until an industry is actually implemented and tested.

The project must maintain an explicit implementation manifest so that:

- documented industries are not mistaken for shipped industries;
- planned industries can remain in the design without pretending to be implemented;
- NML coverage can be audited against the canonical model;
- era playability can be tested independently.

A checked-off design item is not considered implemented until it has executable code and a passing validation/build/playtest path.

## 10. Scope Rules

Before expanding the industry graph, the project should prove one complete playable era slice.

The next implementation target is **Era 1 (1700–1849)** with a coherent mini-economy including agriculture/food, forestry/materials, construction, the existing coal/coke/iron/steel slice where appropriate, personnel/operational supplies, and town-facing demand.

Later eras should reuse persistent economic sectors and transform their implementations rather than creating four disconnected economies.

Dynamic settlements, dynamic pricing, world-state simulation, causal event records, AI policy loops, and sidecar analytics remain future work until the static economy architecture is proven.

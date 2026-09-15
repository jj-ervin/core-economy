# Core Economy Industry Reconciliation Matrix — v0.4.1

This matrix records **economic-sector disposition**, not automatic industry deletion. A technological successor may coexist with its predecessor. The matrix is deliberately a design artifact until canonical records and validation rules are migrated.

## Lifecycle vocabulary

- `persistent` — the sector remains economically available across the campaign.
- `transforming` — the sector changes technology, recipes, productivity, or customers.
- `emerging` — a later-era capability becomes available.
- `declining` — demand or relative importance falls, but the sector remains usable.
- `phase_out` — reserved for a genuinely obsolete process with an explicit successor rationale.

## Sector matrix

| Sector family | Current model direction | Reconciled disposition | 2150–2299 treatment |
|---|---|---|---|
| Agriculture | Traditional → mechanized → precision → automated | `persistent` + `transforming` | Continue advanced/automated variants; do not delete farming. |
| Forestry | Traditional → industrial → mechanized → precision/sustainable | `persistent` + `transforming` | Continue sustainable/managed forestry and timber outputs. |
| Fisheries | Coastal → commercial → advanced | `persistent` + `transforming` | Continue advanced, managed, or aquaculture-oriented production. |
| Coal extraction | Early → mechanized → modern | `persistent` + `declining` | Retain niche, materials, industrial, and legacy demand even where fuel demand falls. |
| Coke production | Coal-derived industrial carbon for metallurgy | **`persistent` + `transforming`** | Keep Coke Works available; demand and customers may shift. No automatic phase-out. |
| Iron | Primary extraction and mechanization | `persistent` + `transforming` | Continue extraction alongside recycling and advanced metallurgy. |
| Quarry / clay / sand | Foundational mineral inputs | `persistent` | Extend through Era IV; construction materials remain a permanent demand source. |
| Oil / gas | Energy and feedstock inputs | `persistent` + `declining` + `transforming` | Preserve chemical/material feedstock roles even if combustion demand declines. |
| Steel | Conventional → advanced steelmaking | `persistent` + `transforming` | Continue steel through recycled, electric, hydrogen, and other future routes. |
| Copper / glass / ceramics / aluminum / titanium | Durable materials | `persistent` + `transforming` | Continue with advanced processing and new demand centers. |
| Precious metals | Processing and specialty/financial uses | `persistent` + `transforming` | Retain niche industrial, electronics, reserve, and luxury demand with explicit sinks. |
| Rare earths | Advanced-material processing | `persistent` + `transforming` | Continue for electronics, energy, robotics, and advanced manufacturing. |
| Food | Processing for population centers | `persistent` + `transforming` | Continue as a core population-linked consumer sector. |
| Construction materials | Stone, clay, sand, lumber, steel, cement/concrete | `persistent` + `transforming` | Remains a permanent economic sink across all four eras. |

## Coke and carbon-materials decision

Coke is **not** a temporary placeholder and must not be removed merely because later steelmaking technologies appear. The economy should model changing demand rather than industry deletion:

```text
Coal / gas / biomass / recycled carbon
                 ↓
       Carbon Materials Processing
          ├── Metallurgical coke
          ├── Foundry coke
          ├── Industrial carbon
          ├── Graphite
          ├── Carbon fiber
          ├── Graphene
          └── Synthetic diamond
```

These are separate branches, not a magical `coal → diamond` conversion. Synthetic diamond is a late technology-gated product requiring an advanced carbon feedstock and its own specialized process and demand. The exact recipes belong in a later recipe-reconciliation pass.

## Construction-material decision

Construction remains persistent. The intended material progression is:

```text
Stone + clay + sand
        ↓
   Lime / cement
        ↓
Concrete / construction materials
        ↓
Construction demand
```

Lumber, steel, glass, ceramics, aluminum, and advanced materials may join the construction chain by era. Cement/concrete should be represented as a coherent chain rather than as an isolated cargo.

## Explicit non-decisions

- Do not expand NML from this matrix yet.
- Do not mark Coke Works as `phase_out`.
- Do not add synthetic-diamond recipes to the implemented graph yet.
- Do not rewrite the large canonical industry file until the full matrix and validator migration plan are complete.

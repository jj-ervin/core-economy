# Industry Endpoint Reconciliation — v0.4.1

## Purpose

This document defines the required treatment of industry records whose legacy era data ends at 2150. The architecture horizon is 1700–2299, with Era IV covering 2150–2299. A record ending at 2150 is therefore incomplete unless it is explicitly transformed or phased out.

## Endpoint policy

Every canonical industry record must receive exactly one endpoint disposition:

- `continue`: the existing industry function remains available through 2299.
- `transform`: a successor or future variant carries the function forward.
- `decline`: the function remains available but with reduced relative demand.
- `phase_out`: the function ends only with a documented successor and rationale.

A successor relationship alone does not authorize deletion.

## Required sector treatment

| Sector / family | Required endpoint disposition | Rationale |
|---|---|---|
| Agriculture | `continue` / `transform` | Food production remains necessary; technology changes. |
| Forestry | `continue` / `transform` | Timber, biomass, ecological, and material roles remain. |
| Fisheries | `continue` / `transform` | Managed fisheries and aquaculture provide continuation. |
| Coal | `decline` / `continue` | Fuel demand may fall, but metallurgy and carbon-feedstock roles remain. |
| Coke Works | **`continue` / `transform`** | Coke remains useful for blast furnaces, foundries, and specialty carbon. |
| Iron | `continue` / `transform` | Primary extraction coexists with recycling and alternative metallurgy. |
| Quarry, clay, sand | `continue` | Construction and materials remain persistent sinks. |
| Oil and gas | `decline` / `transform` | Preserve chemical, polymer, lubricant, fertilizer, hydrogen, and specialty feedstock roles where modeled. |
| Steel | `continue` / `transform` | Steel remains a core material despite production-route changes. |
| Copper, glass, ceramics, aluminum, titanium | `continue` / `transform` | Durable and advanced materials remain economically relevant. |
| Precious metals | `continue` / `transform` | Industrial, electronics, reserve, medical, and luxury demand persists. |
| Rare earths | `continue` / `transform` | Advanced technology creates continuing demand. |
| Food processing | `continue` / `transform` | Population-linked demand persists across all eras. |
| Construction | `continue` | Permanent economic sink for infrastructure, buildings, and future habitats. |
| Cement / lime / concrete | `continue` / `transform` | Foundational construction-material chain; future binders may change recipes. |

## Coke-specific acceptance rules

1. Coke Works must not be marked `phase_out` in the current model.
2. Coke must remain available after 2150.
3. Reduced blast-furnace demand may be represented through demand or recipe changes.
4. Future carbon-materials processing must not silently replace Coke Works.
5. Metallurgical coke, foundry coke, industrial carbon, graphite, carbon fiber, graphene, and synthetic diamond are distinct product concepts.
6. Synthetic diamond must be modeled later as a separate technology-gated process; no direct `coal → synthetic diamond` shortcut is permitted.

## Construction-material acceptance rules

The canonical model must eventually represent a coherent chain in which stone, clay, and sand can feed lime/cement/concrete or an equivalent construction-material process. Lumber, steel, glass, ceramics, aluminum, and advanced materials may join by era. Cement must not be introduced as an isolated cargo with no producer or consumer.

## Migration sequence

1. Parse and count every canonical industry record.
2. Normalize legacy lifecycle values into economic lifecycle values without deleting legacy compatibility prematurely.
3. Assign every record an endpoint disposition.
4. Repair successor/predecessor references and verify reciprocity.
5. Validate every hard input, output, operational supply, and cargo reference.
6. Add construction-material records and recipes.
7. Add future carbon-materials records only when their recipes and consumers are specified.
8. Run validation before any NML expansion.

## Explicit status

This is a reconciliation contract for the canonical-data migration. It does not claim that the full 1700–2299 industry graph is already implemented in the current NewGRF.

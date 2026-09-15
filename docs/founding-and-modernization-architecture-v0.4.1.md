# Founding & Modernization Architecture v0.4.1

## Status

Design-locked architecture. This document records the final scope addition for player-founded economic sites and modernization incentives. It does not implement GameScript/Dynamics or expand the current NML slice.

## Player-founded sites

Players may eventually found either:

- `town` — a new settlement established near resources, markets, transport, or existing infrastructure.
- `industrial` — a new industrial complex established near resources, infrastructure, labor, or markets.

Founding is an economic decision, not merely a geographic placement action.

### Site evaluation factors

A founding decision may consider:

- resource proximity and expected longevity
- existing transport infrastructure
- population and labor access
- market access
- transport cost and expected throughput
- industry lifecycle and technology trajectory
- infrastructure condition and modernization potential
- diversification/redevelopment potential
- environmental and social consequences

The player should receive enough information to make an informed strategic choice without being given perfect knowledge of future events.

### Risk/reward model

A site may be attractive because it has:

- low founding cost
- excellent current resource access
- existing rail/road/port infrastructure
- immediate employment and demand
- strong short-term profitability

The same site may carry long-term risks:

- resource depletion
- industry decline
- technology-driven demand reduction
- infrastructure obsolescence
- stranded-asset exposure

These risks are independent. Resource depletion does not automatically mean industry decline, and industry decline does not automatically make infrastructure useless.

## Modernization as an economic choice

Declining or aging infrastructure should create pressure and opportunity to modernize rather than forcing automatic replacement.

The intended loop is:

`older infrastructure/vehicles -> declining efficiency -> economic pressure -> modernization opportunity -> improved capacity/efficiency`

Modernization may include:

- replacing older vehicles with newer vehicles
- upgrading transport infrastructure
- rebuilding or modernizing industrial facilities
- replacing obsolete production technology
- converting infrastructure to support new economic roles

Benefits may include lower operating costs, higher capacity, greater reliability, improved speed, or access to new cargo/industry opportunities. Costs may include capital expenditure, transition disruption, or stranded investment.

Players may continue operating older assets when they remain economically viable. Modernization is an incentive-driven strategic choice, not a mandatory scripted upgrade.

## Decline, redevelopment, and stranded assets

A declining industry should not automatically destroy the settlement or invalidate all nearby infrastructure.

A former resource-oriented town or industrial site may:

- diversify into other industries
- reuse transport infrastructure
- modernize its network
- convert industrial facilities to new production
- become a lower-growth settlement
- eventually decline substantially when alternatives fail

This allows economic history to emerge from player decisions rather than from automatic deletion rules.

## Runtime boundary

### NewGRF

NewGRF remains responsible for the industry/cargo runtime model, including:

- industries
- cargoes
- production
- technology/era behavior
- industry lifecycle state
- economic effects exposed through the NewGRF model

### GameScript / Dynamics

GameScript/Dynamics is the intended owner of higher-level world and player actions, including:

- founding towns and industrial sites
- founding costs
- site viability evaluation
- player-facing site information
- incentives and consequences
- settlement growth/decline
- redevelopment and diversification
- stranded-infrastructure consequences

No GameScript/Dynamics implementation is part of v0.4.1 industry reconciliation.

### Sidecar / Admin

A future external Sidecar/Admin layer remains permitted for observation, administration, diagnostics, analytics, historical/event inspection, and development tooling. It is not a dependency of the core simulation.

## Scope lock

This is the final architecture addition for the current reconciliation stage. Future ideas should normally be expressed using these existing mechanisms rather than creating new top-level economic subsystems. Genuine extensions should be documented as future work instead of expanding the current implementation stage.

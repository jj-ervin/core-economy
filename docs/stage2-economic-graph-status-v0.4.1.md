# Core Economy — Stage 2 Reconciliation Status v0.4.1

## Current status

**Stage 2 audit: complete.**  
**Canonical graph repair: substantially complete, validation gate still open.**  
**Stage 3 NML expansion: remains blocked pending passing validation.**

## Repairs completed

- Corrected `steel_lumber_machinery_to_advanced_goods` to produce `advanced_goods`.
- Added canonical extraction coverage for Bauxite, Titanium Ore, Gold Ore, Silver Ore, and Rare Earth Ore.
- Extended the existing Quarry to produce Sand as a defensible co-output, avoiding a redundant new extraction system.
- Added the documented Cement transformation: Stone + Clay + Sand -> Cement.
- Connected Cement into Construction Materials production.
- Normalized `FIN_SYSTEM` to the canonical `financial_services` sector and converted it to a service endpoint/sink rather than an industrial producer of Advanced Goods.
- Removed synthetic passenger production from passenger-port and offshore-supply logistics industries.

## Still unresolved

1. Precious Metals Works still exposes Gold/Silver as alternative feedstock while declaring both outputs. The economic model needs an explicit co-product or separate-process decision before this is considered fully reconciled.
2. The advanced/legacy downstream economic role of Aluminum and Titanium remains weak and should be resolved only from existing canonical intent, not invented gameplay.
3. Chemical Works alternative semantics need final validator confirmation across all recipes and eras.
4. Era IV (2150–2299) remains an endpoint/lifecycle contract issue rather than a new graph subsystem; many variants terminate at 2150 and need the existing lifecycle/endpoint rules checked for full continuity.

## Explicitly deferred

Electricity/Power, textiles, geography, depletion, settlements, modernization, GameScript/Dynamics, Sidecar/Admin, and future carbon-material branches beyond the locked Coke decision remain outside Stage 2 repair.

## Validation gate

Before Stage 3:

- existing contract validator must pass;
- graph validator must pass;
- all four eras must have source-to-sink reachability for active economic chains;
- no orphan cargoes or industries may remain unless explicitly classified as endpoint/flow/deferred;
- alternative-input semantics must agree between industry definitions and recipes;
- successor flow continuity must pass;
- no unrelated cleanup or architecture expansion is permitted.

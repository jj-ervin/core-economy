# Core Economy — Stage 2 Reconciliation Status v0.4.1

## Current status

**Stage 2 audit: complete.**  
**Stage 2 canonical graph: not yet complete.**  
**Stage 3 NML expansion: blocked until graph validation passes.**

## Completed in this branch

- Completed canonical cargo/industry/recipe/endpoint/lifecycle inspection.
- Recorded the full Stage 2 economic graph audit in `docs/stage2-economic-graph-audit-v0.4.1.md`.
- Corrected `steel_lumber_machinery_to_advanced_goods` so it produces `advanced_goods` rather than `manufactured_goods`.
- Added `tools/validate_economic_graph.py` for producer/consumer/source/sink, flow-cargo, recipe compatibility, and succession-flow checks.
- Added the graph validator to the economy CI workflow.

## Remaining canonical repairs

### Unambiguous graph defects

- Add missing primary extraction sources for Sand, Bauxite, Titanium Ore, Gold Ore, Silver Ore, and Rare Earth Ore.
- Complete the documented Stone/Clay/Sand -> Lime/Cement -> Construction Materials chain.
- Normalize `FIN_SYSTEM` to the canonical sector vocabulary.
- Remove synthetic passenger production from logistics industries and preserve passengers as a transport/endpoint flow.

### Semantics requiring explicit reconciliation

- Precious Metals Works currently describes alternative Gold/Silver feedstock while outputting both products. The graph needs explicit co-product or separate-process semantics.
- Chemical Works has alternative Petroleum Products/Gas feedstock semantics while recipes are represented as separate explicit paths. The validator now needs to treat these as alternative production paths rather than requiring both inputs.
- Aluminum, Titanium, Gold, Silver, and Advanced Goods need explicit downstream economic roles where current records are only weakly connected.

## Explicitly deferred

Electricity/Power, textiles, geography, depletion, settlements, modernization, GameScript/Dynamics, Sidecar/Admin, and future carbon-material branches beyond the locked Coke decision remain outside this repair pass.

## Exit gate

Stage 3 is permitted only after:

1. all missing primary sources have canonical industry definitions;
2. the construction chain is connected;
3. financial/precious-metal semantics are resolved;
4. passenger flow handling is no longer modeled as synthetic industrial production;
5. graph validation passes for all four eras;
6. the existing contract validator still passes;
7. no new scope or runtime subsystem has been introduced.

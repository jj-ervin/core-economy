# Core Economy — Stage 2 Economic Graph Audit v0.4.1

## Status

**Audit complete. No canonical economy data or runtime implementation was changed by this audit commit.**

Scope is limited to reconciling the existing canonical economy before Stage 3 NML expansion.

## 1. Inspected

Canonical and implementation artifacts inspected:

- `data/reference-economy/economy.json`
- `data/reference-economy/cargoes.json`
- `data/reference-economy/materials.json`
- `data/reference-economy/recipes.json`
- `data/reference-economy/industries.json`
- `data/reference-economy/industry-lifecycle.json`
- `data/reference-economy/industry-endpoints.json`
- `data/reference-economy/modules.json`
- `tools/validate_economy.py`
- `docs/industry-registry.md`
- `docs/industry-reconciliation-matrix-v0.4.1.md`
- `data/implementation-manifest.json`

Repository HEAD was `612900bfa45050fddac94c05582825374eae18cb` at audit start.

The canonical manifest contains 44 cargo IDs, 65 industry IDs, and 30 recipe IDs. The implementation manifest correctly limits shipped NewGRF scope to the four-industry historical steelmaking slice.

## 2. Graph model

The canonical production graph is interpreted as:

`source industry -> cargo -> consuming industry -> output cargo -> next consumer`

Operational supplies are treated as support edges, not mandatory production edges unless explicitly represented as hard inputs. Human-flow cargoes (`passengers`, `personnel`, `mail`) are not ordinary industrial products and require endpoint/transport semantics rather than an assumption that an industry must manufacture them.

## 3. Cargo coverage audit

| Cargo family | Finding | Status |
|---|---|---|
| Grain, Livestock | Farm outputs; food feedstock | VALID |
| Timber | Forestry output; sawmill input | VALID |
| Fish | Fishery output; food feedstock | VALID |
| Coal | Coal extraction; coke feedstock; retained beyond fuel decline | VALID |
| Iron Ore | Iron extraction; steel feedstock | VALID |
| Stone | Quarry output; construction recipe input | VALID |
| Clay | Clay pit output; ceramics/construction inputs | VALID |
| Oil | Onshore/offshore extraction; refinery feedstock | VALID |
| Gas | Gas extraction/offshore output; chemical feedstock path | VALID |
| Copper Ore | Copper extraction; copper processing | VALID |
| Sand | Glass/construction input but no canonical source industry | MISSING |
| Bauxite | Aluminum input but no canonical source industry | MISSING |
| Titanium Ore | Titanium input but no canonical source industry | MISSING |
| Gold Ore | Precious-metal input but no canonical source industry | MISSING |
| Silver Ore | Precious-metal input but no canonical source industry | MISSING |
| Rare Earth Ore | Rare-earth processing input but no canonical source industry | MISSING |
| Coke | Coal-derived; persistent; steel feedstock | VALID |
| Steel | Steel production; many downstream consumers | VALID |
| Copper | Copper production; machinery/electronics consumers | VALID |
| Glass | Glass production; advanced electronics input | VALID |
| Ceramics | Ceramics production; construction role documented | VALID |
| Aluminum | Aluminum production; downstream construction/manufacturing role not yet explicit | DESIGN_DECISION_REQUIRED |
| Titanium | Titanium production; downstream role not explicit | DESIGN_DECISION_REQUIRED |
| Gold/Silver | Produced and referenced by financial system; downstream industrial/consumer sink is weak | CONTRADICTORY |
| Rare Earth Materials | Produced; electronics/technology use exists | VALID |
| Food | Produced by food processors; town demand is documented | VALID |
| Lumber | Produced by sawmills; manufacturing/construction use | VALID |
| Petroleum Products | Refinery output; fuel/chemical feedstock | VALID |
| Machinery | Machinery works output; factories/equipment/advanced goods use | VALID |
| Chemicals | Chemical works output; multiple downstream uses | VALID |
| Manufactured Goods | Factory output; town demand documented | VALID |
| Electronics | Electronics works and advanced electronics paths; technology systems/advanced goods use | VALID |
| Advanced Goods | Advanced goods works output; current financial-system output is semantically suspect | CONTRADICTORY |
| Tools & Hardware | Supply-production output; operational inputs | VALID |
| Industrial Equipment | Supply-production output; operational inputs | VALID |
| Construction Materials | Supply-production output; construction support and steel support | VALID but incomplete construction chain |
| Agricultural Supplies | Supply-production output; farm support | VALID |
| Technology Systems | Supply-production output; advanced operations | VALID |
| Fuel | Petroleum-derived supply path; industrial support | VALID |
| Passengers | Human-flow cargo; current port output placeholders are not true production | CONTRADICTORY |
| Personnel | Human-flow transport role; not an ordinary manufactured cargo | INTENTIONALLY_DEFERRED |
| Mail | Human-flow transport role; not an ordinary manufactured cargo | INTENTIONALLY_DEFERRED |

## 4. Known issue audit

### Advanced Electronics

The `advanced_electronics` recipe produces `electronics` and consumes Copper, Chemicals, Glass, and Rare Earth Materials. The canonical advanced electronics industry also accepts those materials and produces Electronics. This is a valid alternative production path, not a separate `advanced_electronics` cargo.

**Status: VALID**, with validator coverage required to ensure recipe/industry input compatibility remains explicit.

### `steel_lumber_machinery_to_advanced_goods`

The recipe ID/name describes an advanced-goods transformation but currently declares `manufactured_goods` as its output. A separate `electronics_chemicals_machinery_to_advanced_goods` recipe correctly outputs `advanced_goods`.

**Status: BROKEN.** Minimal repair: make the first recipe output `advanced_goods` (or explicitly rename/redefine it if canonical intent proves otherwise). Do not create a new cargo.

### Chemical gas alternative

The industry registry defines Chemical Works as accepting Petroleum Products **or** Gas through an explicit `chemical_feedstock` alternative group. The recipe set instead has separate petroleum and gas recipes, which is compatible with explicit alternative production paths, but the industry contract must match those recipes rather than implying both are simultaneously required.

**Status: CONTRADICTORY.** Minimal repair: normalize the industry/recipe semantics so Petroleum Products and Gas are explicit alternative feedstock recipes in the same canonical group.

### Port passenger outputs/placeholders

Port industries currently output `passengers` even though they are logistics industries. Project documentation treats passengers as ordinary travel flow and towns as endpoints. A port should move/handle passenger flow, not manufacture passengers.

**Status: CONTRADICTORY.** Minimal repair requires removing synthetic passenger production from the canonical industrial production graph and representing passenger handling as transport/endpoint behavior. Runtime adapter work remains outside this Stage 2 graph repair.

### `FIN_SYSTEM`

`FIN_SYSTEM` is declared as a service industry but currently uses sector `financials`, while the canonical sector manifest uses `financial_services`; this is a direct manifest mismatch. It also lists Gold, Silver, and Rare Earth Materials as optional inputs and outputs `advanced_goods`, which conflates financial/specialty-material handling with industrial production.

**Status: BROKEN / DESIGN_DECISION_REQUIRED.** The sector identifier must be normalized. The economic role of precious/rare materials in the financial system must be explicitly defined before treating the system as a producer of Advanced Goods. Do not invent a financial cargo or new financial subsystem in Stage 2.

### Electricity / power

No Electricity/Power cargo exists in the canonical cargo manifest, and no industry currently depends on it as a hard input. Existing operational-supply semantics use Fuel, Industrial Equipment, Technology Systems, etc.

**Status: INTENTIONALLY_DEFERRED.** Do not add an electricity system merely to satisfy the audit. Future power integration must be a separately defined canonical decision.

### Cement / lime / construction

The reconciliation matrix explicitly requires a coherent Stone/Clay/Sand -> Lime/Cement -> Concrete/Construction Materials chain, while the canonical cargo manifest contains none of Lime, Cement, or Concrete. Construction Materials currently has a direct Stone + Clay + Lumber + Steel recipe.

**Status: MISSING.** This is not optional cleanup: the locked construction-economy rule requires a real construction-material transformation chain. Minimal Stage 2 repair should add the smallest canonical Lime/Cement representation necessary to connect the existing Stone/Clay/Sand resources to Construction Materials, without creating a new gameplay subsystem.

### Textiles

There is no Textile cargo, textile industry, or textile recipe in the canonical economy. The existing canonical model does not currently define a textile chain.

**Status: INTENTIONALLY_DEFERRED.** Do not invent a textile subsystem during Stage 2. If textile demand becomes necessary for an existing manufacturing chain, that becomes a specific design decision rather than an inferred repair.

### Gold / Silver

Gold Ore and Silver Ore have processing recipes and the Precious Metals Works record has an alternative feedstock group while outputting both Gold and Silver. The recipes separately produce Gold or Silver. This creates an industry-level contradiction: an alternative feedstock means one of the ores can satisfy the requirement, while the output record claims both refined products emerge.

**Status: CONTRADICTORY.** Minimal repair should make the canonical production semantics explicit: either separate production paths for Gold and Silver, or a clearly defined co-product process. Do not silently assume one ore creates both outputs.

### Rare Earths

Rare Earth Ore -> Rare Earth Materials is coherent and Rare Earth Materials feed Advanced Electronics and Technology Systems. The upstream extraction industry is missing.

**Status: MISSING upstream source.** Add the minimal extraction source required by the existing canonical chain; do not alter the downstream recipe unless later evidence requires it.

## 5. Industry reconciliation

### Strong coherent families

- Agriculture: persistent transformation family with grain/livestock outputs.
- Forestry: persistent transformation family with timber outputs.
- Fisheries: persistent transformation family with fish outputs.
- Coal -> Coke -> Steel: coherent historical vertical slice; Coke remains persistent.
- Iron -> Steel: coherent.
- Copper Ore -> Copper: coherent.
- Oil -> Petroleum Products -> Fuel/Chemicals: coherent.
- Timber -> Lumber: coherent.
- Food feedstock alternatives -> Food: coherent.
- Steel/Copper/Chemicals -> Machinery: coherent.
- Steel/Lumber -> Manufactured Goods: coherent.
- Copper/Chemicals/(Glass/Rare Earth) -> Electronics: coherent once the advanced recipe is treated as an explicit alternative path.
- Electronics/Chemicals/Machinery -> Advanced Goods: coherent.

### Industry/source gaps

The following canonical raw cargoes are consumed but have no source industry: Sand, Bauxite, Titanium Ore, Gold Ore, Silver Ore, Rare Earth Ore.

This is the largest graph-level defect in the current model because it prevents the graph from being playable from raw-resource extraction through downstream transformation.

## 6. Successor/predecessor audit

The Stage 1 validator already checks reference validity, reciprocity, cycles, and terminal endpoint coverage. The four-era lifecycle contract and 2299 endpoint contract are structurally coherent.

However, graph validation must additionally verify that successor variants preserve or intentionally transform the same economic role and cargo flow. A successor that changes inputs/outputs must be checked against the actual graph rather than only against its ID link.

No accidental successor cycle was identified from the canonical succession structure inspected.

## 7. Era validation

### Era I — 1700–1849

Core historical chains are present: agriculture, forestry, fisheries, coal, iron, quarrying, clay, ceramics, coke from 1750, steel from 1750, food, and early timber/construction processing.

**Result: BROKEN at full canonical scope** because Sand is required by Glass but lacks a source; Gold/Silver Ore also lack extraction sources; the construction chain lacks the documented cement/lime transformation.

### Era II — 1850–1999

Oil, gas, copper, aluminum, titanium, chemicals, petroleum products, machinery, factories, and electronics enter through documented dates. The steel/coke chain remains active.

**Result: BROKEN** due to the same upstream gaps plus chemical alternative semantics and the advanced-goods recipe mismatch.

### Era III — 2000–2149

Advanced food, forestry, copper, steel, chemical, machinery, factory, electronics, technology, and advanced-goods variants are represented.

**Result: BROKEN** due to unresolved graph gaps and the financial/advanced-goods contradiction.

### Era IV — 2150–2299

The endpoint contract provides campaign-horizon dispositions, but many legacy industry records end at 2150. This is intentional Stage 1 endpoint semantics, not by itself a graph defect.

**Result: INCOMPLETE / DESIGN-CONSTRAINED.** The endpoint contract is structurally valid, but the actual cargo transformations after 2150 are not sufficiently specified to prove full graph continuity for every persistent sector.

## 8. Minimal repair set

1. Correct `steel_lumber_machinery_to_advanced_goods` to its canonical Advanced Goods output.
2. Normalize Chemical Works gas/Petroleum Products alternative-feedstock semantics.
3. Normalize `FIN_SYSTEM` sector naming to the canonical sector vocabulary.
4. Remove/replace port passenger production placeholders with explicit flow semantics; do not manufacture passengers as an industrial output.
5. Resolve Precious Metals Works input/output semantics so Gold and Silver are not simultaneously implied by an alternative single feedstock.
6. Add missing primary-resource source coverage for Sand, Bauxite, Titanium Ore, Gold Ore, Silver Ore, and Rare Earth Ore using the smallest existing extraction-industry pattern.
7. Complete the construction chain with the documented Lime/Cement transformation into Construction Materials.
8. Strengthen validation to distinguish industrial production cargoes from endpoint human-flow cargoes and to validate graph connectivity by era.
9. Strengthen validation so every recipe has a compatible producer with compatible hard-input semantics, not merely an output match.
10. Validate alternative groups consistently between recipes and industry definitions.

## 9. Explicitly deferred

- Electricity/Power cargo and generation/distribution system.
- Textiles/textile industry.
- Geography and resource depletion.
- Settlement/population simulation.
- Modernization incentives and player-founded sites.
- GameScript/Dynamics implementation.
- Sidecar/Admin implementation.
- Future carbon-material branches beyond the already locked Coke decision, including synthetic diamond.
- NewGRF expansion beyond the existing implementation boundary.

## 10. Validator requirements discovered

The current validator is strong on schema/reference integrity but not yet graph-complete. Stage 2 validation should add:

- cargo source/sink coverage by role and era;
- recipe producer compatibility;
- recipe input compatibility with the actual producing industry;
- alternative-group equivalence checks;
- detection of recipe output/name contradictions where canonical IDs encode intent;
- detection of industrial industries producing human-flow cargoes unless explicitly marked as flow handlers;
- endpoint-flow exceptions for Passengers/Personnel/Mail;
- era-aware reachability from primary sources to economic sinks;
- orphan cargo detection;
- orphan industry detection;
- raw cargo source detection;
- downstream sink detection;
- accidental directed cycles, while permitting explicitly designated economic loops if one is later defined;
- successor flow continuity checks;
- endpoint coverage checks already present in Stage 1.

## 11. Stage 2 exit condition

The graph is **not ready for Stage 3 NML implementation** yet.

Stage 2 should close the seven graph defects above, strengthen graph validation, and then run the complete four-era reachability audit again. Only when the canonical graph passes those checks should the NML implementation expand beyond the existing steelmaking vertical slice.

## 12. Commit boundary

This audit document is intentionally isolated from canonical data repairs. Subsequent commits should be narrow and reviewable:

1. graph contract / validator hardening;
2. canonical cargo/industry/recipe repairs;
3. construction-chain reconciliation;
4. final validation/reporting.

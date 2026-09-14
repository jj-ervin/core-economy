# Core Economy Industry Model Reconciliation — v0.4.1

## Purpose

Reconcile the canonical industry graph with the four-era architecture merged in v0.4.1.

This document is a working reconciliation record. It distinguishes an economic sector from an implementation-era industry variant. A successor relationship does **not** imply that the predecessor disappears when the successor becomes available.

## Locked rules

1. Overall game horizon: **1700–2299**.
2. Era slices are inclusive and exactly 150 years:
   - Era I: 1700–1849
   - Era II: 1850–1999
   - Era III: 2000–2149
   - Era IV: 2150–2299
3. Each era must be playable as a self-contained mini-economy.
4. The full game is a continuous progression across all four eras.
5. Economic sectors persist by default.
6. An industry variant may be persistent, transforming, emerging, declining, or phase-out.
7. `predecessor`/`successor` describes technological/economic succession, not automatic deletion.
8. Agriculture, forestry, construction, food, logistics, and other foundational sectors are persistent unless a specific economic reason says otherwise.
9. Construction is a persistent sink/sector. Cement must be represented in its material chain rather than added as an isolated cargo.
10. Era transitions may change recipes, productivity, demand, transport assumptions, or the relative importance of an industry without requiring sector extinction.

## Current findings

### Agriculture

The current graph already models Traditional → Mechanized → Precision → Automated farms, but these variants overlap in time. That is compatible with a transformation model only if overlap is intentional and documented. The model must not imply that all farms vanish when the next variant appears.

**Disposition:** persistent sector; transforming industry variants.

### Forestry

Traditional → Industrial → Mechanized → Precision/Sustainable forestry similarly represents technological transformation rather than sector replacement.

**Disposition:** persistent sector; transforming variants.

### Fisheries

Coastal → Commercial → Advanced represents a transformation path. The current 1970–2150 endpoint needs an explicit post-2150 policy: either a continuing advanced fishery or a new future variant. It should not silently disappear at 2150.

**Disposition:** persistent sector; transforming variants.

### Coal

Early → Mechanized → Modern is a useful technology progression. Coal should become declining after its historical peak rather than simply disappearing at a successor boundary. A future niche/legacy coal role may remain possible.

**Disposition:** persistent resource sector; transforming then declining variants.

### Iron

Iron Mine → Mechanized Iron Mine currently ends at 2150. Iron extraction should remain available after 2150 unless the future scenario deliberately replaces primary extraction with recycling/alternative materials.

**Disposition:** persistent resource sector; transforming variants.

### Quarry / Clay

These are correctly modeled as continuous foundational construction/material resources, but their end year of 2150 conflicts with the new 2299 horizon.

**Disposition:** persistent; extend/redefine through Era IV during reconciliation.

### Oil / Gas

Oil and gas are currently marked continuous to 2150. Their future role should be modeled as declining/transforming rather than an unexplained hard stop. They may remain as feedstocks even if energy demand falls.

**Disposition:** persistent-to-declining energy/feedstock sectors; future role requires explicit era treatment.

### Coke

Coke is an excellent example of a potentially phase-out industrial process rather than a permanent sector. It should remain important while coke-based steelmaking is important, then decline as steelmaking transitions to electric/recycled/alternative processes.

**Disposition:** transforming/declining; possible phase-out late in the campaign.

### Steel

Steel is a persistent materials sector. The current Steel Mill → Advanced Steel Works relationship should describe changing production technology, not steel disappearing.

**Disposition:** persistent sector; transforming variants.

### Copper / Glass / Ceramics / Aluminum / Titanium

These are durable materials sectors. Their current 2150 endpoints need reconciliation with the 2299 horizon. Some may gain future variants rather than simply ending.

**Disposition:** generally persistent; transforming variants where justified.

### Precious metals

Precious Metals Works is currently continuous to 2150 but has ambiguous output semantics and downstream rationale. Gold and silver should remain distinct resources/materials where useful; the processing model and financial endpoint require reconciliation.

**Disposition:** persistent/niche materials sector; model downstream demand explicitly.

### Rare earths

Rare Earth Processing begins in 1960, which is plausible as an industrial specialization. It should remain relevant beyond 2150 if the future economy uses electronics/technology systems.

**Disposition:** persistent/transforming advanced-materials sector.

### Food

Food Processing is a persistent consumer-staples sector. It should not be treated as an era-specific industry that expires.

**Disposition:** persistent sector; transforming variants.

### Construction / Cement

Construction must be treated as a permanent economic sink across the campaign. The reconciled graph should introduce a coherent cement/lime/concrete path and determine how stone, clay, sand, lumber, steel, and cement/concrete feed construction materials by era.

**Disposition:** persistent sector; transforming materials chain.

## Phase-out candidates

These require explicit justification before being marked `phase_out`:

- coke production, eventually
- coal-fired power generation, if modeled as a distinct industry
- legacy petroleum refining, potentially, while preserving petrochemical feedstock roles
- historically obsolete transport/production technologies if they are represented as industries
- other genuinely obsolete sectors only after a documented successor exists

## Reconciliation rule for 2150–2299

No canonical industry should end at 2150 merely because the old model ended there. Each industry must receive one of:

- continued/persistent
- transformed into a future variant
- declining but available
- explicitly phased out with successor rationale

## Next pass

1. Build the complete industry matrix from `data/reference-economy/industries.json`.
2. Normalize sector names and lifecycle semantics.
3. Repair era endpoints against 1700–2299.
4. Identify genuine phase-outs versus persistent sectors.
5. Add missing persistent construction/cement structure.
6. Reconcile recipes and cargo references.
7. Only then update canonical JSON and validator rules.
8. Do not expand NML until this matrix is internally consistent.

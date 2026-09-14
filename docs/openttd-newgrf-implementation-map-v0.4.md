# OpenTTD / NewGRF Implementation Map — Core Economy v0.4

## Purpose

This document maps the reusable Core Economy v0.4 contract onto the OpenTTD implementation stack. It deliberately separates what belongs in **NewGRF**, **GameScript/AI**, and an optional **external/sidecar layer** so the core economy is not constrained by one game's modding API.

## Architectural boundary

```text
Core Economy Definition
        |
        +-- Economic Contract / canonical data
        |
        +-- OpenTTD Game Profile
              |
              +-- NewGRF: static/content mechanics
              +-- GameScript: world-state/runtime policy
              +-- AI: transport/economic decision agents
              +-- Sidecar: audit, analytics, advanced policy
```

The canonical economy remains immutable during play. Runtime systems may apply bounded policy/state changes without rewriting canonical recipes or industry definitions.

## Capability matrix

| Core contract capability | OpenTTD mapping | Primary layer | Status |
|---|---|---|---|
| Cargo identities | Cargo definitions / cargo labels | NewGRF | Direct |
| Cargo classes | Cargo acceptance / handling / routing conventions | NewGRF + profile | Direct/adapter |
| Industries | Industry definitions | NewGRF | Direct |
| Industry succession | Availability dates + industry replacement/transition logic | NewGRF + GameScript | Hybrid |
| Historical eras | Date-gated industry/cargo availability | NewGRF | Direct |
| Base production ratios | Production callbacks / industry production rules | NewGRF | Direct |
| Runtime ratio policy | Bounded runtime modifiers | GameScript/profile adapter | Hybrid |
| Industry efficiency | Production modifiers / supply effects | NewGRF + GameScript | Hybrid |
| Operational supplies | Accepted supply cargos and production effects | NewGRF | Direct for bounded effects |
| Production multiplier | Industry production rules | NewGRF + GameScript | Hybrid |
| Modules | Profile/configuration selecting content families | Build/config layer | Direct |
| Demand endpoints | Towns, industries, ports, custom acceptance | NewGRF + GameScript | Hybrid |
| Passengers | Native passenger cargo | NewGRF/native | Direct |
| Personnel | Profile-specific labor flow representation | NewGRF + GameScript | Adapter required |
| Returning personnel | Flow/state concept | GameScript | Adapter required |
| Mail | Native mail cargo | NewGRF/native | Direct |
| Settlements | Towns | NewGRF + GameScript | Hybrid |
| Settlement specialization | Town state derived from accepted/produced cargo | GameScript | Adapter required |
| Town growth/shrinkage | Native growth plus scripted state | GameScript + NewGRF | Hybrid |
| Remote-market premium | Cargo contract/payment modifier | GameScript | Adapter required |
| Contracts | Script-managed economic contracts | GameScript | Adapter required |
| Scarcity premium | Scripted demand/price modifier | GameScript | Adapter required |
| Resource depletion | Production/resource state | GameScript + NewGRF | Hybrid |
| Exploration/prospecting | Deposit discovery / new industry placement | GameScript | Adapter required |
| Industry expansion | Industry state/capacity changes | GameScript + NewGRF | Hybrid |
| Capital/investment | Scripted investment state | GameScript | Adapter required |
| Industry health | Script-maintained state | GameScript | Adapter required |
| Geographic resources | Map location + industry generation rules | NewGRF + GameScript | Hybrid |
| Technology modifiers | Date/technology state affecting production | NewGRF + GameScript | Hybrid |
| Labor constraints | Personnel acceptance/production state | GameScript | Adapter required |
| Maintenance | Supply acceptance / scripted reliability | NewGRF + GameScript | Hybrid |
| Environmental externalities | Scripted state and event effects | GameScript | Adapter required |
| Events/catastrophes | Script events / scenario events | GameScript | Adapter required |
| Prosperity | World/settlement state | GameScript | Adapter required |
| Difficulty | Game settings / scenario parameters / script policy | GameScript + settings | Hybrid |
| Dynamic demand | Script-managed demand state | GameScript | Adapter required |
| Dynamic prices | Script-managed price modifiers and/or native economy interaction | GameScript | Adapter required |
| Economic pivots | Settlement/industry transition state | GameScript | Adapter required |
| Network resilience | Observed transport network state | AI/script/sidecar | Externalized metric |
| Causal records | Event/state log | Sidecar/script logging | Adapter required |
| Economic AI | Policy/state agent | GameScript/AI | Adapter required |
| Scenario composition | Scenario + script configuration | GameScript | Direct |

## NewGRF responsibilities

NewGRF should contain the durable game-content layer:

1. **Cargo set** — stable cargo identities and visual/handling properties.
2. **Industry set** — the physical economic actors and their historical availability.
3. **Production rules** — canonical/base recipes and production quantities.
4. **Industry families** — historical succession families such as traditional → mechanized → automated.
5. **Operational supply hooks** — Tools & Hardware, Industrial Equipment, Construction Materials, Agricultural Supplies, Fuel, Chemicals, and Technology Systems where OpenTTD mechanics can express the intended effect.
6. **Town acceptance/content hooks** — Food, Manufactured Goods, Passenger, Mail and profile-selected consumer flows.
7. **Graphics and metadata** — industry appearance, cargo sprites, station interaction and period presentation.

NewGRF is the right place for things that should remain deterministic, content-defined, and portable across games using the profile.

## GameScript responsibilities

GameScript should own mutable world state and rules that depend on the evolving game:

- settlement prosperity and specialization
- population pressure and growth/shrinkage modifiers
- resource depletion
- prospecting and discovery
- industry capacity and expansion
- contracts and scarcity premiums
- dynamic demand
- runtime economic policy
- events and catastrophes
- investment/capital state
- industry health
- labor/personnel state
- environmental state
- economic pivots
- bounded AI policy
- causal/event records

This is also where the **difficulty profile** should be applied. Difficulty changes should select parameter bounds and event frequencies rather than mutate canonical economy definitions.

## AI responsibilities

The transport AI should not become the economic authority. Its role is to operate within the economic environment:

```text
observe economy
    -> evaluate opportunities/risks
    -> choose transport investment
    -> build/modify network
    -> observe results
    -> adapt
```

An economic AI may recommend or apply bounded policy changes only through the runtime policy contract. It must not rewrite canonical recipes, cargo definitions, or historical industry definitions.

## Sidecar responsibilities

An optional external process can provide capabilities that are useful for development, balancing, and research but should not be required for ordinary gameplay:

- detailed causal logs
- replay/event analysis
- economy telemetry
- calibration against target ratios
- balance experiments
- policy-learning experiments
- network resilience analytics
- regression testing
- cross-game economy comparison

This layer is particularly useful because the same Core Economy can later be evaluated against OpenTTD and Farming Simulator profiles without putting game-specific analytics into the canonical data.

## OpenTTD profile structure

The implementation should eventually look approximately like:

```text
games/
  openttd/
    profile.json
    newgrf/
      cargoes.nml
      industries.nml
      production.nml
      graphics.nml
      towns.nml
    gamescript/
      economy.nut
      settlements.nut
      resources.nut
      events.nut
      policy.nut
      contracts.nut
      logging.nut
```

The exact directory layout is an implementation choice; the important boundary is that **core economy data is not duplicated into hand-maintained OpenTTD rules**.

## Profile responsibilities

The OpenTTD profile should declare:

- enabled modules
- supported cargoes
- supported industries
- supported endpoints
- supported runtime features
- mapping from core cargo IDs to OpenTTD cargo labels
- mapping from core industry IDs to NewGRF industry definitions
- which core relationships are exact, approximated, or unsupported
- conversion/scaling rules where OpenTTD's production units differ from canonical units
- profile-specific limitations

Example conceptual profile:

```json
{
  "id": "openttd",
  "core_economy": "reference_economy",
  "core_version": "0.4.0",
  "enabled_modules": ["core", "materials", "energy", "chemicals", "technology", "agriculture", "forestry", "fisheries", "heavy_industry", "construction", "food", "manufacturing", "offshore", "ports"],
  "runtime": {
    "newgrf": true,
    "gamescript": true,
    "ai": true,
    "sidecar": true
  }
}
```

## Known implementation constraints

### 1. Canonical ratio vs runtime ratio

The core economy can define a historical/base ratio and permitted bounds. OpenTTD's NewGRF layer should implement the baseline. Runtime changes belong to the script/profile layer where the engine permits them.

Do **not** pretend that arbitrary live editing of NewGRF source data is equivalent to runtime policy.

### 2. Personnel

Personnel is deliberately distinct from Passengers. OpenTTD does not automatically provide a perfect labor-market simulation, so the profile needs an explicit representation. The first implementation may use a dedicated cargo/flow abstraction while GameScript maintains the labor-state semantics.

### 3. Financial system

Gold, Silver and Rare Earth Materials can participate in financial/economic state, but the financial endpoint should not manufacture Advanced Goods. Money remains an economic state variable, not an automatic cargo conversion.

### 4. Settlement evolution

OpenTTD towns have native growth mechanics, but the Core Economy's richer lifecycle — FOUND → GROW → SPECIALIZE → PROSPER → CHALLENGE → ADAPT — should be implemented as a scripted overlay rather than forced into NewGRF alone.

### 5. Resource discovery

A fully dynamic prospecting system is a world-state operation. NewGRF can define industry types and their properties; GameScript should decide when/where a new deposit becomes discoverable.

## Implementation priority

### Phase A — deterministic NewGRF core

1. Cargo definitions.
2. Materials processing chain.
3. Historical industry availability.
4. Production recipes.
5. Industry succession.
6. Town acceptance.
7. Baseline operational supplies.
8. Graphics/stations as needed.

### Phase B — economic simulation

1. Settlement state.
2. Resource depletion.
3. Dynamic demand.
4. Industry health/capacity.
5. Contracts and scarcity premiums.
6. Events/catastrophes.
7. Prosperity and pivots.
8. Runtime policy bounds.

### Phase C — adaptive transport economy

1. Network observation.
2. Resilience metrics.
3. Transport investment feedback.
4. AI behavior.
5. Optional sidecar telemetry and causal analysis.

## Validation rule

Before implementing a NewGRF feature, the mapping must answer:

> **Is this canonical economic truth, a game-specific representation, or mutable runtime state?**

If it is canonical truth, keep it in Core Economy data.
If it is OpenTTD representation, put it in the OpenTTD profile/NewGRF adapter.
If it changes during play, put it in runtime state/GameScript.
If it exists mainly for measurement or research, put it in the sidecar.

That boundary is the mechanism that keeps the project reusable for future game profiles.

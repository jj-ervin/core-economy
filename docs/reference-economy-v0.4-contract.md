# Reference Economy v0.4 — Architecture & Contract

## Status

**Frozen feature baseline:** v0.4.0

This document freezes the Reference Economy feature set discovered during the v0.3 design/reconciliation work. v0.4 is an architecture contract, not a promise that every system is already implemented in OpenTTD/NewGRF.

The Reference Economy remains a concrete 1700–2150 implementation of the reusable Economy Toolkit.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

---

## 1. What v0.4 Adds

v0.4 formalizes the following layers in addition to the existing cargo/industry/recipe/era model:

1. **Runtime economic policy** — adjustable production ratios, efficiency, capacity, demand and other bounded parameters without rewriting canonical definitions.
2. **Difficulty profiles** — named parameter sets such as Easy, Normal, Hard and Custom.
3. **World state** — prosperity, recession, crisis, technology, resource condition and other global/regional state.
4. **Data-driven events/catastrophes** — temporary or persistent economic shocks represented as data.
5. **Dynamic settlements** — towns/cities can grow, stabilize, specialize, shrink and recover according to economic conditions.
6. **Resource depletion and exploration** — deposits can decline; regions can investigate for new resources.
7. **Economic transition/pivot** — settlements and regions can diversify or change specialization when their existing economic base weakens.
8. **Dynamic demand and pricing** — demand and scarcity influence economic opportunities rather than relying only on static cargo acceptance.
9. **Industry capacity and investment** — productive capacity can expand, contract and require investment.
10. **Labor and Personnel economics** — labor requirements vary with industry scale and technology.
11. **Infrastructure/resource resilience** — diversified and redundant transportation networks can be more resilient to economic shocks.
12. **Causal records** — important economic changes should retain machine-readable reasons/causes so players and AI can understand what changed and why.

These are the **frozen v0.4 concepts**. New cargoes are not part of the v0.4 expansion plan unless a later change demonstrates a missing economic relationship that cannot be represented with existing abstractions.

---

## 2. Layered Architecture

```text
                 CANONICAL ECONOMY
       Cargoes / Recipes / Industries / Eras
                         │
                         ▼
              ECONOMIC PARAMETERS
      Base ratios / capacity / efficiency / demand
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
       DIFFICULTY                 WORLD STATE
        profile             prosperity / technology
            │              resources / events / shocks
            └────────────┬────────────┘
                         ▼
                 POLICY ENGINE
        scenario + player + AI adjustments
                         │
                         ▼
                    SIMULATION
          industries / settlements / networks
                         │
                         ▼
                      RECORD
              state + causes + decisions
```

### Authority boundary

Canonical economy data is authoritative for **what exists and what the base rules are**.

Runtime policy is authoritative only for **bounded adjustments to those rules during simulation**.

The policy layer must never rewrite canonical definition files during play.

---

## 3. Canonical Economy vs Runtime State

### Canonical definition data

Stable source-of-truth files include:

- `economy.json`
- `cargoes.json`
- `industries.json`
- `recipes.json`
- `materials.json`
- `modules.json`
- schemas under `schema/`

### Runtime state

Runtime state may contain:

- current production ratios;
- efficiency modifiers;
- industry capacity;
- current demand pressure;
- current prices;
- resource remaining/quality;
- settlement population/prosperity;
- active events;
- technology level;
- policy decisions;
- AI proposals and applied adjustments.

Runtime state can be saved, replayed, inspected and reset without changing the canonical economy.

---

## 4. Adjustable Production Ratios

Every recipe has a canonical base ratio. A recipe may additionally declare whether its ratio is adjustable and the permitted bounds.

Conceptual model:

```text
base recipe
    ↓
policy ratio modifier
    ↓
effective recipe ratio
    ↓
industry efficiency
    ↓
actual production
```

Example:

```text
Steel:
  base iron_ore = 1.00
  base coke      = 1.00

Runtime policy:
  coke ratio = 0.90

Effective requirement:
  iron_ore = 1.00
  coke      = 0.90
```

Ratio adjustment must be bounded, auditable and reversible.

**Do not confuse:**

- recipe ratio — material relationship;
- efficiency — how effectively an industry converts inputs;
- capacity — maximum production throughput;
- production multiplier — temporary/global output scaling.

---

## 5. Difficulty Profiles

Difficulty is a policy profile, not a separate economy.

Initial conceptual profiles:

| Profile | Intended behavior |
|---|---|
| Easy | forgiving ratios, high resilience, low disruption severity |
| Normal | Reference Economy baseline |
| Hard | tighter economics, greater volatility and weaker resilience |
| Expert | severe constraints and stronger consequences |
| Custom | player-defined bounded parameters |

Difficulty may modify:

- allowable ratio ranges;
- demand volatility;
- price volatility;
- resource depletion rate;
- event frequency/severity;
- recovery speed;
- industry resilience;
- settlement growth sensitivity;
- exploration success probability.

Difficulty must not alter the identity or historical existence of canonical cargoes and industries.

---

## 6. World State

World state represents conditions that influence the economy without redefining it.

Representative state variables:

```text
prosperity
technology_level
investment_confidence
resource_pressure
labor_availability
trade_conditions
infrastructure_condition
```

State may exist globally, regionally or locally.

### Prosperity

Prosperity is a bounded economic condition that can influence:

- consumer demand;
- construction;
- passenger demand;
- investment;
- industrial expansion;
- advanced-goods demand;
- commercial activity.

Prosperity should be capable of rising and falling through simulation and events rather than functioning only as a scripted era flag.

---

## 7. Events and Catastrophes

Events are data.

An event definition should be able to specify:

```text
id
trigger
probability
start/duration
geographic scope
cargo effects
industry effects
settlement effects
infrastructure effects
price/demand effects
recovery
aftermath
```

Examples include:

- drought;
- flood;
- earthquake;
- volcanic event;
- war;
- embargo;
- pandemic;
- financial crisis;
- oil crisis;
- crop failure;
- labor shortage;
- mining accident;
- technological breakthrough;
- resource discovery;
- resource depletion;
- trade boom;
- recession;
- depression.

An event should normally **change state or parameters**, not directly prescribe a transportation solution.

Example:

```text
Flood
  → bridge capacity -100%
  → regional food supply -25%
  → construction demand +40%
```

The player decides how to respond.

---

## 8. Resources, Depletion and Exploration

Resource deposits may have:

- quantity/remaining reserves;
- quality;
- extraction cost;
- accessibility;
- geographic extent;
- discovery state;
- depletion behavior.

Depletion must be bounded and must not silently delete an industry from the game.

### Exploration

A region may invest in exploration using appropriate inputs such as:

- Personnel;
- Machinery;
- Industrial Equipment;
- Construction Materials;
- capital/investment.

Exploration is probabilistic and may result in:

- no discovery;
- small deposit;
- large deposit;
- strategic/rare deposit;
- discovery in a different location.

A discovery may create a new economic opportunity and alter transportation demand.

---

## 9. Settlements

Towns and cities are economic actors, not passive cargo endpoints.

Settlement state may include:

```text
population
prosperity
employment
housing
food_security
goods_access
industrial_access
resource_access
connectivity
growth_pressure
decline_pressure
specialization
```

### Growth

Growth responds to a combination of:

- population base;
- employment;
- food availability;
- goods access;
- construction activity;
- prosperity;
- connectivity;
- industrial opportunity;
- housing/capacity.

### Shrinkage

Settlements may decline when economic support weakens through:

- resource depletion;
- industry closure/contraction;
- prolonged shortages;
- unemployment;
- loss of connectivity;
- catastrophic events;
- sustained recession.

Decline does not imply permanent destruction. A settlement may stabilize or recover.

---

## 10. Settlement Specialization and Pivot

Settlements have **transition potential**, not immutable classes.

Possible economic directions include:

- resource extraction;
- agriculture;
- manufacturing;
- logistics;
- port/trade;
- commercial/services;
- technology;
- tourism;
- mixed economy;
- managed decline.

Transition potential should derive from conditions such as:

- geography;
- resources;
- population;
- transportation;
- existing industry;
- labor;
- capital;
- technology;
- nearby markets.

A declining mining town may therefore:

```text
resource town
    ↓
resource depletion
    ↓
transition window
    ├── explore
    ├── diversify
    ├── industrialize
    ├── become logistics hub
    ├── become service center
    └── decline
```

A pivot is an opportunity, not a guaranteed outcome.

---

## 11. Demand and Prices

Demand is dynamic and may depend on:

- population;
- prosperity;
- industry activity;
- technology;
- scarcity;
- season/event state;
- geographic isolation;
- contracts;
- public-service requirements.

Prices should respond to supply/demand pressure and scarcity within bounded ranges.

Conceptual form:

```text
price = base_price
      × supply_pressure
      × demand_pressure
      × scarcity
      × prosperity
      × event_modifier
```

The exact formula remains an implementation/balance decision, but the architecture must preserve the distinction between **base value** and **dynamic market state**.

---

## 12. Remote Settlement Premiums and Contracts

Small or isolated settlements may have higher delivered willingness-to-pay for scarce or critical cargoes because alternatives are limited.

This is distinct from OpenTTD's existing subsidy system.

Supported mechanisms may include:

- normal market scarcity premium;
- explicit delivery contracts;
- public-service support;
- strategic resource-development incentives;
- emergency procurement;
- temporary event premiums.

A small population should still impose a demand ceiling. High unit value does not mean unlimited volume.

Informal/scarcity premiums may represent exceptional local markets without requiring a literal bribery mechanic.

---

## 13. Industry Capacity and Investment

Industries have a productive capacity that can expand or contract.

Expansion may require:

- Construction Materials;
- Machinery;
- Industrial Equipment;
- Technology Systems;
- Personnel;
- capital/investment;
- time.

Industry state may include:

```text
healthy
strained
starved
profitable
unprofitable
damaged
idle
expanding
contracting
```

The model should permit profitable demand to attract capacity over time without making growth instantaneous.

---

## 14. Labor and Personnel

Personnel remains distinct from Passengers.

Personnel is a productive labor flow and may be required according to:

- industry;
- scale;
- technology;
- automation;
- labor intensity;
- era.

Automation should generally reduce labor intensity rather than require a new cargo identity.

Returning Personnel remains a flow/state adapter concept unless a specific implementation requires a distinct cargo.

---

## 15. Transportation Network Adaptation

The transportation network is the player's response layer.

Economic changes may require the player to:

- add capacity;
- reroute cargo;
- build feeder routes;
- consolidate routes;
- add passenger/personnel service;
- develop ports/hubs;
- abandon obsolete infrastructure;
- repurpose existing corridors;
- diversify markets.

The economy does not prescribe a solution.

> **The player does not control the economy. The player builds the transportation system that responds to it — and can influence it.**

### Network resilience

A network may be evaluated by:

- utilization;
- redundancy;
- cargo diversity;
- destination diversity;
- economic dependency;
- alternate routing;
- geographic exposure.

These are strategic characteristics, not necessarily player-facing scores.

---

## 16. Causal Records

Important state changes should retain machine-readable causes.

Example:

```json
{
  "metric":"steel_production",
  "change":-0.27,
  "causes":[
    {"factor":"coke_shortage","contribution":-0.11},
    {"factor":"iron_shortage","contribution":-0.08},
    {"factor":"labor_shortage","contribution":-0.04},
    {"factor":"maintenance_deficit","contribution":-0.04}
  ]
}
```

This supports:

- player explanation;
- debugging;
- balancing;
- AI reasoning;
- scenario analysis;
- replay/audit.

---

## 17. AI Policy Boundary

The in-game economic AI may:

- observe economic state;
- identify bottlenecks;
- estimate likely consequences;
- propose policy changes;
- apply permitted bounded adjustments;
- record decisions and outcomes.

The AI may **not**:

- rewrite canonical economy definitions during play;
- create unbounded resources;
- bypass policy bounds;
- silently change historical identity;
- create mandatory dependencies that do not exist in the canonical model.

Conceptual loop:

```text
OBSERVE
   ↓
ANALYZE
   ↓
PROPOSE
   ↓
APPROVE / POLICY CHECK
   ↓
APPLY
   ↓
RECORD
   ↓
EVALUATE
```

AI adjustments must be reversible.

Each applied adjustment should retain:

```text
previous value
new value
scope
reason
source/authority
timestamp
duration or expiry
```

---

## 18. Scenario Contract

A scenario is a package of starting conditions and/or event schedules. It does not fork the canonical economy merely to change conditions.

A scenario may define:

- starting year;
- enabled modules;
- difficulty profile;
- initial world state;
- regional conditions;
- starting resource knowledge;
- scheduled events;
- scripted objectives;
- victory/failure conditions.

Scenarios may reuse the same event definitions and policy definitions.

---

## 19. Module Boundary

Advanced systems remain modular.

Potential modules include:

- recycling;
- finance;
- advanced technology;
- research;
- global trade;
- environmental effects;
- alternative energy;
- future/space economy.

A module must declare dependencies and must not silently make itself mandatory to the core historical economy.

---

## 20. v0.4 Frozen Feature Wishlist

The following are **in scope as architectural capabilities**:

- [x] Date-gated historical industry progression
- [x] Moderately interconnected production chains
- [x] Materials processing layer
- [x] Operational supplies
- [x] Personnel flows
- [x] Industry succession
- [x] Modular economy definitions
- [x] Adjustable runtime production ratios
- [x] Runtime economic policy layer
- [x] Difficulty profiles
- [x] World-state model
- [x] Data-driven events/catastrophes
- [x] Dynamic demand
- [x] Dynamic pricing model
- [x] Resource depletion
- [x] Exploration/discovery
- [x] Settlement growth and shrinkage
- [x] Settlement specialization
- [x] Settlement economic pivots/transitions
- [x] Industry capacity/investment
- [x] Labor/Personnel economics
- [x] Transportation adaptation/resilience
- [x] Causal records
- [x] Scenario composition
- [x] AI policy boundary and reversible adjustments

### Explicitly frozen: no cargo expansion by default

The cargo vocabulary is considered sufficient for v0.4. New cargoes require a demonstrated missing economic relationship, not merely a real-world material that could be named separately.

### Explicitly deferred

The following may be future modules but are **not required to complete v0.4**:

- detailed banking/credit simulation;
- stock-market simulation;
- individual household simulation;
- full climate simulation;
- political simulation;
- detailed military logistics;
- detailed environmental chemistry;
- space economy;
- fully autonomous self-modifying AI.

---

## 21. Completion Criterion

Reference Economy v0.4 is architecturally complete when:

1. canonical definitions validate against their schemas;
2. every manifest entry resolves to a definition;
3. runtime policy can modify permitted parameters without editing canonical definitions;
4. events can modify world state through data;
5. resource depletion and discovery use bounded state transitions;
6. settlements can respond to economic conditions;
7. settlement transitions can create new transport demand;
8. transportation changes can feed back into economic conditions;
9. important state changes can be explained through causal records;
10. an AI can observe, propose, apply and reverse bounded policy changes;
11. scenarios and difficulty profiles can reuse the same underlying economy.

At that point, additional work should focus on **implementation, balance, testing and content**, not adding another foundational economic layer unless a concrete simulation gap is demonstrated.

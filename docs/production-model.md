# OpenTTD Economic Framework — Production Model

**Status:** Draft v0.1

## Purpose

This document defines how an industry's production should be calculated from its base capacity, production inputs, operational supplies, Personnel, technology, and other approved economic factors.

The production model exists to make industries deep enough to create logistics decisions while remaining understandable to players and reusable by economy designers.

## Core Principle

> **Production should be modified by logistics, not buried under logistics.**

The player should be able to understand why an industry is producing more or less without needing to inspect a dozen hidden variables.

## Production Layers

Production is conceptually divided into five layers:

```text
1. Base Production
       ↓
2. Production Inputs
       ↓
3. Operational Supply Service
       ↓
4. Personnel / Labor
       ↓
5. Technology + Approved Modifiers
       ↓
Effective Production
```

Not every industry needs every layer.

## 1. Base Production

Every productive industry has a base production level.

Base production answers:

> How much could this site produce under ordinary operating conditions before logistics bonuses and penalties are applied?

A properly functioning industry should generally be capable of some production without operational supplies.

```text
No supplies → base production
```

This is an important accessibility rule. Players should not be forced to construct an enormous supply network merely to make an industry function at all.

## 2. Production Inputs

Production inputs are materials directly involved in creating an output.

Example:

```text
Iron Ore + Coal
       ↓
   Steelworks
       ↓
     Steel
```

Production inputs are different from operational inputs.

### Production input states

An industry may use one of several models:

- Required input
- Proportional input
- Preferred input
- Alternative input
- Optional input

The framework should not assume that every industry uses the same rule.

## Required Inputs

A required production input is necessary for a particular production cycle.

Example:

```text
Iron Ore + Coal → Steel
```

If either is unavailable, steel production may stop or be reduced according to the industry's definition.

Required inputs should be used when the physical transformation would otherwise make little economic sense.

## Proportional Inputs

Production can scale with the amount of input delivered.

Conceptually:

```text
More usable input
      ↓
More production
```

This is useful for resource extraction and large processing industries where continuous supply matters.

## Alternative Inputs

Some industries may accept different inputs that perform a similar economic function.

Example:

```text
Coal OR another approved industrial energy source
              ↓
           Industry
```

Alternative inputs should be used sparingly. They are useful when they represent a genuine technological or historical substitution rather than simply making every chain interchangeable.

## 3. Operational Supply Service

Operational supplies improve an industry's productivity.

The reference framework uses three broad service levels:

| Service level | Conceptual result |
|---|---|
| None | Base production |
| Regular | Meaningful production bonus |
| Excellent | Maximum intended supply bonus |

A starting balancing target could be approximately:

```text
None      = 100% of base
Regular   = 115–125%
Excellent = 135–150%
```

These values are deliberately provisional. Gameplay testing determines the final numbers.

### Why bonuses instead of shutdowns?

The supply system should create a decision:

> Is the cost of supplying this industry worth the additional output?

That is more interesting than:

> Did I deliver one missing crate, yes or no?

## Supply Classes

The initial framework defines five operational supply classes:

1. Tools & Hardware
2. Industrial Equipment
3. Construction Materials
4. Agricultural Supplies
5. Technology Systems

Industries can use different combinations.

Example:

```text
Farm
  Tools & Hardware
  Agricultural Supplies

Mine
  Tools & Hardware
  Industrial Equipment

Factory
  Tools & Hardware
  Industrial Equipment
  Technology Systems

Shipyard
  Tools & Hardware
  Industrial Equipment
  Construction Materials

Offshore Platform
  Industrial Equipment
  Construction Materials
  Technology Systems
```

The purpose is not to make every industry consume all five classes.

## Supply Quality

Supply service should be evaluated over time rather than based solely on a single delivery.

Conceptually:

```text
No recent supply
      ↓
Low service
      ↓
Regular service
      ↓
Excellent sustained service
```

A reliable supply network should therefore outperform an occasional emergency delivery.

The implementation may use rolling service percentages, supply counters, monthly averages, or another mechanism. The economic framework only requires that service quality be measurable and interpretable.

## 4. Personnel / Labor

Personnel represents labor supplied to a productive site.

Personnel should be treated separately from ordinary passengers.

```text
Passengers
= people traveling

Personnel
= labor being supplied to production
```

Personnel can affect production in several ways:

- maintaining minimum staffing;
- providing a productivity bonus;
- enabling larger production capacity;
- supporting specialized or advanced industries.

The exact model can vary by industry.

## Personnel Service Levels

A simple model may use:

| Personnel service | Conceptual effect |
|---|---|
| Adequate | Normal operation |
| Well supplied | Improved productivity |
| Excellent | Maximum labor contribution |

Personnel should not automatically become another binary prerequisite for every industry.

The framework should preserve the distinction between:

```text
No Personnel
→ base or reduced operation, depending on industry

Personnel supplied
→ productive labor available

Returning Personnel
→ labor cycle can continue
```

## Returnable Personnel

Personnel creates an opportunity for productive round trips.

Example:

```text
Town / Personnel Source
        ↓
    Personnel
        ↓
      Mine
        ↓
Returning Personnel
```

A transport service might therefore carry:

```text
OUTBOUND
Personnel
Tools & Hardware
Industrial Equipment

RETURN
Coal
Returning Personnel
```

This should be a meaningful economic loop, not merely decorative passenger traffic.

## Personnel and Production Capacity

Personnel should generally scale with the productive capacity of a site.

A small industry should not require the same labor flow as a giant industrial complex.

Conceptually:

```text
Personnel Need ∝ Industry Scale × Labor Intensity
```

Automation can reduce labor intensity over time.

This provides a natural historical progression:

```text
Labor-intensive
      ↓
Mechanized
      ↓
Automated
      ↓
Highly autonomous
```

## 5. Technology Modifier

Technology represents the capability of the industry during its current historical period.

Technology can modify:

- production capacity;
- labor intensity;
- supply efficiency;
- energy requirements;
- output mix;
- storage requirements;
- geographic flexibility.

Technology should not simply be a universal multiplier applied to everything.

For example, automation might increase production while reducing Personnel demand.

## Recommended Formula

The framework should keep the production equation conceptually simple:

```text
Effective Production =
    Base Production
    × Input Factor
    × Supply Factor
    × Personnel Factor
    × Technology Factor
    × Approved Modifiers
```

Each factor should normally be normalized around `1.0`.

Example:

```text
Base Production       = 100
Input Factor           = 1.00
Supply Factor          = 1.20
Personnel Factor       = 1.00
Technology Factor      = 1.10
Other Modifiers        = 1.00

Effective Production = 132
```

The example is illustrative, not a locked balance value.

## Why Multipliers?

Multipliers make different economic factors composable.

They also make it easier for modules to add a modifier without rewriting the entire production equation.

However, modifiers should be bounded to prevent runaway production.

## Modifier Budget

A framework economy should avoid stacking unlimited bonuses.

Conceptually:

```text
Base
 ├─ Supplies
 ├─ Personnel
 ├─ Technology
 ├─ Geography
 └─ Special condition
       ↓
Bounded effective production
```

Each industry or module should document its maximum intended modifier contribution.

The framework should prefer a few meaningful modifiers over many tiny bonuses.

## Diminishing Returns

Supply systems may eventually benefit from diminishing returns.

For example:

```text
0% service       → 100% production
50% service      → meaningful improvement
80% service      → strong improvement
100% service     → excellent service
120% service     → little or no additional benefit
```

The exact curve is an implementation/balancing decision.

The important principle is that players should not need to flood an industry with supplies indefinitely to maximize profit.

## Production and Storage

Production should interact with storage without requiring perfect timing.

Conceptually:

```text
Inputs → Input Storage → Production → Output Storage → Transport
```

If output storage is full, the industry may reduce production or stop producing that output.

If input storage is empty, production may fall according to the input rule.

Storage therefore becomes part of the logistics problem.

## Production and Transport Reliability

A supply route should reward consistency.

An industry receiving regular deliveries should be more productive than one receiving occasional large deliveries if both provide the same average cargo but the first maintains better service continuity.

This creates an important distinction:

> **Capacity is not the same thing as service.**

A giant vehicle arriving occasionally may be less useful than smaller vehicles maintaining reliable service.

## Production Scaling

Industry scale should influence production without requiring completely different production systems.

Conceptually:

```text
Small site
  ↓
Low base production

Large site
  ↓
Higher base production
  ↓
Higher supply demand
  ↓
Higher Personnel demand
  ↓
Larger transport opportunity
```

Scaling creates a natural reason for players to upgrade infrastructure around successful industries.

## Production Growth

Production growth should be governed separately from instantaneous production modifiers.

For example:

```text
Production modifier
= how efficiently the industry operates now

Production growth
= how the industry's underlying capacity changes over time
```

A farm receiving excellent supplies today does not necessarily become permanently larger tomorrow.

Likewise, an industry can grow because of sustained demand, investment, technology, or historical development without receiving an immediate production bonus every month.

## Demand-Driven vs Supply-Driven Industries

Different industries can use different growth philosophies.

### Supply-driven

More input availability directly supports higher production.

Typical examples:

- Mines
- Farms
- Forestry
- Fishing

### Transformation-driven

Production is primarily limited by the availability of processing inputs.

Typical examples:

- Steelworks
- Food processors
- Refineries
- Factories

### Demand-sensitive

An industry may grow or shrink partly in response to downstream demand.

Potential examples:

- Manufacturing
- Construction materials
- Advanced technology
- Shipbuilding

The reference economy can use a mixture rather than forcing one universal model.

## Historical Production Evolution

Production mechanics should allow the same industry role to become more productive as technology advances.

Example:

```text
1700 Farm
  Low base production
  High Personnel intensity
  Limited supply bonus

1900 Mechanized Farm
  Higher base production
  Lower Personnel intensity
  Stronger Agricultural Supplies effect

2050 Automated Farm
  Very high base capacity
  Low Personnel intensity
  Strong Technology Systems effect
```

This makes historical progression visible through logistics rather than merely changing graphics.

## Energy as a Modifier

Energy can eventually be modeled as either a production input or operational input depending on the industry.

The framework should not make electricity a universal requirement unless gameplay demonstrates that it improves the economy.

Possible progression:

```text
Fuel / Steam
     ↓
Electricity
     ↓
Grid + Distributed Energy
     ↓
Renewables + Storage
     ↓
Advanced Energy Systems
```

Energy belongs in a future dedicated module/model rather than being hard-coded into every industry.

## Environmental and External Modifiers

Optional modules may introduce factors such as:

- resource depletion;
- pollution;
- climate conditions;
- congestion;
- disasters;
- environmental regulations;
- seasonal production.

These should be additive framework extensions, not mandatory complexity in the core model.

## Production Transparency

Players should be able to understand the major reasons for an industry's production state.

A useful interface should be able to communicate something equivalent to:

```text
Base Production:        100%
Production Inputs:      100%
Supply Service:         +20%
Personnel Service:      +0%
Technology:             +10%

Effective Production:   132%
```

Exact UI is outside this document, but the model should be inspectable.

## Balancing Principles

### 1. Base production must be viable

An unsupplied industry should still contribute to the economy.

### 2. Logistics should matter

Good service should produce a noticeable economic advantage.

### 3. Bonuses must not trivialize transport

Excellent supply service should reward investment without turning every industry into an infinite money printer.

### 4. Personnel should create logistics

Personnel should be economically meaningful without becoming a frustrating universal requirement.

### 5. Automation should change logistics

Later technology should not simply mean `+50% production`; it should change the types and quantities of transportation problems.

### 6. Complexity must earn its place

Every additional modifier should create a decision that players can understand and exploit.

## Anti-Patterns

Avoid:

- dozens of interacting multipliers with no visible explanation;
- production falling to zero because one supply shipment was missed;
- unlimited stacking of supply bonuses;
- treating Personnel exactly like Passengers;
- making every industry consume every supply class;
- forcing every era to use a completely different production equation;
- hidden modifiers that players cannot diagnose;
- using vehicles to determine production instead of economic demand determining vehicle choice.

## Framework Boundary

This document defines the production model conceptually. It does not yet define the exact NewGRF/NML implementation.

Implementation should preserve these principles while adapting them to the actual capabilities and limitations of the OpenTTD/NewGRF production system.

The framework should maintain a clear separation between:

```text
Economic definition
        ↓
Production model
        ↓
Implementation adapter
        ↓
NewGRF / OpenTTD behavior
```

This allows the economic model to remain reusable even when the implementation changes.

## Guiding Principle

> **Simple rules. Deep logistics.**
>
> Base production keeps the economy alive. Inputs make production possible. Supplies make it better. Personnel makes it work. Technology changes how the work gets done.

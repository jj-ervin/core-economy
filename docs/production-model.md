# OpenTTD Economic Framework — Production Model

**Status:** Draft v0.2

## Purpose

This document defines how production is calculated from base capacity, production inputs, operational-supply service, Personnel, technology, and other explicitly approved modifiers.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

## Production Layers

```text
Base Production
      ↓
Production Inputs
      ↓
Operational-Supply Service
      ↓
Personnel / Labor
      ↓
Technology and Approved Modifiers
      ↓
Effective Production
```

Not every industry needs every layer.

## Base Production

Every productive industry has a base production level. A properly functioning industry should generally produce something without operational supplies.

```text
No operational supplies → base production
```

This keeps the economy accessible while allowing reliable logistics to create meaningful advantages.

## Production Inputs

Production inputs are materials directly transformed into an output.

Canonical examples:

```text
Iron Ore + Coal → Steel Mill → Steel
Copper Ore → Copper Works → Copper
Oil → Refinery → Petroleum Products
Petroleum Products / defined feedstocks → Chemical Works → Chemicals
```

The framework distinguishes the following input relationships:

- `required` — necessary for the defined production cycle;
- `proportional` — delivered quantity scales production;
- `preferred` — favored input with a defined alternative or fallback;
- `alternative` — one member of an explicitly defined alternative group may satisfy the input requirement;
- `optional` — contributes when present but is not required;
- `supply` — operational service input, not an ordinary transformation input.

### Alternative-input rule

Do not write ambiguous `and/or` recipes. If an industry can use several interchangeable feedstocks, define an explicit group.

Example:

```text
Food Processing
  group: food_feedstock
  relationship: alternative
  members: Grain, Livestock, Fish
```

The validator must define whether the group requires at least one member, a specified number of members, or a proportional combination. The meaning must not be inferred from prose.

## Operational-Supply Service

Operational supplies improve productivity, capacity, reliability, efficiency, maintenance, expansion, or modernization. They are not universal hard prerequisites.

The current operational-supply vocabulary is:

1. Tools & Hardware
2. Industrial Equipment
3. Construction Materials
4. Agricultural Supplies
5. Technology Systems
6. Fuel
7. Chemicals

Fuel represents aggregated energy and movement support. Chemicals represents aggregated industrial and process chemicals, including relevant lubricants, coolants, solvents, reagents, and related materials. These identities should not be fragmented into separate cargoes unless a distinct transportation or gameplay decision requires it.

### Service levels

| Service level | Conceptual result |
|---|---|
| None | Base production |
| Regular | Meaningful production bonus |
| Excellent | Maximum intended supply bonus |

Provisional balancing target:

```text
None      = 100% of base
Regular   = 115–125%
Excellent = 135–150%
```

These values are not locked balance numbers and require playtesting.

Supply service should be evaluated over time. A consistent route should generally outperform an occasional emergency delivery with the same average volume.

### Supply relationships

An industry must explicitly declare which operational supplies it uses and what effect they have. The presence of a cargo in the global vocabulary does not make it mandatory for every industry.

Example:

```text
Farm
  Tools & Hardware
  Agricultural Supplies

Mine
  Tools & Hardware
  Industrial Equipment
  Fuel

Factory
  Tools & Hardware
  Industrial Equipment
  Technology Systems
  Chemicals

Port
  Fuel
  Industrial Equipment
  Construction Materials
```

## Personnel / Labor

Personnel is distinct from Passengers.

```text
Passengers = people traveling
Personnel  = labor being supplied to production
```

Personnel may support staffing, productivity, capacity, or specialized operations. It should not automatically become a binary prerequisite for every industry.

Personnel demand should eventually be machine-readable in terms of:

- industry scale;
- labor intensity;
- service level or staffing requirement;
- returnability;
- automation or technology effects;
- source and destination semantics.

Conceptually:

```text
Personnel Need ∝ Industry Scale × Labor Intensity
```

Automation can reduce labor intensity over time.

## Returnable Personnel

Personnel can create productive round trips:

```text
Town / Personnel Source
        ↓
    Personnel
        ↓
      Mine
        ↓
Returning Personnel
```

A route may carry Personnel, Tools & Hardware, Industrial Equipment, or Construction Materials outbound and return with a resource plus returning labor. Whether returning labor is implemented as a separate cargo or an adapter state is an implementation decision.

## Technology Modifier

Technology may modify:

- production capacity;
- labor intensity;
- supply efficiency;
- energy requirements;
- output mix;
- storage requirements;
- geographic flexibility.

Technology should not be a universal unexplained multiplier. Automation, for example, may increase capacity while reducing Personnel demand.

## Recommended Formula

```text
Effective Production =
    Base Production
    × Input Factor
    × Supply Factor
    × Personnel Factor
    × Technology Factor
    × Approved Modifiers
```

Factors should normally be normalized around `1.0`, and modifiers must be bounded to prevent runaway production.

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

## Storage and Reliability

Production interacts with storage:

```text
Inputs → Input Storage → Production → Output Storage → Transport
```

Empty input storage may reduce production according to the input relationship. Full output storage may reduce or stop production. The exact implementation belongs to the OpenTTD/NewGRF adapter.

Capacity is not the same thing as service. Large occasional deliveries should not automatically outperform smaller, reliable deliveries.

## Historical Evolution

Historical progression should change the logistics problem rather than merely apply a larger multiplier.

```text
Traditional Farm
  high labor intensity
  limited supply effects

Mechanized Farm
  higher capacity
  lower labor intensity
  stronger Agricultural Supplies effect

Automated Farm
  very high capacity
  low labor intensity
  stronger Technology Systems and Chemicals effects
```

Industry succession should not require a completely different production equation for every era.

## Boundaries

This document defines the conceptual production model. It does not define the exact NewGRF/NML implementation.

The intended separation is:

```text
Economic Definition
        ↓
Production Model
        ↓
Implementation Adapter
        ↓
NewGRF / OpenTTD Behavior
```

The adapter must preserve the economic meaning while respecting actual technical limitations.

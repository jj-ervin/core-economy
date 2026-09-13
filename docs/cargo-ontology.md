# OpenTTD Economic Framework — Cargo Ontology

**Status:** Draft v0.1

## Purpose

This document defines what a cargo is within the OpenTTD Economic Framework, how cargoes are classified, and which properties should remain consistent across industries, eras, and optional modules.

The goal is to give economy designers a common vocabulary without forcing every economy to use the same cargo roster.

## Core Principle

> **A cargo has a semantic role before it has a name.**

A cargo is not merely a label attached to a NewGRF cargo slot. It represents an economic thing that can participate in production, consumption, labor, communication, or financial logistics.

The framework should distinguish:

- **What something is economically** — its role.
- **What it is physically** — its represented material, people, goods, or documents.
- **Where it is useful** — its acceptance and production relationships.
- **When it exists** — its era and technology availability.

## Semantic Roles

The core ontology defines five roles.

### 1. PRIMARY_RESOURCE

Something extracted, harvested, caught, mined, pumped, or otherwise obtained from the environment.

Examples:

- Grain
- Livestock
- Timber
- Fish
- Coal
- Iron Ore
- Stone
- Clay
- Oil
- Gas
- Copper

A primary resource normally originates at an extraction or production site and becomes an input to another economic activity.

### 2. PRODUCT

Something created through processing, manufacturing, refinement, or other productive activity.

Examples:

- Food
- Lumber
- Steel
- Machinery
- Chemicals
- Manufactured Goods
- Electronics
- Advanced Goods

A product may itself become an input to another industry.

### 3. OPERATIONAL_INPUT

Something supplied to an industry to operate, maintain, expand, improve, or modernize productive capacity.

Initial framework classes:

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems

Operational inputs normally modify productivity rather than functioning as binary prerequisites.

### 4. HUMAN_FLOW

People transported as part of an economic or social movement.

Core human-flow cargoes:

- **Passengers** — people traveling because they want or need to reach a destination.
- **Personnel** — people transported because a productive site requires their labor.
- **Mail** — physical communication and parcels.

Passengers and Personnel are intentionally distinct. Personnel has an economic relationship with the destination: the destination needs workers.

### 5. FINANCIAL_FLOW

Physical financial objects transported because their physical movement has economic value or gameplay significance.

Possible examples:

- Gold
- Bullion
- Coin
- Cash
- Securities
- Financial Documents

Financial flows are optional. Systemic company money is not automatically a cargo.

## Cargo Identity

Every framework cargo should have a stable identifier separate from its display name.

Conceptual example:

```text
id: INDUSTRIAL_EQUIPMENT
name: Industrial Equipment
role: OPERATIONAL_INPUT
```

The identifier should remain stable even if the description, artwork, technology represented, or production relationships evolve.

This allows a cargo to survive historical transitions without requiring a new cargo merely because the underlying technology changed.

## Cargo Properties

A framework cargo may define the following properties.

| Property | Purpose |
|---|---|
| `id` | Stable machine-readable identity |
| `name` | Player-facing display name |
| `role` | Semantic economic role |
| `description` | Human-readable meaning |
| `mass_class` | Relative transportation weight |
| `volume_class` | Relative transportation space |
| `value_class` | Relative economic value |
| `perishability` | How quickly the cargo loses usefulness |
| `hazard_class` | Safety or handling requirements |
| `storage_class` | Storage requirements and constraints |
| `era_start` | Earliest intended availability |
| `era_end` | Optional end of availability |
| `technology_state` | Technology assumptions for the current era |
| `returnable` | Whether the cargo can meaningfully return to its source or another origin |
| `module` | Owning optional module or framework component |

Not every property must be exposed directly to players. Some exist to support consistent economic design.

## Stable Cargo, Evolving Technology

The framework prefers stable cargo identities where the economic role remains substantially the same.

For example:

```text
TOOLS_AND_HARDWARE

1700 → hand tools, simple hardware, replacement parts
1850 → machine tools and industrial maintenance equipment
1950 → precision tools and specialized hardware
2000 → advanced tools and maintenance components
2050 → automated tools and advanced service hardware
```

Likewise:

```text
TECHNOLOGY_SYSTEMS

Early era → electrical equipment and communications hardware
Industrial era → electrical control and instrumentation
20th century → electronics and computing systems
21st century → digital control, automation, robotics, AI systems
Future → advanced autonomous systems
```

The cargo identity remains stable while its historical representation changes.

## Cargo Is Not an Industry

A cargo represents something transported between economic locations.

An industry represents an economic activity or site that produces, consumes, transforms, employs, or otherwise interacts with cargo.

For example:

```text
IRON_ORE
    ↓
STEELWORKS
    ↓
STEEL
```

The cargo `IRON_ORE` is not the mine. The cargo `STEEL` is not the steelworks.

This separation is fundamental to modularity.

## Production and Acceptance Relationships

Cargoes participate in relationships rather than hard-coded universal rules.

A cargo may be:

- produced by one or more industries;
- consumed by one or more industries;
- transformed into another cargo;
- required as an operational input;
- accepted by cities or other economic destinations;
- associated with personnel demand;
- associated with a financial or logistics relationship.

Conceptual relationship vocabulary:

```text
PRODUCES
CONSUMES
TRANSFORMS
REQUIRES
EMPLOYS
ACCEPTS
TRANSPORTS
STORES
TRADES
```

The same cargo can participate in different relationships in different modules or eras.

## Personnel Semantics

Personnel is intentionally generic at the cargo level.

The destination provides context.

For example:

```text
Personnel → Coal Mine
= mining labor

Personnel → Offshore Platform
= offshore crew

Personnel → Shipyard
= shipbuilding labor

Personnel → Research Facility
= researchers / technical staff
```

The framework does not need separate cargoes for every profession.

### Returnability

Personnel may be marked as returnable.

Conceptually:

```text
PERSONNEL_SOURCE
      ↓
  PERSONNEL
      ↓
  WORKSITE
      ↓
RETURNING_PERSONNEL
```

Whether the implementation uses one cargo identity or an explicit returned state is an implementation decision. The economic model must preserve the concept that labor can make a productive trip and subsequently leave the worksite.

## Operational Input Semantics

Operational inputs should remain broad enough to create useful logistics decisions without producing dozens of nearly identical cargoes.

For example, the framework may use:

```text
TOOLS_AND_HARDWARE
INDUSTRIAL_EQUIPMENT
CONSTRUCTION_MATERIALS
AGRICULTURAL_SUPPLIES
TECHNOLOGY_SYSTEMS
```

An industry can specify which supply classes improve its productivity.

Example:

```text
Coal Mine
  Tools & Hardware      → productivity support
  Industrial Equipment  → productivity support

Farm
  Tools & Hardware       → productivity support
  Agricultural Supplies  → productivity support

Factory
  Tools & Hardware       → productivity support
  Industrial Equipment   → productivity support
  Technology Systems     → modernization / productivity support
```

The framework should resist splitting these into highly specialized cargoes unless the distinction creates a meaningful transportation decision.

## Era Availability

A cargo can have an earliest and optional latest intended era.

Date gating should normally describe **when the cargo becomes available for new economic activity**, not automatically destroy or invalidate existing cargo flows.

Cargo availability should be coordinated with industry succession.

Example:

```text
Traditional agricultural supplies
        ↓
Industrial agricultural supplies
        ↓
Precision agricultural systems
```

If these can be represented economically by the same cargo role, the framework should prefer a stable cargo identity with changing technology representation.

## Optional Modules

The core ontology should remain small. Additional modules may define additional cargoes using the same role system.

Possible modules include:

- Agriculture
- Forestry
- Heavy Industry
- Maritime
- Offshore
- Energy
- Chemicals
- Global Logistics
- Recycling
- Finance
- Advanced Technology
- Space

A module owns its cargo definitions and documents its relationships with other modules.

## Compatibility and Namespacing

Independent modules should avoid ambiguous cargo identities.

Conceptually:

```text
CORE:PERSONNEL
CORE:MAIL
CORE:TOOLS_AND_HARDWARE
OFFSHORE:OFFSHORE_EQUIPMENT
FINANCE:BULLION
SPACE:LAUNCH_VEHICLE
```

A final implementation may use a different technical namespace, but the principle is the same: ownership and identity should be explicit.

Modules should document:

1. which cargoes they introduce;
2. which existing cargoes they consume or produce;
3. which cargoes they modify or extend;
4. which era they target;
5. which optional dependencies they require.

This improves conceptual compatibility even where NewGRF technical limitations still require careful integration.

## Core vs Optional Cargoes

The reference framework should have a small core vocabulary.

Likely core cargoes include:

```text
PRIMARY_RESOURCE
  Grain
  Timber
  Fish
  Coal
  Iron Ore
  Stone
  Oil

PRODUCT
  Food
  Lumber
  Steel
  Machinery
  Manufactured Goods

OPERATIONAL_INPUT
  Tools & Hardware
  Industrial Equipment
  Construction Materials
  Agricultural Supplies
  Technology Systems

HUMAN_FLOW
  Passengers
  Personnel
  Mail
```

Additional cargoes should be added when they create a meaningful economic or transportation relationship.

## Anti-Patterns

Avoid the following unless a specific gameplay purpose justifies them.

### Era duplication

Do not create separate cargoes merely because the technology changed if the economic role is still the same.

Bad:

```text
STEAM_TOOLS
ELECTRIC_TOOLS
DIGITAL_TOOLS
AI_TOOLS
```

Prefer a stable economic identity where practical:

```text
TOOLS_AND_HARDWARE
```

### Profession explosion

Do not create separate Personnel cargoes for every occupation merely to provide flavor.

Bad:

```text
MINERS
ENGINEERS
TECHNICIANS
SCIENTISTS
OFFSHORE_CREW
```

Prefer:

```text
PERSONNEL
```

with destination context defining the labor relationship.

### Supply fragmentation

Do not create dozens of small supply cargoes when a broader operational-input class produces the same logistics decision.

### Financial overreach

Do not require physical money transport to represent ordinary monetary transactions. Financial cargoes should exist only where physical financial logistics adds gameplay.

### Cargo as industry

Do not encode an industry into the cargo definition. Keep production sites and transported things conceptually separate.

## Design Test for New Cargoes

Before adding a cargo, ask:

1. What semantic role does it have?
2. What economic relationship does it create?
3. What industry produces it?
4. What industry or destination needs it?
5. What transportation decision does it create?
6. Does an existing cargo already represent the same economic role?
7. Does the distinction matter to gameplay?
8. What era does it belong to?
9. Which module owns it?
10. Can another economy use the same semantic definition?

If the answer to the transportation/gameplay question is weak, the cargo probably does not belong in the framework.

## Guiding Principle

> **Define cargoes by economic meaning, not by the number of boxes they occupy.**
>
> Keep identities stable. Let industries, eras, geography, and technology provide the depth.

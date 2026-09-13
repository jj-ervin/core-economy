# OpenTTD Economic Framework — Cargo Ontology

**Status:** Draft v0.2

## Purpose

This document defines what a cargo is within the OpenTTD Economic Framework, how cargoes are classified, and which properties remain stable across industries, eras, and optional modules.

The framework provides a common vocabulary without requiring every economy to use the same cargo roster.

## Core Principle

> **Cargo identity and economic role are related, but they are not always identical.**

A cargo is a stable transported economic identity. Its economic role or roles describe how it participates in the economy.

A cargo definition must distinguish:

- what the cargo is economically;
- what it represents physically;
- where it is produced, consumed, accepted, or transported;
- when it is available;
- which module owns or extends it.

## Cargo Classes

The machine-readable contract uses a `classes` array. A cargo may have more than one class when one stable cargo identity legitimately participates in multiple economic roles.

Approved classes are:

- `primary` — extracted, harvested, caught, mined, pumped, or otherwise obtained from the environment;
- `product` — created through processing, refinement, or manufacturing;
- `operational_supply` — delivered to improve productivity, capacity, reliability, efficiency, maintenance, expansion, or modernization;
- `human_flow` — passengers, personnel, mail, or another explicitly defined human/economic flow;
- `financial` — an optional physical financial flow such as bullion or securities;
- `optional` — an availability or module designation, never a substitute for a semantic economic role.

Example:

```json
{
  "id": "chemicals",
  "name": "Chemicals",
  "classes": ["product", "operational_supply"]
}
```

This means that Chemicals is manufactured as a product and may also be delivered as an operational supply. It remains one cargo identity and must not create duplicate cargo slots merely because it has multiple classes.

## Multi-Role Cargo Rules

1. `classes` is required and must contain at least one value.
2. Values in `classes` must be unique.
3. Every value must be an approved class.
4. Multiple classes describe one stable cargo identity.
5. A multi-role cargo must not receive duplicate IDs, duplicate transport slots, or duplicated production relationships solely because it has multiple classes.
6. Each production, consumption, supply, human-flow, or financial relationship must be compatible with at least one declared class.
7. `optional` may be combined with a semantic class, but it must not be the only class when the cargo participates in a defined economic relationship.
8. A class does not automatically create a production recipe. Relationships must be explicitly defined by industries, recipes, endpoints, or modules.

## Canonical Cargo Examples

### Primary resources

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
- Copper Ore

### Products

- Food
- Lumber
- Steel
- Copper
- Petroleum Products
- Machinery
- Chemicals
- Manufactured Goods
- Electronics
- Advanced Goods

### Operational supplies

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems
- Fuel
- Chemicals

Chemicals intentionally appears in both the product and operational-supply lists because its identity supports both roles.

## Cargo Identity

Every cargo must have a stable machine-readable identifier separate from its display name.

```json
{
  "id": "industrial_equipment",
  "name": "Industrial Equipment",
  "classes": ["operational_supply"]
}
```

The identifier should remain stable even if artwork, technology representation, or production relationships evolve.

A change in technology does not automatically justify a new cargo. For example, hand tools, machine tools, precision tools, and automated tools may remain represented by `tools_and_hardware` when they create the same economic and transportation decision.

## Cargo Properties

A cargo may define:

| Property | Purpose |
|---|---|
| `id` | Stable machine-readable identity |
| `name` | Player-facing display name |
| `classes` | One or more approved economic roles |
| `description` | Human-readable meaning |
| `mass_class` | Relative transportation weight |
| `volume_class` | Relative transportation space |
| `value_class` | Relative economic value |
| `perishability` | How quickly usefulness declines |
| `hazard_class` | Safety or handling requirements |
| `storage_class` | Storage requirements and constraints |
| `introduced` | Earliest intended availability |
| `era_end` | Optional end of availability |
| `technology_state` | Historical technology representation |
| `returnable` | Whether the cargo can meaningfully return |
| `module` | Owning optional module or framework component |

Not every property must be exposed directly to players. Some exist to support consistent design and validation.

## Production and Acceptance Relationships

Cargoes participate in explicit relationships rather than universal hard-coded rules. A cargo may be:

- produced by one or more industries;
- consumed by one or more industries;
- transformed into another cargo;
- delivered as an operational supply;
- accepted by towns or other destinations;
- associated with personnel demand;
- associated with financial or logistics relationships;
- stored, traded, or transported by specialized facilities.

The framework recognizes relationship concepts such as:

```text
PRODUCES
CONSUMES
TRANSFORMS
REQUIRES
SUPPLIES
EMPLOYS
ACCEPTS
TRANSPORTS
STORES
TRADES
```

The same cargo may participate in different relationships in different modules or eras, provided those relationships remain explicit and valid.

## Operational Supply Semantics

Operational supplies normally modify service quality or productivity rather than acting as universal binary prerequisites.

The framework currently recognizes these broad supply identities:

```text
TOOLS_AND_HARDWARE
INDUSTRIAL_EQUIPMENT
CONSTRUCTION_MATERIALS
AGRICULTURAL_SUPPLIES
TECHNOLOGY_SYSTEMS
FUEL
CHEMICALS
```

Their historical representation may evolve without requiring separate cargoes for every lubricant, solvent, coolant, fertilizer, seed, reagent, or maintenance component.

Examples:

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

An operational-supply class does not by itself mean that every industry consumes that cargo. Each industry must declare its own supply relationships and effects.

## Human-Flow Semantics

The core human-flow identities are:

- **Passengers** — people traveling because they want or need to reach a destination;
- **Personnel** — people transported because a productive site requires labor;
- **Mail** — physical communication and parcels.

Personnel is contextual. The destination determines whether the flow represents miners, offshore crew, shipyard workers, researchers, or another workforce. The framework should not create profession-specific cargoes merely for flavor.

Personnel may be returnable. Whether the implementation uses one cargo identity or an explicit returned state is an adapter decision, but the economic model must preserve the possibility of productive round trips.

## Financial-Flow Semantics

Financial cargoes are optional physical flows whose movement creates meaningful gameplay, such as:

- Gold
- Bullion
- Coins or Cash
- Securities or Financial Documents

Systemic company money is not automatically represented as cargo.

## Era Availability

Cargo availability should describe when a cargo becomes available for new economic activity. It should not automatically destroy existing flows when a successor industry or technology appears.

Stable cargo identities are preferred when the underlying economic role remains substantially the same. Historical change should usually be represented through industry succession, technology state, production modifiers, geography, or logistics requirements.

## Modules and Namespacing

Optional modules may introduce cargoes using the same contract. Modules must document:

1. cargoes they introduce;
2. existing cargoes they consume or produce;
3. cargoes they modify or extend;
4. target eras;
5. dependencies on other modules;
6. whether their relationships are optional or core.

Conceptual namespacing may look like:

```text
CORE:PERSONNEL
CORE:MAIL
CORE:TOOLS_AND_HARDWARE
OFFSHORE:OFFSHORE_EQUIPMENT
FINANCE:BULLION
SPACE:LAUNCH_VEHICLE
```

The technical implementation may use another namespace, but ownership and identity must remain explicit.

## Core vs Optional Cargoes

The core economy should remain compact. Optional modules may add depth, but they must create meaningful economic, geographic, historical, or transportation decisions.

A cargo should not be added merely because it can be represented technically.

## Anti-Patterns

Avoid:

- using singular `class` or `role` in new machine-readable cargo definitions;
- using `OPERATIONAL_INPUT` when the current contract is `operational_supply`;
- creating duplicate cargoes for multiple classes;
- treating `optional` as a semantic economic role;
- creating separate cargoes for every technological era;
- creating profession-specific Personnel cargoes;
- fragmenting broad supplies into dozens of near-identical cargoes;
- requiring physical money transport to represent ordinary monetary transactions;
- encoding an industry into a cargo definition;
- adding a cargo without a meaningful economic or transportation decision.

## Design Test for New Cargoes

Before adding a cargo, ask:

1. What stable identity does it represent?
2. Which approved class or classes apply?
3. What economic relationship does it create?
4. What produces it?
5. What consumes, accepts, or uses it?
6. What transportation decision does it create?
7. Does an existing cargo already represent the same decision?
8. What era and module own it?
9. Is `optional` merely describing availability, rather than replacing a semantic class?
10. Can the relationship be validated without inventing hidden rules?

## Guiding Principle

> **Define cargoes by economic meaning, not by the number of boxes they occupy.**
>
> Keep identities stable. Let industries, eras, geography, technology, and explicit relationships provide the depth.

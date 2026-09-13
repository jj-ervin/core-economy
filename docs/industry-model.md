# OpenTTD Economic Framework — Industry Model

**Status:** Draft v0.1

## Purpose

The industry model defines how productive sites behave within the OpenTTD Economic Framework.

An industry is an economic activity located somewhere in the world. It may extract resources, transform materials, manufacture products, consume operational inputs, employ Personnel, generate transport demand, and respond to geography and technology.

The model is deliberately broader than a simple `input → output` chain. The objective is to create industries that generate useful transportation problems without making every industry needlessly complicated.

## Core Principle

> **Every productive site should create both a need and an opportunity.**

A player should be able to look at an industry and understand:

1. What does this site need?
2. What does this site produce?
3. Who or what must reach the site for it to operate well?
4. What can leave the site on the return journey?
5. How does geography affect the best way to serve it?

## Industry Identity

Every industry should have a stable identity independent of its current technology state or display name.

Conceptual example:

```text
id: COAL_MINE
name: Coal Mine
family: MINING
```

A later successor may represent the same economic activity with a different industry identity or an explicitly linked successor relationship:

```text
TRADITIONAL_COAL_MINE
    ↓
MECHANIZED_COAL_MINE
    ↓
AUTOMATED_EXTRACTION_SITE
```

The framework should distinguish between:

- **economic identity** — what the site does;
- **technology state** — how it does it;
- **era state** — when that technology is available;
- **physical location** — where it operates.

## Industry Components

A framework industry may define:

| Component | Meaning |
|---|---|
| `id` | Stable industry identity |
| `name` | Player-facing name |
| `family` | Economic family/module |
| `inputs` | Cargoes consumed or transformed |
| `outputs` | Cargoes produced |
| `operational_inputs` | Supplies that improve operation |
| `personnel_demand` | Labor requirement or productivity relationship |
| `location_rules` | Geographic placement constraints |
| `era_start` | Earliest construction/availability date |
| `era_end` | Optional end of new construction |
| `technology_state` | Current technological representation |
| `base_production` | Output without operational supplies |
| `productivity_modifiers` | Factors that alter production |
| `storage` | Input/output holding capacity |
| `successors` | Later industry forms |
| `predecessors` | Earlier industry forms |
| `module` | Owning optional module |

Not every industry needs every field exposed directly to players.

## Industry Roles

An industry can perform one or more economic roles.

### Extraction

Obtains primary resources from the environment.

Examples:

- Farm → Grain, Livestock
- Forest → Timber
- Coal Mine → Coal
- Iron Mine → Iron Ore
- Oil Field → Oil
- Fishing Harbor → Fish

### Processing

Transforms one or more inputs into intermediate or finished products.

Examples:

```text
Grain → Flour
Flour + Grain → Food
Iron Ore + Coal → Steel
Timber → Lumber
Oil → Refined Fuels / Chemicals
```

### Manufacturing

Combines processed materials, products, and operational inputs to create manufactured goods or equipment.

Examples:

```text
Steel + Lumber + Industrial Equipment
              ↓
          Machinery
```

### Infrastructure / Supply Production

Produces operational inputs used by other industries.

Examples:

```text
Iron + Timber + Coal
        ↓
Engineering Works
        ↓
Tools & Hardware
Industrial Equipment
```

### Service / Logistics

Some economic sites primarily exist to support movement, storage, distribution, communication, finance, or other economic activity.

Examples may include:

- Warehouses
- Distribution centers
- Ports
- Banks
- Financial centers
- Research facilities

These may have different production rules from conventional resource industries.

## Inputs and Outputs

An industry should explicitly describe the cargo relationships that matter to it.

A simple industry may be:

```text
IRON_ORE
   ↓
STEELWORKS
   ↓
STEEL
```

A deeper industry can combine several inputs:

```text
IRON_ORE + COAL + INDUSTRIAL_EQUIPMENT + PERSONNEL
                         ↓
                    STEELWORKS
                         ↓
                       STEEL
```

The framework does not require every listed input to be a hard prerequisite.

## Hard Inputs vs Productivity Inputs

This distinction is central.

### Production inputs

Materials directly transformed into the output.

Example:

```text
Iron Ore + Coal → Steel
```

If the industry cannot obtain the necessary production input, its ability to produce that output may fall or stop according to the industry's specific design.

### Operational inputs

Supplies that improve the industry's ability to operate.

Example:

```text
Steelworks
  Tools & Hardware
  Industrial Equipment
  Technology Systems
```

These normally modify productivity rather than functioning as an on/off switch.

This distinction prevents the economy from becoming a giant dependency tree where every missing box causes an industry to shut down.

## Supply Service

Operational inputs are evaluated as a service level.

Conceptual baseline:

```text
No supplies
    ↓
Base production

Regular supply service
    ↓
Improved production

Excellent supply service
    ↓
Maximum intended productivity
```

The exact numerical modifiers are a balancing parameter, not a framework constant.

Different industries may have different supply priorities or combinations.

## Personnel Demand

Personnel is a distinct economic flow.

A productive site may require workers to maintain its normal production or achieve higher productivity.

Example:

```text
Personnel Source
      ↓
   Personnel
      ↓
    Mine
      ↓
 Returning Personnel
```

Personnel should not automatically be treated as ordinary passengers.

### Personnel is contextual

The cargo remains `PERSONNEL`; the destination determines the labor relationship.

```text
Personnel → Mine
Personnel → Factory
Personnel → Shipyard
Personnel → Offshore Platform
Personnel → Research Facility
```

This avoids a proliferation of profession-specific cargoes.

### Personnel is potentially returnable

A worksite can produce a return opportunity after a work period or assignment.

The economic model should permit:

```text
Town / Personnel Source
        ↓
    Personnel
        ↓
     Worksite
        ↓
Returning Personnel
```

Implementation details may vary, but the economic concept should remain explicit.

## Productive Trips

An industry should be designed with transportation loops in mind.

For each industry, designers should consider:

```text
What arrives?
What happens there?
What leaves?
Who needs to arrive?
Who can return?
```

Example mine service:

```text
OUTBOUND
Personnel
Tools & Hardware
Industrial Equipment
        ↓
      Mine
        ↓
RETURN
Coal
Returning Personnel
```

This does not mean every trip must be perfectly balanced. Some industries naturally produce asymmetric flows.

The objective is to create opportunities for useful return cargo where economically plausible.

## Production Capacity

An industry should separate its base production from its productivity modifiers.

Conceptually:

```text
Effective Production =
    Base Production
    × Supply Modifier
    × Personnel Modifier
    × Technology Modifier
    × Other Approved Modifiers
```

The exact formula belongs in the production model and should not be duplicated independently by every industry.

The industry definition supplies the parameters; the framework supplies the interpretation.

## Geography

Industries should interact with physical geography rather than being placed arbitrarily.

Examples:

| Industry | Geographic preference |
|---|---|
| Farm | Suitable agricultural land |
| Forest | Forested terrain |
| Mine | Appropriate mineral terrain / deposits |
| Fishing Harbor | Coast / navigable water |
| Shipyard | Coast / navigable water |
| Oil Field | Appropriate land or offshore zone |
| Offshore Platform | Offshore access |
| Quarry | Stone-bearing terrain |
| Port | Coast / navigable water and inland access |
| Research Facility | Often urban or infrastructure-connected |

Geography should create transportation choices rather than merely restrict construction.

## Location as an Economic Variable

The same industry can have different logistics depending on where it is built.

A remote mine may require:

- longer rail or road service;
- larger supply deliveries;
- personnel transport;
- specialized vehicles;
- nearby staging facilities.

A mine near a major rail corridor may be much easier to serve but potentially less strategically valuable.

Location therefore affects the economics of serving an industry.

## Storage

Industries should have meaningful input and output storage.

Storage prevents production from requiring perfect synchronization while still rewarding reliable service.

Conceptually:

```text
Input storage
     ↓
  Production
     ↓
Output storage
```

Storage can create additional logistics decisions:

- large bulk storage near mines;
- refrigerated storage for perishables;
- tanks for liquids;
- warehouses for manufactured goods;
- secure storage for financial cargoes.

Storage should not become an unnecessary simulation of individual inventory units.

## Industry Size

Industries may vary in scale.

Possible conceptual classes:

- Small
- Medium
- Large
- Major
- Complex / Mega-site

Size can influence:

- base production;
- storage capacity;
- personnel demand;
- supply demand;
- transport frequency;
- geographic footprint.

Size should affect logistics, not merely provide a cosmetic label.

## Technology State

An industry's technology state describes how the industry currently performs its economic role.

For example:

```text
FARM

1700–1850
Traditional / labor-intensive

1850–1950
Mechanized

1950–2000
Industrialized

2000–2050
Precision agriculture

2050+
Automated / autonomous agriculture
```

Technology can affect:

- production capacity;
- supply requirements;
- personnel requirements;
- energy use;
- output mix;
- environmental footprint;
- transport requirements.

Technology should not automatically invalidate older industries.

## Date-Gated Succession

New industries can appear as technology and economic conditions change.

Existing industries should generally continue operating unless the design explicitly calls for closure or conversion.

Conceptual sequence:

```text
Traditional Farm
      ↓ overlap
Mechanized Farm
      ↓ overlap
Precision Farm
      ↓ overlap
Automated Farm
```

The overlap is intentional. Real economies contain multiple generations of productive technology at the same time.

## Construction vs Operation

Date gating should distinguish between:

- when an industry can be newly constructed;
- when an industry operates;
- when an industry becomes less likely to appear;
- when an industry can be upgraded or replaced.

A successor appearing in 1950 should not imply that every predecessor disappears on January 1, 1950.

This allows the world to develop historically rather than reset itself whenever the calendar changes.

## Industry Families

Industries should belong to broad families so modules can be organized without requiring a single giant economy.

Initial families:

- Agriculture & Food
- Forestry & Wood
- Mining & Minerals
- Energy & Fuels
- Manufacturing
- Chemicals & Materials
- Fisheries & Aquaculture
- Maritime & Shipbuilding
- Offshore Industry
- Construction & Infrastructure
- Cities & Services
- Logistics & Distribution
- Communications & Information
- Electricity & Energy Systems
- Automation & Technology
- Advanced / Space Industry

Families are organizational concepts. They do not automatically determine cargo relationships.

## Modular Industries

A module should be able to introduce an industry without rewriting the core framework.

Example:

```text
OFFSHORE MODULE

Offshore Supply Base
    ↓
Offshore Supply Vessel
    ↓
Offshore Oil Platform
    ↓
Oil / Gas
```

Another module might add offshore wind:

```text
Component Factory
    ↓
Offshore Equipment
    ↓
Construction Port
    ↓
Heavy-Lift Vessel
    ↓
Offshore Wind Farm
    ↓
Electricity
```

The modules share the same cargo and industry concepts.

## Industry Lifecycle

An industry can move through a lifecycle:

```text
NOT_AVAILABLE
      ↓
INTRODUCED
      ↓
GROWING
      ↓
MATURE
      ↓
DECLINING
      ↓
NO_NEW_CONSTRUCTION
```

This is a design model, not necessarily a literal implementation state machine.

An industry may remain operational after reaching `NO_NEW_CONSTRUCTION`.

## Industry Evolution Examples

### Agriculture

```text
Traditional Farm
  Grain + Livestock
       ↓
Mechanized Farm
  Grain + Livestock
  ↑ improved with Agricultural Supplies
       ↓
Precision / Automated Farm
  Grain + specialized outputs
  ↑ improved with Technology Systems
```

### Forestry

```text
Forest
  ↓ Timber
Sawmill
  ↓ Lumber
Manufacturing
  ↓ Manufactured Goods
```

The sawmill can evolve from a small local operation into a large industrial facility without requiring the cargo identity `TIMBER` to change.

### Steel

```text
Iron Ore + Coal
        ↓
Foundry / Early Steelworks
        ↓
Steel
        ↓
Industrial Manufacturing
```

Later steelworks can consume more Industrial Equipment and Technology Systems while retaining the same core economic role.

## Industry Design Checklist

Before adding an industry, answer:

1. What economic role does it perform?
2. What does it consume?
3. Which inputs are true production inputs?
4. Which inputs are operational supplies?
5. Does it need Personnel?
6. Can Personnel return?
7. What does it produce?
8. What can be carried away?
9. What geography does it prefer?
10. What storage does it need?
11. What transportation problem does it create?
12. When can it appear?
13. What happens to it when successor technology appears?
14. Which module owns it?
15. Does adding it create meaningful gameplay rather than just another cargo chain?

## Anti-Patterns

### Everything is a hard prerequisite

Avoid chains where one missing supply shuts down an entire economy.

### New replaces old instantly

Avoid deleting historical industries simply because a newer technology becomes available.

### Industry without logistics

Avoid industries whose inputs and outputs do not create meaningful transportation decisions.

### Cargo explosion

Avoid adding a new cargo whenever a new industry needs a slightly different flavor of an existing material.

### Vehicle-first design

Do not design an industry merely to give a particular vehicle something to carry.

The economic need comes first. Vehicles are selected to solve the resulting transportation problem.

## Framework Rule

An industry definition should describe **what the economic site does**. The framework should determine how that site interacts with cargo, supplies, personnel, production, time, and geography.

This keeps the economy extensible while allowing individual industries to remain understandable.

## Guiding Principle

> **An industry is not a box that makes cargo. It is a place where economic activity happens.**
>
> Give it a reason to exist, something it needs, something it produces, people who make it work, and a location that makes serving it interesting.

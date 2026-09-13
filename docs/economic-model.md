# OpenTTD Economic Framework — Economic Model

**Status:** Draft v0.1

## Purpose

A reusable framework for designing modular, evolving economies for OpenTTD. The framework defines economic roles and relationships rather than prescribing one fixed industry list. The 1700–2150 economy is the first reference implementation.

## Design Philosophy

### Simple rules, deep logistics

Create strategic depth through relationships between industries, locations, transportation modes, supplies, personnel, and production—not by requiring players to memorize enormous numbers of cargoes.

### The economy comes first

Vehicles serve economic needs. A vehicle is valuable when it solves a transportation problem efficiently, not simply because it is newer or faster.

### Every productive site creates a demand and an opportunity

A productive site generally needs resources, supplies, equipment, personnel, or other inputs; performs an economic activity; and produces something valuable that can be transported elsewhere.

## Economic Roles

### Primary Resources

Resources extracted, harvested, caught, mined, pumped, or otherwise obtained from the environment.

Examples: Grain, Livestock, Timber, Fish, Coal, Iron Ore, Stone, Clay, Oil, Gas, Copper.

### Products

Materials or goods created by processing or manufacturing.

Examples: Food, Lumber, Steel, Machinery, Chemicals, Manufactured Goods, Electronics, Advanced Goods.

### Operational Inputs

Materials, equipment, and systems used by an industry to operate more effectively, maintain itself, expand, or modernize.

Initial reference categories:

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems

Operational inputs generally improve productivity rather than acting as binary on/off requirements.

### Human/Economic Flows

- **Passengers:** people traveling because they want or need to go somewhere.
- **Personnel:** people transported to a productive worksite because the site needs their labor.
- **Mail:** letters, documents, parcels, and later forms of express physical communication.

Personnel is a distinct cargo type, not a passenger subtype.

### Financial Flows

Optional physical financial cargoes such as Gold, Bullion, Coin, Cash, Securities, and Financial Documents. The monetary system itself should normally remain systemic rather than requiring money to be physically transported.

## Industry Model

An industry may have inputs, operational inputs, personnel demand, outputs, location constraints, era availability, technology state, storage capacity, production rate, and productivity modifiers.

A minimal industry can transform an input into an output. More sophisticated industries may combine resources, operational inputs, personnel, technology, and geography.

## Production Model

### Base production

An industry operates at base production even when it receives no operational supplies.

**No supplies → base production.**

### Supply service levels

| Service | Effect |
|---|---|
| None | Base production |
| Regular | Production bonus |
| Excellent | Maximum productivity |

Exact numerical modifiers are not fixed in v0.1 and must be balanced through gameplay testing.

Supply service is a logistics decision: the player decides whether the cost of supplying an industry is justified by its additional production.

## Personnel Model

Personnel represents labor being supplied to a productive site.

**Passengers** travel to destinations. **Personnel** travel because a productive site requires workers.

### Returnable personnel

Personnel is normally temporary at the worksite and may return after a work period or assignment.

```text
Town / Personnel Source
        ↓
    Personnel
        ↓
      Worksite
        ↓
 Returning Personnel
```

The destination gives generic Personnel its contextual meaning. Separate cargoes for miners, engineers, technicians, scientists, etc. are not required by the core model.

## Productive Trips

A productive transportation service should answer:

1. What does this site need?
2. What does this site produce?
3. What can I carry on the return trip?

Example:

```text
Outbound:
Personnel + Tools & Hardware + Industrial Equipment
                    ↓
                  Mine
                    ↓
Return:
Coal + Returning Personnel
```

Not every route needs a balanced return cargo. Empty returns remain valid where geography or economics makes them unavoidable.

## Historical Evolution

The same economic role may represent different physical technologies in different eras.

For example, Tools & Hardware can represent hand tools and replacement parts in an early era, machine tools and maintenance equipment during industrialization, and advanced components later. Industrial Equipment can evolve from pumps and hoists to steam machinery, electrical machinery, automated machinery, and robotics. Technology Systems can evolve from electrical equipment and communications to electronics, computers, autonomous control, AI systems, and robotics.

Cargo identities should remain stable where practical while the technology represented by a cargo evolves.

## Date-Gated Industry Succession

Industries may be introduced, overlap, mature, decline, and eventually stop appearing as new construction according to the current year. Existing industries should generally continue operating after successors appear.

```text
Traditional Farm
    ↓ overlap
Mechanized Farm
    ↓ overlap
Precision / Automated Farm
```

## Modularity

The framework supports optional modules such as Agriculture, Forestry, Heavy Industry, Maritime, Offshore, Energy, Chemicals, Global Logistics, Recycling, Finance, Advanced Technology, and Space.

Developers should be able to add or remove industries and define their own primary resources, products, operational inputs, human/economic flows, and optional financial flows while relying on the common economic concepts.

## Financial Model

Financial activity has two layers.

### Systemic money

Company money, revenue, expenses, investment, loans, and economic value are handled by the game's monetary/economic simulation and do not need to be physical cargo.

### Financial logistics

Physical financial objects may be transportable when doing so creates meaningful gameplay.

Possible progression:

```text
Gold → Bullion → Mint → Coin / Currency → Banks → Cash / Financial Documents → Modern high-value logistics
```

Digital finance should not require physical transport merely to represent digital transactions.

## Geography

Economic relationships should interact with geography. Mines may be remote; farms favor suitable land; ports favor coastlines and navigable water; offshore industries require maritime access; mountains, rivers, and islands alter transportation choices; large cities generate passenger, mail, and goods demand.

## Transportation Philosophy

Avoid a simple ladder where every new vehicle replaces every previous vehicle. Different modes should have economic niches.

Examples include sailing vessels for inexpensive early bulk movement, steamships for long-distance movement, fast ferries for frequent coastal service, hydrofoils for high-speed coastal service, hovercraft for shallow water, rail for high-capacity corridors, aircraft for long-distance or high-value movement, and helicopter/VTOL craft for remote-site personnel and specialized logistics.

The fastest vehicle should not automatically be the best vehicle.

## Reference Economy

The reference economy spans approximately 1700–2150:

1. **1700–1850 — Transformation:** agrarian to industrial; sail, animal transport, canals, steam, early rail, coal and iron.
2. **1851–2000 — Acceleration:** electricity, petroleum, steel, mass production, aviation, telecommunications, containerization, globalization, computing.
3. **2001–2150 — Convergence:** electrification, renewables, batteries, automation, autonomy, advanced logistics, offshore energy, advanced manufacturing, and speculative late-game technologies.

## Compatibility Principle

The framework aims to reduce conceptual overlap and incompatibility between independently designed economies through stable semantic roles, explicit industry relationships, modular definitions, clear ownership, avoidance of unnecessary duplicate cargo concepts, versioning, and documented assumptions.

This cannot eliminate every technical NewGRF compatibility problem, but it can provide a common economic vocabulary and architecture.

## Non-Goals for v0.1

Avoid requiring detailed accounting, individual employee simulation, real-world monetary policy, physical movement of all money, dozens of nearly identical supply cargoes, or mandatory multi-stage chains for every product.

Complexity should be added only when it creates meaningful transportation decisions.

## Guiding Principle

> **Simple rules. Deep logistics.**
>
> Bring what a productive site needs. Move the people who make it work. Take away what it produces. Build the network that makes the whole economy more productive.

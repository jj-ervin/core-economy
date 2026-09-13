# Era Model

## Purpose

The Era Model defines the historical progression of the OpenTTD Economic Framework from 1700–2150. It controls when industries, technologies, vehicles, infrastructure, and optional modules emerge, mature, decline, and become legacy systems.

> **History should change the economic choices available to the player, not erase the choices they already made.**

## Design Philosophy

The reference economy uses three broad design eras:

| Era | Years | Transition |
|---|---:|---|
| Transformation | 1700–1850 | Agrarian → industrial |
| Acceleration | 1851–2000 | Industrial → mass-production/global |
| Convergence | 2001–2150 | Digital → automated/advanced |

These are design eras, not rigid historical labels. Sub-phases may be used when they improve gameplay.

The economy should feel historical without becoming a technology-tree simulator.

## Transformation — 1700–1850

The economy moves from agrarian trade toward industrial production.

### 1700–1750 — Agrarian Trade

Traditional farms, livestock, forestry, fisheries, small mines, mills, trading wharves, canals, horse-and-wagon transport, and sailing vessels dominate. Personnel demand is generally high because production is labor-intensive.

### 1751–1800 — Early Industrialization

Larger mills, improved iron production, expanding coal extraction, commercial ports, early mechanization, and steam technology emerge.

### 1801–1850 — Steam Transition

Steam engines, railways, steamships, mechanized factories, larger mines, and industrial ports become increasingly important. New technology does not instantly replace its predecessor.

## Acceleration — 1851–2000

Industrial production expands through steel, electricity, petroleum, chemicals, mass production, mechanized agriculture, large-scale mining, rail, motor shipping, aviation, telecommunications, containerization, and computing.

### 1851–1900 — Industrial Expansion

Steel, industrial machinery, rail corridors, steamships, industrial ports, large factories, petroleum, electricity, and telegraphy expand.

### 1901–1950 — Mass Production

Automobiles, trucks, modern factories, electrical grids, oil refining, chemicals, large-scale agriculture, aviation, modern shipbuilding, and early offshore petroleum become important.

### 1951–1970 — High Industrialization

Dieselization, jet aviation, containerized logistics, petrochemicals, large offshore platforms, advanced manufacturing, highways, and deepwater ports expand. Containerization is treated as a logistics transformation, not merely a new ship type.

### 1971–2000 — Global Network

Container ports, global supply chains, modern logistics, computers, telecommunications, advanced electronics, industrial automation, sophisticated offshore operations, and high-speed passenger transport become established.

## Convergence — 2001–2150

The economy increasingly emphasizes electrification, automation, advanced information systems, renewable energy, autonomous logistics, and specialized manufacturing. The further the timeline extends beyond the present, the more explicitly speculative the design becomes.

### 2001–2030 — Digital Integration

Advanced electronics, automated logistics, renewable energy, batteries, sophisticated manufacturing, offshore wind, and precision agriculture expand.

### 2031–2050 — Electrification and Automation

Electric transport, autonomous logistics, advanced batteries, offshore wind, hydrogen systems, highly automated factories, precision agriculture, and remote operations expand.

### 2051–2100 — Autonomous Industry

Possible developments include autonomous vessels, autonomous mining, highly automated farms, robotic factories, advanced storage, offshore energy complexes, hydrogen logistics, automated ports, and distributed manufacturing.

### 2101–2150 — Advanced / Speculative Economy

Optional systems may include highly autonomous industrial networks, advanced energy systems, mature offshore energy complexes, space infrastructure, advanced materials, and highly automated logistics. Speculative systems remain modular.

## Era Availability States

| State | Meaning |
|---|---|
| Not Available | Cannot normally exist yet |
| Emerging | Available but uncommon |
| Available | Normal new construction/operation |
| Mature | Fully established |
| Declining | Increasingly superseded |
| Legacy | Existing examples remain; new construction normally closed |
| Retired | No longer part of the active reference economy |

Not every industry must use every state.

## Succession and Overlap

Industries evolve through succession families:

```text
Traditional Farm
      ↓
Mechanized Farm
      ↓
Precision Farm
      ↓
Automated Farm
```

Other examples:

```text
Traditional Mine → Industrial Mine → Mechanized Mine → Automated Mine
```

```text
Trading Wharf → Commercial Harbor → Industrial Port → Deepwater Port → Container Port → Smart/Mega Port
```

When a successor appears, the predecessor normally remains available for a period. This overlap creates a living historical landscape and prevents mandatory replacement gameplay.

## New Construction vs Existing Industry

The framework distinguishes between new construction and continued operation.

```text
New construction: Traditional Farm → unavailable
Existing farm:    Traditional Farm → continues operating
```

Automatic destruction of legacy industries is not the default. Existing facilities may become less competitive through optional maintenance, supply, productivity, or technology mechanics.

## Stable Cargo Identity

Cargo identities should remain stable whenever possible.

```text
GRAIN
1700 → manual agriculture
1900 → mechanized agriculture
2050 → automated precision agriculture
```

Avoid creating separate cargoes merely because production technology changed. Technology belongs primarily to the industry and production models.

## Technology State

An industry can carry a technology state independent of cargo identity:

```text
Industry
├── Economic role
├── Inputs
├── Outputs
├── Labor intensity
├── Technology state
└── Era availability
```

Useful conceptual states include Traditional, Mechanized, Electrified, Mass Production, Computerized, Automated, Autonomous, and Advanced. Not every industry uses every state.

Technology state should explain meaningful changes in production capacity, labor demand, supply requirements, equipment requirements, energy requirements, or transportation patterns.

## Automation

Automation primarily changes how much human labor is required and which operational inputs are needed.

```text
Manual → Mechanized → Electrified → Automated → Autonomous
```

As automation rises, Personnel demand generally falls while Industrial Equipment and Technology Systems requirements may rise. Specialized human oversight may remain important.

Automation should reshape logistics rather than become a universal production bonus.

## Transportation Progression

Vehicles are not a simple chronological replacement ladder.

```text
Sailing Vessel → Steamship → Motor/Diesel Ship → Container Ship → Autonomous Vessel
```

Each vehicle can retain a niche based on cost, speed, capacity, range, port requirements, cargo suitability, reliability, geography, draft, personnel requirements, or energy use.

Other historical transport progression includes horse/wagon and canals, rail, trucks, aircraft, tankers, ferries, offshore support vessels, jets, electric transport, and autonomous systems.

> **Vehicles serve the economy.**

## Ports

Port development follows the broader economy:

```text
Trading Wharf
    ↓
Commercial Harbor
    ↓
Steam Harbor
    ↓
Industrial Port
    ↓
Modern Harbor
    ↓
Deepwater Port
    ↓
Container Port
    ↓
Mega / Smart Port
```

Approximate milestone dates are design windows, not mandatory exact dates. Specialized ports may coexist, including Fishing Harbor, Oil Port, Shipbuilding Port, Offshore Supply Base, and Container Port.

## Offshore Progression

```text
1700–1800  Coastal fishing
1800–1850  Improved navigation and coastal trade
1900s      Offshore petroleum development
1930s–50s  Offshore drilling/platforms
1950–70    Large offshore complexes
2000+      Offshore wind
2030+      Floating wind
2050+      Integrated offshore energy complexes
```

Future complexes may combine wind, hydrogen, desalination, storage, and data infrastructure. These remain optional/speculative modules.

## Finance Through the Eras

Physical financial flows may evolve from Gold, Coins, Bullion, and financial documents toward Banknotes and Securities, and later toward secure high-value logistics as digital finance becomes dominant.

Systemic money remains systemic. Physical financial cargo does not define the monetary system.

## Era Transition Rules

1. **Introduce before replacing.** New technology becomes available before old technology disappears.
2. **Overlap is intentional.** Transitional mixtures are part of the economy.
3. **Existing facilities persist.** Existing industries normally continue operating.
4. **Cargo identities remain stable.** Technology does not automatically create new cargo names.
5. **Technology changes logistics.** It should affect labor, inputs, outputs, capacity, geography, or transport.
6. **Avoid arbitrary date walls.** Dates should represent economic transitions.
7. **Future technology is modular.** Speculative systems cannot be required for the historical core.

## Date Gating Without a Technology Tree

Avoid giant prerequisite chains such as:

```text
Coal → Steel → Electricity → Computers → AI
```

Instead, technologies emerge through time, industry families, modules, and economic context.

The desired experience is:

```text
New capability appears
        ↓
Player evaluates its economic value
        ↓
Old and new systems coexist
        ↓
Network evolves organically
```

## Industry Succession Examples

### Agriculture

```text
Traditional Farm → Mechanized Farm → Modern / Precision Farm → Automated Farm
```

### Forestry

```text
Traditional Forestry → Industrial Forestry → Mechanized Forestry → Precision / Sustainable Forestry
```

### Mining

```text
Traditional Mine → Industrial Mine → Mechanized Mine → Automated Mine
```

### Manufacturing

```text
Workshop → Factory → Mass-Production Factory → Automated Factory → Advanced Manufacturing
```

## Era Model and Personnel

Historical progression should generally move from high labor requirements toward automation:

```text
High labor requirement
        ↓
Mechanization
        ↓
Lower labor requirement
        ↓
Automation
        ↓
Low routine labor requirement
        ↓
Specialized human oversight
```

Personnel remains a generic HUMAN_FLOW cargo. The era model changes its demand rather than creating profession-specific cargoes.

## Era Model and Operational Supplies

Technology can change the operational input footprint without changing the core cargo identity.

```text
Traditional Farm
→ Agricultural Supplies

Mechanized Farm
→ Agricultural Supplies + Industrial Equipment

Automated Farm
→ Agricultural Supplies + Technology Systems
```

## Era Model and Geography

Technology changes where economic activity can profitably occur.

- Canals expand inland bulk movement.
- Rail enables long-distance inland industry.
- Steamships expand maritime range.
- Refrigeration expands food markets.
- Tankers enable large-scale petroleum distribution.
- Containerization strengthens global networks.
- Aircraft make high-value long-distance transport practical.
- Automation enables more remote operations.
- Offshore technology moves production into marine environments.

The era model should change the geography of viable economic activity, not merely which industries appear.

## Network Complexity

Complexity should increase through interconnection rather than arbitrary dependencies.

```text
Early:       Local resources → local processing → nearby markets
Industrial:  Resources → processing → manufacturing → regional markets
Global:      Resource regions → global logistics → specialized processing → manufacturing hubs → worldwide markets
Advanced:    Distributed resources → autonomous logistics → specialized production → regional/global markets
```

## Optional Modules Across Eras

| Module | Early window | Later development |
|---|---:|---|
| Agriculture | 1700 | Precision/automation |
| Forestry | 1700 | Mechanized/precision |
| Heavy Industry | 1750+ | Advanced manufacturing |
| Maritime | 1700 | Autonomous vessels |
| Offshore | 1700 coastal | Petroleum → wind → integrated energy |
| Energy | 1700+ | Grid/renewables/storage |
| Chemicals | 1800s | Advanced materials |
| Global Logistics | 1800s | Containerization/autonomy |
| Recycling | 1800s/1900s | Circular systems |
| Finance | 1700 | Digital/high-security logistics |
| Advanced Technology | 1900s | Autonomous/advanced systems |
| Space | Optional future | 2050+ speculative |

## Balancing Principles

New technology should generally introduce tradeoffs involving some combination of cost, capacity, speed, labor requirement, equipment requirement, infrastructure requirement, reliability, range, geography, and environmental impact.

The newest technology should not automatically be universally best.

```text
Older technology
→ cheaper
→ labor-intensive
→ flexible

New technology
→ higher capital cost
→ lower labor requirement
→ higher capacity
→ greater infrastructure needs
```

## Anti-Patterns

- **Hard replacement dates:** do not make all old industries disappear on a date.
- **Cargo duplication by era:** do not create Old Grain, Modern Grain, and Future Grain merely because technology changed.
- **Technology as a simple bonus:** avoid turning every technology into `+20% production`.
- **Chronological vehicle replacement:** newer vehicles should not automatically invalidate older ones.
- **Mandatory future content:** speculative 2050–2150 systems must remain optional.
- **Excessive historical micromanagement:** model meaningful transitions, not every invention.
- **Date gates without economic meaning:** a date should correspond to a plausible transition or useful gameplay distinction.

## Design Checklist

Before assigning an era gate, ask:

- What economic transition does this represent?
- Is the date a design window rather than an arbitrary wall?
- Does the predecessor remain useful?
- Should new construction eventually end?
- Should existing examples continue operating?
- Does the change affect labor?
- Does it affect operational inputs?
- Does it affect production capacity?
- Does it affect geography?
- Does it create a meaningful transportation niche?
- Does it preserve stable cargo identities?
- Is it core or optional-module content?
- Is speculative content clearly separated from established history?
- Does the transition make the network more interesting rather than merely more complicated?

## Reference Progression

```text
1700  Agrarian Trade
  ↓
1750  Early Industrialization
  ↓
1800  Steam Transition
  ↓
1850  Industrial Expansion
  ↓
1900  Industrial / Petroleum Economy
  ↓
1950  Mass Production
  ↓
1970  Containerized Global Logistics
  ↓
2000  Digital / Global Network
  ↓
2030  Electrification + Automation
  ↓
2050  Autonomous Industry
  ↓
2100  Advanced Automated Economy
  ↓
2150  Speculative Advanced Economy
```

This is a reference backbone, not a mandatory list of discrete game eras.

## Guiding Principle

> **History should change the economic choices available to the player, not erase the choices they already made.**
>
> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

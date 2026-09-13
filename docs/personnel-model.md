# Personnel Model

## 1. Purpose

This document defines the economic meaning and gameplay role of **Personnel** within the OpenTTD Economic Framework.

Personnel is a specialized human-flow cargo representing labor being transported to a place where productive economic activity occurs. It is intended to create meaningful logistics without creating a separate cargo for every profession.

The model is deliberately implementation-neutral. It defines the economic behavior first; OpenTTD/NewGRF mechanics are an implementation layer.

> **Personnel is labor in motion, not passengers in disguise.**

---

## 2. Definition

**Personnel** is a HUMAN_FLOW cargo used when people must be transported because a productive site requires their labor.

The destination gives the cargo its occupational context. The same generic Personnel cargo can represent miners at a mine, agricultural workers at a farm, engineers at a factory, crews at a shipyard, technicians at an offshore platform, or researchers at a research facility.

Personnel therefore has an economic relationship with a **worksite**, rather than merely a destination town.

---

## 3. Personnel vs. Passengers

Personnel and Passengers are intentionally distinct.

| Flow | Economic meaning |
|---|---|
| Passengers | People traveling because they want or need to travel between places. |
| Personnel | People traveling because a productive site needs their labor. |

Passengers create a transportation market.

Personnel creates a **labor logistics requirement**.

A route can therefore carry both, but they should not be interchangeable by default.

Personnel should not simply be implemented as a renamed Passenger cargo. Its acceptance, demand, service quality, work-cycle behavior, and relationship to industry production are different.

---

## 4. Personnel as HUMAN_FLOW

Within the cargo ontology, Personnel belongs to:

```text
HUMAN_FLOW
└── Personnel
```

Personnel is a stable semantic cargo identity. Occupational labels should normally be contextual rather than separate cargoes.

Preferred:

```text
Personnel → Mine
```

where the destination interprets the flow as mining labor.

Avoid:

```text
Miners
Engineers
Farm Workers
Offshore Technicians
Researchers
Shipyard Workers
```

unless a specific optional module demonstrates a strong gameplay reason to split them.

---

## 5. Source, Destination, and Assignment

A Personnel movement has three conceptual stages:

1. **Source** — where personnel are recruited, housed, staged, or otherwise made available.
2. **Destination** — the worksite requiring labor.
3. **Assignment** — the economic relationship connecting the Personnel flow to that worksite.

Conceptually:

```text
PERSONNEL SOURCE
      ↓
  PERSONNEL
      ↓
WORKSITE ASSIGNMENT
      ↓
  WORK PERIOD
```

The source does not need to be a dedicated Personnel industry. Towns, settlements, worker camps, ports, stations, or other suitable locations may serve as sources depending on the era and module.

---

## 6. Worksite Relationship

Personnel should be consumed economically by the worksite's labor requirement rather than disappearing as an arbitrary cargo transaction.

A worksite has a **Personnel demand** determined by factors such as:

- Industry size
- Labor intensity
- Technology state
- Degree of automation
- Operating capacity
- Remote location
- Work-cycle duration
- Optional module rules

A simplified conceptual relationship is:

```text
Personnel Demand
    = Industry Scale
    × Labor Intensity
    × Operating Requirement
    × Remote/Operational Factor
    ÷ Automation Factor
```

This is a conceptual model, not a locked implementation formula.

---

## 7. Personnel Demand

Personnel demand should be **bounded and understandable**.

A small, highly automated facility should not require the same Personnel flow as a large, labor-intensive operation.

Demand should generally scale with industry capacity:

```text
Small Worksite   → Low Personnel demand
Medium Worksite  → Moderate Personnel demand
Large Worksite   → High Personnel demand
```

Labor intensity then differentiates industries.

For example:

```text
Traditional Farm       → moderate/high labor intensity
Mechanized Farm        → lower labor intensity
Automated Farm         → low labor intensity

Early Mine             → high labor intensity
Mechanized Mine        → moderate labor intensity
Automated Mine         → low labor intensity
```

This lets technological progress change the **quantity of labor required**, rather than merely adding a generic production multiplier.

---

## 8. Personnel Service Levels

Personnel availability can be modeled as a service level similar to operational supplies.

A conceptual scale is:

| Personnel service | Meaning |
|---|---|
| None | Worksite has little or no required labor available. |
| Partial | Some labor is available; operations are constrained. |
| Regular | Normal staffing level. |
| Excellent | Strong staffing coverage; worksite can operate at intended labor capacity. |

Exact factors remain subject to gameplay balancing.

The framework should avoid making every industry completely nonfunctional without Personnel. Some industries may have a hard minimum labor requirement, while others may experience progressively reduced output as staffing falls.

---

## 9. Returnability

Personnel may be **returnable** after completing a work period.

This is a core feature of the model, not merely a cosmetic return cargo.

Conceptual lifecycle:

```text
PERSONNEL SOURCE
      ↓
  PERSONNEL
      ↓
ASSIGNED TO WORKSITE
      ↓
  WORK PERIOD
      ↓
RETURNING PERSONNEL
      ↓
PERSONNEL SOURCE / NEXT ASSIGNMENT
```

The return trip creates a legitimate economic opportunity:

```text
OUTBOUND
Personnel + Operational Inputs
             ↓
          Worksite
             ↓
RETURN
Product + Returning Personnel
```

Not every Personnel movement must return. Empty returns remain valid where the economic circumstances do not justify a return flow.

---

## 10. Work Cycles

Personnel movement should conceptually represent a **work cycle**, not instantaneous teleportation of labor.

A work cycle may include:

```text
Recruit / stage
    ↓
Transport
    ↓
Assignment
    ↓
Work period
    ↓
Release / rotation
    ↓
Return or reassignment
```

The exact duration need not be simulated literally. The framework only requires that returnability have an economic explanation.

Long-cycle remote industries may therefore create different logistics patterns from short-cycle urban or regional industries.

---

## 11. Personnel Storage and Holding

Personnel can require temporary staging or holding capacity.

Conceptual examples include:

- Worker stations
- Crew terminals
- Company housing
- Worker camps
- Port staging facilities
- Offshore accommodation
- Remote-site transport hubs

The framework does not require a dedicated physical storage building for every case. The implementation may represent holding capacity through stations, industry acceptance, town population, or module-specific infrastructure.

The important economic concept is that **available labor is not necessarily identical to immediately assigned labor**.

---

## 12. Personnel and Industry Scale

Personnel demand should respond to industry scale.

Example:

```text
Mine A — Small
Personnel demand: low

Mine B — Large
Personnel demand: high
```

If the player expands Mine B, the labor logistics problem should grow with it.

This makes expansion create transportation consequences rather than only increasing production and revenue.

---

## 13. Labor Intensity

Labor intensity describes how much human labor is required to operate an industry relative to its productive capacity.

Examples:

| Industry state | Typical labor intensity |
|---|---|
| Manual agriculture | High |
| Mechanized agriculture | Medium |
| Precision agriculture | Low |
| Early mining | High |
| Mechanized mining | Medium |
| Automated mining | Low |
| Early factory | High |
| Mass-production factory | Medium |
| Highly automated factory | Low |
| Shipyard | Medium/high |
| Advanced shipyard | Medium/low |
| Offshore platform | Medium/high |
| Highly automated offshore facility | Low/medium |

Labor intensity is an economic property, not a profession list.

---

## 14. Automation Progression: 1700–2150

Automation should reduce Personnel demand over historical time.

### 1700–1850 — Transformation

Typical characteristics:

- High manual labor requirements
- Limited mechanization
- Animal power
- Early steam machinery
- Labor-intensive extraction and agriculture

Personnel can be a major part of productive logistics.

### 1851–2000 — Acceleration

Typical characteristics:

- Mechanization
- Electrification
- Mass production
- Industrial machinery
- Improved transportation
- Early industrial automation
- Computer-controlled processes late in the era

Personnel remains important, but many industries require less labor per unit of output.

### 2001–2150 — Convergence

Typical characteristics:

- Advanced automation
- Robotics
- Autonomous systems
- Remote operations
- AI-assisted operations
- Highly automated manufacturing
- Autonomous resource extraction

Personnel demand generally declines per unit of productive capacity, but specialized and remote labor remains economically important.

Automation therefore changes the **labor requirement**, not simply a generic production coefficient.

---

## 15. Remote-Site Logistics

Remote industries are a major use case for Personnel.

Examples:

- Offshore platforms
- Remote mines
- Mountain operations
- Arctic facilities
- Large construction projects
- Research stations
- Space facilities in optional future modules

Remote worksites may have:

- High Personnel demand
- Long work cycles
- Specialized supply requirements
- Strong dependence on reliable transport
- Limited local population

This creates meaningful transportation problems without requiring separate profession cargoes.

Example:

```text
Coastal City
     ↓ Personnel
Supply Port
     ↓ Offshore transport
Offshore Platform
     ↓
Oil / Gas
     ↓
Refinery
```

Personnel can therefore help connect passenger-producing regions to industrial networks.

---

## 16. Personnel + Operational Supplies

Personnel and operational supplies are complementary.

A worksite may need both:

```text
Personnel
    +
Tools & Hardware
    +
Industrial Equipment
    +
Construction Materials
    ↓
WORKSITE
    ↓
PRODUCT
```

This creates the desired productive round-trip structure without making every input a hard prerequisite.

For example:

```text
Personnel + Tools & Hardware
             ↓
            Mine
             ↓
Coal + Returning Personnel
```

The result is a logistics problem with multiple useful flows rather than a simple one-way cargo chain.

---

## 17. Personnel + Technology

Technology can reduce labor requirements while increasing productive capacity.

Conceptually:

```text
Technology Improvement
        ↓
Higher automation
        ↓
Lower Personnel requirement per unit of capacity
        ↓
Different logistics pattern
```

This should be preferred over simply applying:

```text
Technology = +20% production
```

when a more meaningful labor consequence can be represented.

Technology may simultaneously:

- Reduce Personnel demand
- Increase production capacity
- Increase equipment requirements
- Increase technology-system supply requirements
- Change the skills represented by generic Personnel

The framework should preserve the generic cargo identity while allowing its economic meaning to evolve.

---

## 18. Personnel Routing and Geography

Personnel should obey transportation geography.

Workers cannot be assumed to exist at every worksite.

A productive site may need Personnel from:

- Nearby towns
- Regional population centers
- Port cities
- Worker settlements
- Specialized hubs
- Remote camps

The transportation network therefore determines whether labor can reach the worksite.

This creates a useful relationship:

```text
Population Geography
        ↓
Personnel Availability
        ↓
Transportation Network
        ↓
Industrial Capacity
```

A remote industry with excellent natural resources but poor Personnel access may operate below potential.

---

## 19. Personnel Lifecycle

The conceptual lifecycle is:

```text
AVAILABLE
    ↓
ASSIGNED
    ↓
IN TRANSIT
    ↓
AT WORKSITE
    ↓
WORKING
    ↓
RELEASED
    ↓
RETURNING / REASSIGNED
    ↓
AVAILABLE
```

An implementation does not need to represent every state explicitly. These states define the economic meaning the implementation should preserve.

---

## 20. Personnel Shortages

A Personnel shortage should have understandable consequences.

Possible effects include:

- Reduced production
- Reduced operating capacity
- Slower growth
- Reduced effective industry size
- Temporary idle capacity
- Increased dependence on automation

The framework should prefer gradual and legible consequences over arbitrary failure.

A worksite should not necessarily shut down completely because one vehicle missed one trip.

---

## 21. Personnel Oversupply

Excess Personnel should not automatically generate infinite production.

Once an industry reaches its intended labor capacity, additional Personnel should generally have diminishing or no further productive effect.

Conceptually:

```text
No Personnel       → constrained
Some Personnel     → partial operation
Regular Personnel  → normal operation
Excellent Staffing → maximum intended labor service
Excess Personnel   → little/no additional benefit
```

This prevents labor from becoming an unlimited production multiplier.

---

## 22. Personnel and Transportation Quality

Because Personnel represents labor rather than generic travel, transport quality can matter.

Relevant factors may include:

- Travel time
- Reliability
- Capacity
- Frequency
- Route length
- Transfer requirements
- Remote-site access

A late or unreliable Personnel service can reduce effective staffing even if the nominal cargo quantity is sufficient.

This allows vehicle choice to become an economic decision rather than a simple speed upgrade.

Example:

```text
Slow bulk transport
    → cheap but poor for rotating offshore crews

Fast ferry / aircraft / helicopter
    → more expensive but useful for personnel rotation
```

---

## 23. Personnel and Vehicle Niches

Personnel strengthens the framework's transportation philosophy:

> Vehicles serve the economy.

Different vehicles can solve different Personnel problems.

Examples:

- Passenger rail — high-capacity regional labor movement
- Coastal ferry — routine coastal workforce transport
- Fast ferry — frequent personnel rotation
- Aircraft — long-distance labor movement
- Helicopter — remote-site Personnel
- VTOL — future remote logistics
- Offshore supply vessel — combined personnel and supplies

This prevents the vehicle roster from becoming a simple chronological speed ladder.

---

## 24. Examples

### 24.1 Mine

```text
Town
 ↓
Personnel
 ↓
Mine
 ↑
Tools & Hardware
Industrial Equipment

Mine
 ↓
Coal / Iron Ore
 ↓
Regional Industry

Mine
 ↓
Returning Personnel
 ↓
Town / Next Assignment
```

The mine's labor requirement decreases as mining technology becomes more automated.

### 24.2 Farm

```text
Town / Settlement
 ↓
Personnel
 ↓
Farm
 ↑
Agricultural Supplies
 ↑
Machinery / Equipment

Farm
 ↓
Grain / Livestock
 ↓
Food Processing
```

A traditional farm may have high labor intensity, while a precision automated farm requires much less Personnel per unit of production.

### 24.3 Factory

```text
Personnel + Industrial Equipment + Materials
                  ↓
                Factory
                  ↓
              Products
                  ↓
          Regional / Global Market
```

Factory automation reduces Personnel demand while increasing dependence on machinery and technology systems.

### 24.4 Shipyard

```text
Personnel + Steel + Machinery + Construction Materials
                         ↓
                     Shipyard
                         ↓
                      Ships
```

Personnel remains important even as shipbuilding becomes increasingly mechanized and automated.

### 24.5 Offshore Platform

```text
Coastal Population Center
          ↓
      Personnel
          ↓
     Supply Port
          ↓
 Offshore Transport
          ↓
 Offshore Platform
          ↓
       Oil / Gas
```

Personnel rotation can share transport capacity with operational supplies, creating productive round trips.

### 24.6 Research Facility

```text
Population Center
      ↓
  Personnel
      ↓
Research Facility
      ↑
Technology Systems
      ↑
Industrial Equipment
      ↓
Advanced Goods / Knowledge Outputs
```

Personnel remains generic while the facility provides the contextual meaning: researchers, technicians, engineers, or support staff.

---

## 25. OpenTTD/NewGRF Representation

The economic model should remain implementation-neutral until the gameplay requirements are stable.

An eventual OpenTTD/NewGRF implementation may represent Personnel through some combination of:

- A dedicated cargo type
- Industry acceptance
- Industry production effects
- Station acceptance
- Cargo callbacks / production logic where supported
- Date-gated industry availability
- Returnable or paired flow conventions
- Industry-specific production modifiers
- Vehicle cargo compatibility

The framework should **not** assume that every conceptual state maps directly to an OpenTTD cargo state.

Implementation questions such as exact callback behavior, cargo payment, transfer handling, and return-trip mechanics belong in an implementation specification after the economic model is validated.

The boundary is:

```text
Economic Definition
        ↓
Personnel Model
        ↓
Implementation Adapter
        ↓
NewGRF / OpenTTD Behavior
```

This prevents current engine limitations from prematurely distorting the economic design.

---

## 26. Anti-Patterns

### 26.1 Profession-Specific Cargo Explosion

Do not create a cargo for every occupation.

Bad:

```text
Miners
Engineers
Farm Workers
Researchers
Technicians
```

Preferred:

```text
Personnel
```

with occupational meaning supplied by the destination.

### 26.2 Treating Personnel as Ordinary Passengers

Personnel should have an economic worksite relationship and potentially a return cycle.

### 26.3 Universal Hard Requirement

Not every industry should become completely dependent on Personnel.

Labor intensity and automation should differ across industries and eras.

### 26.4 Infinite Worker Teleportation

Personnel should require an actual transportation path from an available population source to the worksite.

### 26.5 Pointless Return Mechanics

Do not force a return trip merely to make routes symmetrical.

Returnability should represent a real work cycle, rotation, reassignment, or other economic reason.

### 26.6 Personnel as a Generic Production Multiplier

Personnel should represent labor demand. It should not become an arbitrary universal `+X% production` cargo.

### 26.7 Unlimited Staffing

Additional Personnel beyond the worksite's useful capacity should have diminishing or zero benefit.

### 26.8 Simulation for Simulation's Sake

The model should create meaningful transportation decisions. It should not simulate individual workers, shifts, payroll, or employment contracts unless a future optional module has a compelling reason.

---

## 27. Design Checklist

Before adding Personnel behavior to an industry, ask:

- Is labor actually an economically meaningful input here?
- Is Personnel distinct from ordinary passenger travel in this case?
- What is the industry's labor intensity?
- How does industry scale affect Personnel demand?
- What does automation do to labor demand?
- Can Personnel be sourced geographically in a believable way?
- Does the route create a meaningful transportation problem?
- Is a return flow economically justified?
- Can Personnel share transport with operational supplies?
- Does the model avoid creating profession-specific cargoes?
- Is the shortage behavior understandable?
- Is excess staffing bounded?
- Does the model preserve the economic definition independently of NewGRF implementation constraints?

If the answer to these questions is weak, Personnel probably should not be added as a special requirement.

---

## 28. Guiding Principle

> **Personnel is not “people cargo.” It is labor being moved to where economic work needs to happen.**

The purpose of the Personnel system is to make labor geography part of logistics while remaining simple enough to understand.

The desired result is:

```text
Population
   ↓
Personnel Logistics
   ↓
Industrial Capacity
   ↓
Production
   ↓
Economic Network
```

This makes transportation a participant in the economy rather than merely a delivery mechanism.

> **Simple rules. Deep logistics.**

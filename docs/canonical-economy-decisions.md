# Canonical Economy Decisions

Status: **Design baseline — frozen pending validation/playtesting**

This is the normative baseline for the Economy Toolkit and Reference Economy. Changes to these rules require deliberate design revision.

## Core philosophy

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

- Add economic relationships before adding cargoes.
- Aggregate things that behave the same way economically.
- Add a cargo only when the distinction creates meaningful transportation, production, geographic, historical, or strategic choice.
- Complexity should come from relationships and routing, not cargo proliferation.

## Economic roles

1. Primary Resources
2. Products
3. Operational Supplies
4. Human/Economic Flows
5. Optional Financial Flows

## Core cargo identities

**Primary:** Grain, Livestock, Timber, Fish, Coal, Iron Ore, Stone, Clay, Oil, Gas, Copper Ore.

**Products:** Food, Lumber, Steel, Copper, Petroleum Products, Machinery, Chemicals, Manufactured Goods, Electronics, Advanced Goods.

**Operational supplies:** Tools & Hardware, Industrial Equipment, Construction Materials, Agricultural Supplies, Fuel, Chemicals, Technology Systems.

**Optional financial flows:** Gold, Bullion, Coins/Cash, Securities/Financial Documents.

Financial cargoes are optional physical flows representing high-value material or financial instruments. They do not replace the game's systemic money/economy and should be enabled only where they create meaningful logistics or security gameplay.

## Copper

```text
Copper Ore → Copper Works → Copper → Machinery / Electronics
```

There is no separate `processed copper` cargo.

## Petroleum and chemicals

```text
Oil → Refinery → Petroleum Products
                     ├→ Fuel distribution
                     └→ Chemical feedstock / Chemical Works
```

Refinery produces Petroleum Products. Chemical Works produces Chemicals. Gas may feed Chemical Works only through an explicit recipe.

## Fuel

Fuel is a first-class operational-supply cargo supported by the toolkit. It aggregates gasoline, diesel, marine fuel, aviation fuel, and similar energy-use products. Fuel Depot/Fuel Terminal is a storage/distribution node, not another refinery. Fuel should normally be an operational service demand rather than a universal hard prerequisite.

## Chemicals

Chemicals are an aggregated identity covering lubricants, greases, solvents, coolants, reagents, process chemicals, and specialty chemicals. Do not split these into separate cargoes without a demonstrated gameplay distinction. Chemicals can be both a manufactured product and an operational supply.

## Agricultural Supplies

Agricultural Supplies aggregate fertilizer, animal feed, soil amendments, crop treatments, agricultural chemicals, and related consumables. Their real-world composition may change by era while the identity remains stable.

## Personnel

Personnel is distinct from Passengers and represents people transported because a productive site requires labor.

```text
Town / Personnel Source → Personnel → Worksite → Returning Personnel
```

Returning Personnel may be an implementation state rather than a separate cargo identity. Productive round trips are encouraged where economically appropriate.

## Recycling

Recycling is a supported secondary/circular-economy module. Prefer broad `Scrap / Recyclables` and bounded recovery over material-by-material waste cargoes. Recycling must never create unlimited resources.

## Historical progression

Reference eras:

- Transformation: 1700–1850
- Acceleration: 1851–2000
- Convergence: 2001–2150

Industry successors are date-gated and may overlap predecessors. A closed construction window does not mean an existing industry disappears. Stable cargo identities should survive technological succession whenever possible.

## Operational supply service model

- None → 100% base productivity
- Regular → approximately 115–125%
- Excellent → approximately 135–150%

These are balance targets, not immutable engine constants. Operational supplies normally do not count as hard inputs.

## Complexity guardrails

- Most industries: 0–4 meaningful hard inputs.
- Advanced industries: normally no more than 5 without explicit justification.
- Core chains should normally remain below six mandatory intermediate transformations.
- Production and operational-supply graphs are validated separately.
- Legitimate recycling cycles must be explicitly bounded and classified.

## Recipe semantics

Allowed relationship semantics:

- `required`
- `proportional`
- `preferred`
- `alternative`
- `optional`
- `supply`

Ambiguous `and/or` recipe prose is prohibited.

## Toolkit governance

The toolkit should make it easier to build a good economy, not easier to build a complicated economy.

AI authoring may construct and modify supported economy objects, but must validate changes, report assumptions, and never silently invent cargo semantics, add cargoes, alter locked rules, create unbounded cycles, make every supply mandatory, bypass validation, or claim validity without validation.

> **Humans define intent. The framework defines the rules. AI helps construct and validate the economy.**

# Repository-Wide Contract Cleanup

**Status:** Active contract guidance — September 2026

This document records the repository-wide terminology and compatibility rules that apply to all economic framework documentation, schemas, examples, and future machine-readable economy definitions.

## 1. Canonical cargo contract

Use the plural `classes` array for every cargo definition:

```yaml
id: chemicals
name: Chemicals
classes:
  - product
  - operational_supply
```

Do not introduce new singular `class` or `role` fields in cargo definitions. Legacy examples using `class:` are historical migration examples only and must not be copied into new definitions.

## 2. Approved cargo classes

The approved semantic classes are:

- `primary`
- `product`
- `operational_supply`
- `human_flow`
- `financial`
- `optional`

`optional` is an availability or module designation. It is not a substitute for a semantic economic role. A cargo participating in a production, consumption, supply, human-flow, or financial relationship must declare its actual role as well.

## 3. Multi-role cargoes

One stable cargo identity may declare more than one semantic class. This does not create duplicate cargo IDs, duplicate transport slots, or separate cargoes.

Canonical example:

```yaml
id: chemicals
classes:
  - product
  - operational_supply
```

## 4. Canonical production terminology

Use these relationships consistently:

```text
Oil → Refinery → Petroleum Products
Defined feedstocks → Chemical Works → Chemicals
Copper Ore → Copper Works → Copper
Petroleum Products → Fuel Depot / Terminal → Fuel distribution
```

The repository must not define a canonical `processed copper` cargo.

## 5. Recipe semantics

Do not use ambiguous phrases such as `and/or` in active recipe definitions. Encode alternatives explicitly using a relationship of `alternative` and a named group, for example:

```yaml
hard_inputs:
  - cargo: grain
    relationship: alternative
    group: food_feedstock
  - cargo: livestock
    relationship: alternative
    group: food_feedstock
  - cargo: fish
    relationship: alternative
    group: food_feedstock
```

The validator must later define the group cardinality rule, such as “at least one member of the group is required.”

## 6. Operational supplies

The supported operational-supply vocabulary includes:

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems
- Fuel
- Chemicals

Operational supplies normally modify productivity, capacity, reliability, or efficiency. They are not universal hard prerequisites.

## 7. Manifest versus definition

An economy manifest may contain references to cargo, industry, recipe, era, and module IDs. It is not itself a complete economy definition and cannot validate cross-object relationships alone.

A complete economy definition contains the actual objects. The validator operates across that complete object graph.

## 8. Historical wording

Historical decision records may mention removed concepts such as `processed copper` or singular `class` syntax when explaining the migration. Such references must be clearly marked as historical, deprecated, or rejected examples. They must not appear as active canonical definitions.

## 9. Cleanup acceptance criteria

A repository-wide cleanup is complete when:

1. New cargo examples use `classes`.
2. Active cargo contracts use approved classes only.
3. Refinery and Chemical Works have separate outputs.
4. Copper uses the stable `Copper` product identity.
5. Fuel is represented as a supported operational supply.
6. Active recipes use explicit relationship semantics.
7. Optional status is not used as a semantic role.
8. Historical migration examples are labeled as such.
9. The executable validator checks these rules against machine-readable economy data.

The first eight items are documentation-contract requirements. Item nine remains an implementation task for the validator phase.

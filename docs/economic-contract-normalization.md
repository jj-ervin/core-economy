# Economic Contract Normalization

**Status:** Authoritative cleanup note v0.1

This note records the terminology and relationship rules that all reference-economy documents, registries, schemas, examples, and future validators must follow.

## 1. Cargo identity

Use:

```yaml
id: chemicals
name: Chemicals
classes:
  - product
  - operational_supply
```

Do not use singular `class` or `role` in new cargo definitions. `classes` is an array because one stable cargo identity may have multiple legitimate economic roles.

## 2. Approved cargo classes

- `primary`
- `product`
- `operational_supply`
- `human_flow`
- `financial`
- `optional`

`optional` describes availability, ownership, or module status. It is not a replacement for a semantic class. A cargo participating in an economic relationship must have at least one applicable semantic class.

## 3. Canonical processing relationships

```text
Copper Ore → Copper Works → Copper
Oil → Refinery → Petroleum Products
Defined petroleum/gas feedstocks → Chemical Works → Chemicals
```

There is no canonical `processed copper` cargo. Copper is the stable product identity.

Refinery and Chemical Works are separate economic activities:

- Refinery performs petroleum processing and produces Petroleum Products.
- Chemical Works produces Chemicals from explicitly defined feedstocks.

## 4. Operational supplies

The current operational-supply vocabulary is:

- Tools & Hardware
- Industrial Equipment
- Construction Materials
- Agricultural Supplies
- Technology Systems
- Fuel
- Chemicals

Fuel is a first-class operational supply. Chemicals may be both a manufactured product and an operational supply.

A supply identity does not automatically become a hard input for every industry. Each industry must declare its own supply relationship and effect.

## 5. Alternative inputs

Do not use prose such as:

```text
Grain and/or Livestock and/or Fish
```

Instead, define an explicit alternative group:

```yaml
group: food_feedstock
relationship: alternative
members:
  - grain
  - livestock
  - fish
```

The validator must define the group's exact semantics, such as whether at least one member is required or whether proportional substitution is allowed.

## 6. Manifest versus definition

An economy manifest may reference IDs:

```text
Economy Manifest → object IDs
```

A complete economy definition contains the actual cargo, industry, recipe, era, and module objects:

```text
Economy Definition → complete objects and relationships
```

The validator operates on the complete definition. A manifest alone cannot validate source coverage, consumer coverage, recipe semantics, cycles, dependency depth, succession, or module isolation.

## 7. Legacy-document treatment

When older documents conflict with this note, the current contract takes precedence. Legacy wording to be corrected includes:

- singular `class` or `role` cargo fields;
- `OPERATIONAL_INPUT` as a cargo class name;
- Refinery producing Chemicals;
- Fuel described as optional or absent from the operational-supply vocabulary;
- processed copper as a cargo;
- ambiguous `and/or` recipes;
- claims that Chemicals are only a product or only a supply.

This note does not silently alter the historical design rationale. It identifies the current contract that implementation and validation work must use.

# Multi-Role Cargoes

## Rule

A cargo identity may hold more than one economic role. Use the `classes` array rather than a singular cargo-class field.

```json
{
  "id": "chemicals",
  "name": "Chemicals",
  "classes": ["product", "operational_supply"]
}
```

The cargo identity remains singular. Multiple classes describe different economic relationships for the same transported thing; they do not create duplicate cargoes, duplicate IDs, or duplicate transport slots.

## Approved classes

- `primary` — extracted, harvested, caught, mined, pumped, or otherwise obtained resource.
- `product` — processed, refined, or manufactured output.
- `operational_supply` — supply used to support productivity, capacity, reliability, or efficiency.
- `human_flow` — passengers, personnel, mail, or another explicitly defined human/economic flow.
- `financial` — optional physical financial flow.
- `optional` — availability/module designation only; it is not a semantic role by itself.

## Migration

Replace the former singular cargo-class field with:

```yaml
classes:
  - product
```

For a cargo with multiple roles, list each role once:

```yaml
classes:
  - product
  - operational_supply
```

## Validation requirements

A valid cargo must have a nonempty `classes` array containing unique approved values. `optional` must not be the only class for a cargo that participates in a defined economic relationship. Relationship validation must confirm that each production, consumption, supply, human-flow, or financial relationship is compatible with at least one declared class.

## Canonical example

Chemicals is both a manufactured product and an operational supply:

```text
Chemical Works → Chemicals → downstream production
                         └→ operational supply service
```

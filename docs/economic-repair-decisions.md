# Economic Repair Decisions: Findings 1–3

## Status

**Locked for the reference economy.**

This document records the decisions made during validation of the OpenTTD Economic Framework and supersedes conflicting provisional wording in earlier registry/reference-economy passages.

> **The economy comes first. Vehicles serve the economy.**
>
> **Simple rules. Deep logistics.**

---

# 1. Clay — Keep as Core

**Decision: RESOLVED — Clay remains a core Primary Resource.**

Clay is not an orphan resource. It has a defined core pathway through Construction Materials.

```text
Clay ───────────────┐
Stone ──────────────┤
Lumber ─────────────┼→ Construction Materials
Steel ─────────────┘
```

Construction Materials is a broad economic category. The core economy does **not** require separate brick, cement, glass, or ceramic cargoes merely to give Clay a consumer.

### Recipe semantics

Clay is an **alternative/component input** to Construction Materials, not a universal mandatory input. A Construction Materials Works may use combinations of:

- Stone
- Clay
- Lumber
- Steel

The exact proportional recipe remains a balancing parameter, but the economic relationship is now explicit.

### Optional expansion

A future Construction/Ceramics module may add dedicated clay-processing industries. That module must not be required by the core economy.

---

# 2. Copper — Add Copper Works

**Decision: RESOLVED — Copper Works becomes part of the core Heavy Industry chain.**

The previous concept of an undefined `intermediate-copper` cargo is removed. Copper now has a concrete two-stage identity:

```text
Copper Ore
    ↓
Copper Works
    ↓
Copper
    ├──→ Machinery
    └──→ Electronics
```

## Cargo identities

| Cargo | Role | Meaning |
|---|---|---|
| Copper Ore | PRIMARY_RESOURCE | Mined copper-bearing material |
| Copper | PRODUCT | Refined/processed copper suitable for industrial manufacturing |

`Copper` is a stable product identity across the historical timeline. Technology progression changes the Copper Works rather than creating era-specific copper cargoes.

## Copper Works registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Output | Geography |
|---|---|---|---|---|---|---|---|---|---|
| PRC_COPPER | Copper Works | Processing | Heavy Industry | 1850–2150 | Copper Ore | Industrial Equipment, Tools & Hardware | Medium / returnable | Copper | Near copper regions / industrial corridors |
| PRC_COPPER_ADV | Advanced Copper Works | Processing | Heavy Industry | 1980–2150 | Copper Ore | Industrial Equipment, Technology Systems | Low–Medium / returnable | Copper | Major industrial / technology regions |

### Succession

```text
PRC_COPPER
    ↓
PRC_COPPER_ADV
```

Existing Copper Works continue operating after the advanced successor becomes available. The succession rule applies to **new construction**, not automatic deletion.

## Manufacturing correction

The core manufacturing chains should consume **Copper**, not `Copper Ore/intermediate-copper`.

### Machinery

```text
Steel + Copper + Chemicals
          ↓
       Machinery
```

### Electronics

```text
Copper + Chemicals + Machinery
              ↓
          Electronics
```

This gives Copper a clear producer and multiple meaningful consumers without adding unnecessary cargo fragmentation.

---

# 3. Refinery vs Chemical Works — Separate the Functions

**Decision: RESOLVED — Refinery and Chemical Works are distinct processing stages.**

The previous design incorrectly allowed both industries to perform essentially the same Oil/Gas → Chemicals transformation. That overlap is removed.

## Refinery

The Refinery represents petroleum processing and produces a **petroleum feedstock/product category** for downstream industry.

For the current core economy, the broad output is named **Petroleum Products** rather than inventing multiple fuel cargoes.

```text
Oil
 ↓
Refinery
 ↓
Petroleum Products
```

### Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Output |
|---|---|---|---|---|---|---|---|---|
| PRC_REFINERY | Refinery | Processing | Petroleum | 1850–2150 | Oil | Industrial Equipment, Construction Materials | Medium / returnable | Petroleum Products |
| PRC_REFINERY_ADV | Advanced Refinery | Processing | Petroleum | 1980–2150 | Oil | Technology Systems, Industrial Equipment | Low–Medium / returnable | Petroleum Products |

## Chemical Works

Chemical Works converts appropriate feedstocks into the broad **Chemicals** product.

```text
Petroleum Products ─┐
                    ├→ Chemical Works → Chemicals
Gas ────────────────┘
```

Gas may remain a direct feedstock where historically/economically appropriate, but Chemical Works is no longer a duplicate refinery.

### Registry

| ID | Name | Role | Module | New Construction | Hard Inputs | Operational Supplies | Personnel | Output |
|---|---|---|---|---|---|---|---|---|
| PRC_CHEM | Chemical Works | Processing | Chemicals | 1850–2150 | Petroleum Products and/or Gas | Industrial Equipment, Technology Systems | Medium / returnable | Chemicals |
| PRC_CHEM_ADV | Advanced Chemical Works | Processing | Chemicals | 2000–2150 | Chemical feedstocks | Technology Systems, Industrial Equipment | Low / returnable | Chemicals |

## Fuel decision

Fuel remains **optional**, not core.

If a future Energy/Transport module introduces Fuel, it may become an additional Refinery output. That addition must preserve the distinction:

```text
Oil → Refinery → Petroleum Products / Fuel
                         ↓
                  Chemical Works
                         ↓
                     Chemicals
```

The core economy does not need Fuel merely to make petroleum processing work.

---

# 4. Revised Core Chains

## Construction

```text
Stone ─────────────┐
Clay ──────────────┤
Lumber ────────────┼→ Construction Materials
Steel ─────────────┘
```

## Copper

```text
Copper Ore
    ↓
Copper Works
    ↓
Copper
 ┌──┴──┐
 ↓     ↓
Machinery  Electronics
```

## Petroleum / Chemicals

```text
Oil
 ↓
Refinery
 ↓
Petroleum Products
 ↓
Chemical Works
 ↓
Chemicals
```

with an additional direct Gas → Chemical Works feed where justified.

---

# 5. Validation Consequences

These decisions close the three material findings as follows:

| Finding | Previous problem | Locked resolution | Validation status |
|---|---|---|---|
| Clay orphan | No definite core consumer | Clay feeds Construction Materials | **PASS** |
| Copper ambiguity | Undefined intermediate-copper stage | Add Copper Works and stable Copper product | **PASS** |
| Refinery/Chemical overlap | Duplicate Oil/Gas → Chemicals role | Refinery → Petroleum Products → Chemical Works → Chemicals | **PASS** |

The next validation pass should test the resulting dependency graph for cycles, excessive depth, hard-input overload, and unintended supply loops.

---

# 6. Source-of-Truth Rule

For implementation purposes, these locked decisions supersede earlier provisional statements that:

- describe Clay as only an optional ceramics/construction resource;
- route Copper Ore directly into manufacturing as a substitute for a processor;
- describe `intermediate-copper` without a defined producer;
- define Refinery as directly producing Chemicals;
- define Chemical Works as independently converting raw Oil/Gas into the same Chemicals output.

The existing framework documents remain useful historical/design records, but implementation work must follow this repair decision set until the documents are reconciled into their next canonical revision.

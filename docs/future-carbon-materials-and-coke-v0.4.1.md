# Coke and Future Carbon Materials — v0.4.1

## Decision

**Coke is a persistent industrial material across 1700–2299.** Coke Works must not be removed merely because later steelmaking technologies become available.

Coke production may change in importance, recipe, customers, and productivity. Those changes are represented as transformation or decline in a particular use-case—not as automatic extinction of the Coke Works sector.

## Economic distinction

- **Coal** is an extracted carbon-bearing resource with fuel, metallurgical, chemical, and materials uses.
- **Coke** is a processed carbon material produced by heating suitable coal or other qualified carbon feedstocks in controlled conditions.
- **Metallurgical coke** supports blast-furnace ironmaking as fuel, reducing-agent support, and a structural/permeability medium.
- **Foundry coke** supports metal casting and other high-temperature industrial processes.
- **Specialty carbon products** are distinct downstream products and must not be silently substituted for ordinary coke.

## Lifecycle treatment

| Element | Treatment |
|---|---|
| Coal extraction | Persistent resource; transforming and potentially declining energy role |
| Coke Works | Persistent industrial sector; transforming product mix |
| Metallurgical coke | Persistent while compatible ironmaking remains in the model |
| Foundry coke | Persistent niche product; may decline in later eras |
| Carbon-materials processing | Emerging future branch; additive to Coke Works, not a replacement by default |
| Synthetic diamond | Late technology-gated product; separate process and inputs |

## Future carbon-materials direction

The future model may introduce a broader carbon-processing family:

```text
Coal / Gas / Biomass / Recycled Carbon
                ↓
      Carbon Materials Processing
         ├── Metallurgical Coke
         ├── Foundry Coke
         ├── Industrial Carbon
         ├── Graphite
         ├── Carbon Fiber
         ├── Graphene
         └── Synthetic Diamond
```

This is a **design direction**, not an assertion that every branch is already implemented.

## No magical coal-to-diamond conversion

The model must not implement a simplistic `coal → diamond` recipe. Synthetic diamond represents advanced carbon-materials manufacturing and requires its own technology gate, process, energy, and industrial inputs. Carbon feedstock may be one input, but the game should not imply that ordinary coal naturally or directly becomes gem-quality diamond.

## Era intent

- **1700–1849:** coke emerges as a major industrial fuel/material alongside coal.
- **1850–1999:** coke is strongly tied to heavy industry, ironmaking, steelmaking, and foundries.
- **2000–2149:** coke remains available while electric, hydrogen, recycled-material, and alternative processes expand.
- **2150–2299:** Coke Works persists; conventional metallurgical demand may decline, while specialty carbon and advanced-material branches may grow.

## Implementation boundary

This document defines canonical economic intent only. It does not add NewGRF industries, cargoes, recipes, or callbacks. Those changes wait until the complete industry matrix, cargo graph, and validator rules are reconciled.

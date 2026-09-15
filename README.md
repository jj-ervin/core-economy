# Core Economy — OpenTTD Historical Transport Economy Framework

**Core Economy** is a modular, historical transport economy framework for [OpenTTD](https://www.openttd.org/). It provides canonical industry production chains, historical technology date gates, and material-balance production recipes.

The framework is packaged as an **optional, downloadable OpenTTD NewGRF mod** (`core_economy.grf`) that players can activate in their game.

---

## What is Core Economy?

Core Economy is designed as a **1700–2299 economy** made of four independently playable 150-year economic eras:

| Era | Years |
|---|---:|
| Era 1 — Early Industrial | 1700–1849 |
| Era 2 — Industrial & Mass Production | 1850–1999 |
| Era 3 — Advanced Global Economy | 2000–2149 |
| Era 4 — Future Economy | 2150–2299 |

Each era is intended to function as a coherent **mini-economy slice** that can be selected as a starting period. A full campaign can run continuously through all four eras.

### Industries persist by default

Core Economy does **not** treat each era as a replacement economy. Agriculture, forestry, construction, food production, logistics, and other foundational sectors are expected to persist while their technology, recipes, productivity, scale, and economic importance change.

Industry lifecycle classes are:

- `persistent`
- `transforming`
- `emerging`
- `declining`
- `phase_out`

A successor industry represents a technological/economic successor; it does **not** automatically mean the predecessor is destroyed when the successor appears.

### Construction economy

Construction is a persistent economic pillar. The planned construction-material chain includes timber/lumber, stone, aggregates, lime/cement, ceramics, glass, steel, and later engineered materials. **Cement is part of the planned canonical economy and will be implemented as part of that chain rather than as an isolated addition.**

### Economic geography

The long-term design treats distance, transport speed, capacity, and infrastructure as important economic constraints. Earlier eras should favor shorter regional supply chains; later eras should support longer-distance specialization and larger markets.

---

## Architecture

Core Economy separates the canonical economy from the runtime implementation:

```text
Canonical Economy
       │
       ├── NewGRF
       │    industries / cargo / recipes / production / date gates
       │
       └── Core Economy Dynamics (future GameScript)
            settlements / population / dynamic state / events
```

An external sidecar/Admin Port integration is **deferred** and is not required for the core economy.

The canonical economy is intentionally broader than the currently shipped NewGRF. See `data/implementation-manifest.json` for the authoritative implementation boundary.

---

## Current Release & Historical Slice (v0.4.0)

The v0.4.0 release implements the core **Historical Steelmaking Vertical Slice**:

```text
Coal Mine (1700) ----> Coal ─────+
                                  |
                                  v
                             Coke Works (1750) ──> Coke ────+
                                                            |
                                                            v
Iron Mine (1700) ────> Iron Ore ───────────────────> Steel Mill (1750) ──> Steel
```

### Date Gates & Availability
- **1700:** `Coal Mine` (`MIN_COAL_EARLY`) and `Iron Mine` (`MIN_IRON`) become available.
- **1750:** `Coke Works` (`PRC_COKE`) and `Steel Mill` (`PRC_STEEL`) become available.
- **Absolute Boundary:** Coke Works and Steel Mill use absolute engine location-check gates. They cannot be randomly spawned or manually funded prior to 1750.

**Important:** v0.4.0 is a prototype slice, not the complete 1700–2299 economy. The current NewGRF implements four industries; the larger canonical economy remains planned/specification data.

---

## Download & Installation

### Option A: Download Pre-compiled Release (Recommended)

1. Go to the [Core Economy Releases](https://github.com/jj-ervin/core-economy/releases) page on GitHub.
2. Download `core_economy.grf` or `core-economy-openttd-newgrf.zip`.
3. Extract and place `core_economy.grf` in your local OpenTTD `newgrf/` directory:
   - **Windows:** `%USERPROFILE%\Documents\OpenTTD\newgrf\`
   - **Linux:** `~/.local/share/openttd/newgrf/` or `~/.openttd/newgrf/`
   - **macOS:** `~/Documents/OpenTTD/newgrf/`

### Option B: Build Locally from Source

Requirements: Python 3 and the NML compiler (`nmlc`).

```bash
# Install NML compiler once
pip install nml

# Validate the canonical economy contract
python tools/validate_economy.py

# Assemble the modular NML and compile a local GRF
python tools/build_newgrf.py --compile
```

The local build produces:

```text
build/core_economy.grf
```

Copy that file to your OpenTTD `newgrf` directory and test it locally. **GitHub Actions is CI verification and release automation; it is not required to build or test the NewGRF.**

If you only want to regenerate the NML entry point without compiling:

```bash
python tools/build_newgrf.py
```

---

## How to Activate in OpenTTD

> **IMPORTANT:** Core Economy is an optional NewGRF. It **must be enabled before starting a NEW GAME**. NewGRF economy modifications cannot be safely added to an existing saved game.

1. Launch OpenTTD.
2. On the main menu, click **NewGRF Settings**.
3. Locate **Core Economy v0.4.0 - OpenTTD Vertical Slice** in the list of inactive NewGRFs.
4. Select it and click **Add** (moves it to Active NewGRFs).
5. Click **Apply Changes**.
6. Start a **New Game** (or generate a map starting in 1700 or later).

---

## Repository Structure

```text
data/reference-economy/   # Canonical economy contracts (JSON)
data/implementation-manifest.json # What is actually implemented/shipped
schema/                   # JSON schemas for cargoes, industries, recipes
validation/               # Validation rules and constraints
tools/                    # Contract validators and local build tooling
games/openttd/newgrf/     # NML source code and OpenTTD mapping docs
docs/architecture-v0.4.1.md # Runtime boundaries, era model, and design rules
.github/workflows/        # CI/CD and release automation workflows
```

---

## License

Core Economy is released under the **GNU General Public License v2.0 or later** (GPL-2.0-or-later). See [LICENSE](LICENSE) for details.

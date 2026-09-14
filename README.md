# Core Economy — OpenTTD Historical Transport Economy Framework

**Core Economy** is a modular, historical transport economy framework for [OpenTTD](https://www.openttd.org/). It provides canonical industry production chains, historical technology date gates, and material-balance production recipes.

The framework is packaged as an **optional, downloadable OpenTTD NewGRF mod** (`core_economy.grf`) that players can activate in their game.

---

## What is Core Economy?

Core Economy replaces or expands standard OpenTTD industries with historically grounded economic chains. It separates:
- **Canonical Economy Contract** (`data/reference-economy/`): JSON specifications of industries, cargoes, recipes, and eras.
- **OpenTTD NewGRF Adapter** (`games/openttd/newgrf/`): Compiled NML definitions mapping canonical definitions to OpenTTD graphics, callbacks, and cargo labels.

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

---

## Download & Installation

### Option A: Download Pre-compiled Release (Recommended)

1. Go to the [Core Economy Releases](https://github.com/jj-ervin/core-economy/releases) page on GitHub.
2. Download `core_economy.grf` or `core-economy-openttd-newgrf.zip`.
3. Extract and place `core_economy.grf` in your local OpenTTD `newgrf/` directory:
   - **Windows:** `%USERPROFILE%\Documents\OpenTTD\newgrf\`
   - **Linux:** `~/.local/share/openttd/newgrf/` or `~/.openttd/newgrf/`
   - **macOS:** `~/Documents/OpenTTD/newgrf/`

### Option B: Build from Source

Requirements: Python 3 and the NML compiler (`nmlc`).

```bash
# Install NML compiler
pip install nml

# Validate economy contract schema
python tools/validate_economy.py

# Compile NewGRF
nmlc -o games/openttd/newgrf/core_economy.grf --lang=games/openttd/newgrf/lang games/openttd/newgrf/core_economy.nml
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
schema/                   # JSON schemas for cargoes, industries, recipes
tools/                    # Contract validators (validate_economy.py)
games/openttd/newgrf/     # NML source code and OpenTTD mapping docs
.github/workflows/        # CI/CD and release automation workflows
```

---

## License

Core Economy is released under the **GNU General Public License v2.0 or later** (GPL-2.0-or-later). See [LICENSE](LICENSE) for details.

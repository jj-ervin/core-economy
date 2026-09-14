# Core Economy — OpenTTD NewGRF Installation & Usage Guide

**Core Economy v0.4.0** (OpenTTD Historical Steelmaking Vertical Slice)

---

## Installation

1. Copy `core_economy.grf` into your local OpenTTD `newgrf` folder:
   - **Windows:** `%USERPROFILE%\Documents\OpenTTD\newgrf\`
   - **Linux:** `~/.local/share/openttd/newgrf/` or `~/.openttd/newgrf/`
   - **macOS:** `~/Documents/OpenTTD/newgrf/`

2. Launch OpenTTD.
3. Open **NewGRF Settings** from the main menu.
4. Select **Core Economy v0.4.0 - OpenTTD Vertical Slice** and click **Add**.
5. Click **Apply Changes**.

---

## Game Requirements

- **Start a New Game:** NewGRFs that modify industries or cargoes **must be enabled before starting a NEW GAME**. Do not add to existing saved games.
- **Start Year:** Maps starting in year 1700 or later are supported.

---

## Historical Production Chains & Date Gates

### Available 1700
- **Coal Mine** (`MIN_COAL_EARLY`): Produces `Coal` (`COAL`).
- **Iron Mine** (`MIN_IRON`): Produces `Iron Ore` (`IORE`).

### Available 1750
- **Coke Works** (`PRC_COKE`): Accepts `Coal`, produces `Coke` (`COKE`).
- **Steel Mill** (`PRC_STEEL`): Accepts `Iron Ore` + `Coke`, produces `Steel` (`STEL`).

---

## License

This NewGRF is released under the **GNU General Public License v2.0 or later** (GPL-2.0-or-later).

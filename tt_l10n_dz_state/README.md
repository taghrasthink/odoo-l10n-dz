# 🇩🇿 Algeria - Administrative Division

**The definitive geographic database for Odoo in Algeria, updated according to the November 2025 administrative reforms.**

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo 17](https://img.shields.io/badge/Odoo-17.0-blueviolet)](https://github.com/taghrasthink/tt_l10n_dz_state/tree/17.0)
[![Odoo 18](https://img.shields.io/badge/Odoo-18.0-blueviolet)](https://github.com/taghrasthink/tt_l10n_dz_state/tree/18.0)
[![Odoo 19](https://img.shields.io/badge/Odoo-19.0-blueviolet)](https://github.com/taghrasthink/tt_l10n_dz_state/tree/19.0)

---

## Features

### 🏛️ 69 Wilayas
Includes all 58 standard wilayas plus the 11 new delegated wilayas from the 2025 reform.

### 🏘️ 1541 Communes
A complete database of communes linked directly to their respective wilayas. Dynamic filtering for error-free data entry.

### 📜 Ready for the 2025 Reform
Fully compliant with the ministerial decrees of **November 2025**. Official data, updated codes, and latest postal mapping.

### 🌍 Bilingual Support
Native support for **Latin** (French/English) and **Arabic**. Geographic names automatically adapt based on the user's language.

---

## Technical Details

| | |
|---|---|
| **Technical Name** | `tt_l10n_dz_state` |
| **Category** | Localization |
| **License** | LGPL-3 |
| **Dependencies** | `contacts`, `base_address_extended` |
| **Author** | TaghrasThink |

---

## Installation

1. Clone this repository into your Odoo addons directory:
   ```bash
   # For Odoo 18
   git clone -b 18.0 https://github.com/taghrasthink/tt_l10n_dz_state.git

   # For Odoo 17
   git clone -b 17.0 https://github.com/taghrasthink/tt_l10n_dz_state.git

   # For Odoo 19
   git clone -b 19.0 https://github.com/taghrasthink/tt_l10n_dz_state.git
   ```

2. Restart your Odoo server and update the apps list.

3. Search for **"Algeria - Administrative Division"** in Apps and install.

---

## What It Does

- Populates **69 states** (wilayas) for Algeria in `res.country.state`
- Populates **1541 cities** (communes) in `res.city`, each linked to its wilaya
- Enables `enforce_cities` on Algeria for structured address entry
- On partner forms:
  - Filters communes by selected wilaya
  - Shows the free-text city field alongside the commune dropdown
  - Dynamic placeholders: **Wilaya** / **البلدية** based on language and country
- Arabic translations for all 69 wilayas (applied via `post_init_hook`)

---

## Compatibility

| Edition | Odoo 17 | Odoo 18 | Odoo 19 |
|---------|:-------:|:-------:|:-------:|
| Community (CE) | ✅ | ✅ | ✅ |
| Enterprise (EE) | ✅ | ✅ | ✅ |

---

## Data Source

Geographic data sourced from [S450R1/algeria-cities-2025](https://github.com/S450R1/algeria-cities-2025).

---

## Author

Developed by **[TaghrasThink](https://github.com/taghrasthink)**

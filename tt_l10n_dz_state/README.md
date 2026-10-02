# 🇩🇿 Algeria - Administrative Division

**Wilayas and communes of Algeria for Odoo, following the November 2025 administrative reform.**

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo 17](https://img.shields.io/badge/Odoo-17.0-blueviolet)](https://github.com/taghrasthink/odoo-l10n-dz/tree/17.0)
[![Odoo 18](https://img.shields.io/badge/Odoo-18.0-blueviolet)](https://github.com/taghrasthink/odoo-l10n-dz/tree/18.0)
[![Odoo 19](https://img.shields.io/badge/Odoo-19.0-blueviolet)](https://github.com/taghrasthink/odoo-l10n-dz/tree/19.0)
[![Odoo 20](https://img.shields.io/badge/Odoo-20.0-blueviolet)](https://github.com/taghrasthink/odoo-l10n-dz/tree/20.0)

---

## Features

- **69 wilayas**: the 58 standard wilayas plus the 11 delegated wilayas created by the 2025 reform.
- **1541 communes**, each linked to its wilaya.
- **Bilingual names**: Latin script and Arabic, displayed according to the user's language.
- **Address entry on contacts**: the commune list is filtered by the selected wilaya, and the
  field placeholders read *Wilaya* / *Commune* (*الولاية* / *البلدية* in Arabic).

---

## What it does

- Creates the 69 states in `res.country.state` and the 1541 cities in `res.city`.
- Turns on **Enforce Cities** (`enforce_cities`) for Algeria, so addresses use the commune dropdown.
- On partner forms, filters communes by wilaya, clears the commune when the wilaya changes, and
  keeps the free-text *City* field available next to the dropdown.
- Applies the Arabic wilaya names at install time (`post_init_hook`); communes are translated
  through the `.po` files.
- Resets **Enforce Cities** on Algeria when the module is uninstalled.

---

## Installation

1. Clone the branch that matches your Odoo version into your addons directory:

   | Odoo | Command |
   |:----:|---------|
   | 17 | `git clone -b 17.0 https://github.com/taghrasthink/odoo-l10n-dz.git` |
   | 18 | `git clone -b 18.0 https://github.com/taghrasthink/odoo-l10n-dz.git` |
   | 19 | `git clone -b 19.0 https://github.com/taghrasthink/odoo-l10n-dz.git` |
   | 20 | `git clone -b 20.0 https://github.com/taghrasthink/odoo-l10n-dz.git` |

2. Add the cloned folder to `addons_path`, restart Odoo and update the apps list.
3. Install **Algeria - Administrative Division**.

Enable the Arabic language **before** installing the module: the Arabic wilaya names are
applied at install time, and skipped when Arabic is not yet active.

---

## Compatibility

| Edition | Odoo 17 | Odoo 18 | Odoo 19 | Odoo 20 |
|---------|:-------:|:-------:|:-------:|:-------:|
| Community (CE) | ✅ | ✅ | ✅ | ✅ |
| Enterprise (EE) | ✅ | ✅ | ✅ | ✅ |

The module only depends on `contacts` and `base_address_extended`. Odoo 20 itself requires
PostgreSQL 16 or later.

---

## Technical details

| | |
|---|---|
| **Technical name** | `tt_l10n_dz_state` |
| **Category** | Localization |
| **Dependencies** | `contacts`, `base_address_extended` |
| **License** | LGPL-3 |
| **Author** | [TaghrasThink](https://github.com/taghrasthink) |
| **Data source** | [S450R1/algeria-cities-2025](https://github.com/S450R1/algeria-cities-2025) |

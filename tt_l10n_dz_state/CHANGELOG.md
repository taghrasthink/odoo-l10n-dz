# Changelog

## 20.0.4.1.1

- Port to Odoo 20.0.
- Drop the 19.0 migration scripts (obsolete on a fresh 20.0 install).
- Fix: the Arabic post-install hook overwrote the Latin wilaya names when en_US is not an active language.
- Fix: the Wilaya/Municipality placeholders were never applied (res.partner guard evaluated before the record was loaded, and field edits did not re-trigger the update).

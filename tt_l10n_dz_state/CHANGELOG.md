# Changelog

## 17.0.4.1.1

- Fix: the Arabic post-install hook overwrote the Latin wilaya names when en_US is not an active language.
- Fix: the Wilaya/Municipality placeholders were never applied (res.partner guard evaluated before the record was loaded, and field edits did not re-trigger the update).

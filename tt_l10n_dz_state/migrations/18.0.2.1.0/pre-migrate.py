# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Remove orphaned menus from previous versions."""
    if not version:
        return

    _logger.info("tt_l10n_dz_state: cleaning up old menu entries...")

    # Collect all menu IDs owned by this module
    cr.execute("""
        SELECT imd.name, imd.res_id
        FROM ir_model_data imd
        WHERE imd.module = 'tt_l10n_dz_state'
          AND imd.model = 'ir.ui.menu'
    """)
    menu_rows = cr.fetchall()
    if not menu_rows:
        _logger.info("  No old menus found, nothing to clean.")
        return

    menu_ids = [row[1] for row in menu_rows]
    xml_ids = [row[0] for row in menu_rows]
    _logger.info("  Found %d old menus: %s", len(menu_ids), xml_ids)

    # Delete children first, then parents (recursive bottom-up)
    # Using a recursive CTE to find all descendant menus
    cr.execute("""
        WITH RECURSIVE menu_tree AS (
            SELECT id FROM ir_ui_menu WHERE id = ANY(%s)
            UNION ALL
            SELECT m.id FROM ir_ui_menu m
            JOIN menu_tree mt ON m.parent_id = mt.id
        )
        DELETE FROM ir_ui_menu WHERE id IN (SELECT id FROM menu_tree)
    """, (menu_ids,))
    deleted_menus = cr.rowcount
    _logger.info("  Deleted %d menu records (including children).", deleted_menus)

    # Clean up ir_model_data for this module's menus
    cr.execute("""
        DELETE FROM ir_model_data
        WHERE module = 'tt_l10n_dz_state'
          AND model = 'ir.ui.menu'
    """)
    _logger.info("  Cleaned ir_model_data entries.")

    # Also clean up old actions that no longer exist in XML
    old_actions = [
        'tt_action_l10n_dz_commune',
        'tt_action_l10n_dz_wilaya',
        'action_l10n_dz_commune',
        'action_l10n_dz_wilaya',
    ]
    for action_name in old_actions:
        cr.execute("""
            SELECT res_id FROM ir_model_data
            WHERE module = 'tt_l10n_dz_state'
              AND name = %s
              AND model = 'ir.actions.act_window'
        """, (action_name,))
        row = cr.fetchone()
        if row:
            cr.execute("DELETE FROM ir_act_window WHERE id = %s", (row[0],))
            cr.execute("""
                DELETE FROM ir_model_data
                WHERE module = 'tt_l10n_dz_state'
                  AND name = %s
            """, (action_name,))
            _logger.info("  Removed old action: %s", action_name)

    _logger.info("tt_l10n_dz_state: cleanup done.")

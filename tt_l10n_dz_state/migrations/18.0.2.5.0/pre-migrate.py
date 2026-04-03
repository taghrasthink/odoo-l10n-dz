# -*- coding: utf-8 -*-
# Part of tt_l10n_dz_state. See LICENSE file for full copyright and licensing details.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Remove orphaned menus and actions from previous versions."""
    if not version:
        return

    _logger.info("tt_l10n_dz_state: cleaning up old menu/action entries...")

    # --- Step 1: Find all menu IDs owned by this module ---
    cr.execute("""
        SELECT imd.name, imd.res_id
        FROM ir_model_data imd
        WHERE imd.module = 'tt_l10n_dz_state'
          AND imd.model = 'ir.ui.menu'
    """)
    menu_rows = cr.fetchall()

    if menu_rows:
        menu_ids = [row[1] for row in menu_rows]
        xml_ids = [row[0] for row in menu_rows]
        _logger.info("  Found %d module menus: %s", len(menu_ids), xml_ids)

        # --- Step 2: Re-parent any external child menus (from other modules) ---
        cr.execute("""
            UPDATE ir_ui_menu
            SET parent_id = NULL
            WHERE parent_id = ANY(%s)
              AND id != ALL(%s)
        """, (menu_ids, menu_ids))
        if cr.rowcount:
            _logger.info("  Re-parented %d external child menus.", cr.rowcount)

        # --- Step 3: Delete menus bottom-up (children before parents) ---
        # Use recursive CTE to find all descendants, then delete deepest first
        cr.execute("""
            WITH RECURSIVE menu_tree AS (
                SELECT id, parent_id, 0 AS depth
                FROM ir_ui_menu WHERE id = ANY(%s)
                UNION ALL
                SELECT m.id, m.parent_id, mt.depth + 1
                FROM ir_ui_menu m
                JOIN menu_tree mt ON m.parent_id = mt.id
            )
            SELECT id FROM menu_tree ORDER BY depth DESC
        """, (menu_ids,))
        ordered_ids = [row[0] for row in cr.fetchall()]

        for menu_id in ordered_ids:
            cr.execute("DELETE FROM ir_ui_menu WHERE id = %s", (menu_id,))
        _logger.info("  Deleted %d menu records.", len(ordered_ids))

        # --- Step 4: Clean ir_model_data for menus ---
        cr.execute("""
            DELETE FROM ir_model_data
            WHERE module = 'tt_l10n_dz_state'
              AND model = 'ir.ui.menu'
        """)
        _logger.info("  Cleaned menu ir_model_data entries.")

    # --- Step 5: Remove old/obsolete actions ---
    old_actions = [
        'tt_action_l10n_dz_commune',
        'tt_action_l10n_dz_wilaya',
        'tt_action_l10n_dz_region',
        'tt_action_l10n_dz_daira',
        'action_l10n_dz_commune',
        'action_l10n_dz_wilaya',
        'action_l10n_dz_region',
        'action_l10n_dz_daira',
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
            action_id = row[0]
            # Remove any menu referencing this action first
            cr.execute("""
                UPDATE ir_ui_menu SET action = NULL
                WHERE action = CONCAT('ir.actions.act_window,', %s::text)
            """, (action_id,))
            cr.execute("DELETE FROM ir_act_window WHERE id = %s", (action_id,))
            cr.execute("""
                DELETE FROM ir_model_data
                WHERE module = 'tt_l10n_dz_state' AND name = %s
            """, (action_name,))
            _logger.info("  Removed old action: %s (id=%s)", action_name, action_id)

    _logger.info("tt_l10n_dz_state: cleanup done.")

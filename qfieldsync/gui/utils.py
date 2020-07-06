# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QFieldSyncDialog
                                 A QGIS plugin
 Sync your projects to QField on android
                             -------------------
        begin                : 2020-06-15
        git sha              : $Format:%H$
        copyright            : (C) 2020 by OPENGIS.ch
        email                : info@opengis.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

def set_available_actions(combobox, layer_source):
    """Sets available actions on a checkbox and selects the current one.

    Args:
        combobox (QComboBox): target combobox
        layer_source (LayerSource): target layer
    """
    for action, description in layer_source.available_actions:
        combobox.addItem(description)
        combobox.setItemData(combobox.count() - 1, action)

        if layer_source.action == action:
            combobox.setCurrentIndex(combobox.count() - 1)

# -*- coding: utf-8 -*-
"""
Intercambia items entre  dos ListWidgets de PyQt5

06-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class PasaItemsListwidgetListwidget:
    """Intercambia items entre  dos ListWidgets de PyQt5."""

    def __init__(self):
        pass

    def listwidget1_listwidget2(self, lsw_1, lsw_2):
        """Pasa los items seleccionados de listWidget_1 a listWidget_2."""

        for item in lsw_1.selectedItems():
            lsw_2.addItem(item.text())  # Añade item a lsw_2.
            lsw_1.takeItem(lsw_1.row(item))  # Elimina items de lsw_1.

        lsw_1.sortItems()  # Ordena items de lsw_1.
        lsw_2.sortItems()  # Ordena items de lsw_2.

    def todos_listwidget1_listwidget2(self, lsw_1, lsw_2):
        """Pasa todos los items listWidget_1 a listWidget_2."""

        for idx in range(lsw_1.count()):  # Añade items a lsw_2.
            idx = lsw_1.item(idx).text()
            lsw_2.addItem(idx)

        lsw_2.sortItems()  # Ordena items de lsw_2.
        lsw_1.clear()  # Elimina items de lsw_1.

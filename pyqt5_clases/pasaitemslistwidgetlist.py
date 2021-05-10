# -*- coding: utf-8 -*-
"""
Intercambia items entre ListWidget de PyQt5 y list de python

06-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

class PasaItemsListwidgetList:
    """Intercambia items entre ListWidget de PyQt5 y list de python."""

    def __init__(self, listwidget, lista):
        """Inicializa listwidget y lista."""

        self.listwidget = listwidget  # listWidget.
        self.lista = lista  # Lista de python

    def lista_listwidget(self):
        """Pasa items de una lista de python a un listWidget de PyQt5."""

        for item in self.lista:
            self.listwidget.addItem(item)

    def listwidget_lista(self):
        """Pasa items de un QlistWidget de PyQt5 a una lista de python."""

        self.lista = [
            self.listwidget.item(i).text() for i in range(
                self.listwidget.count()
            )
        ]

        return self.lista
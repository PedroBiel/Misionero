# -*- coding: utf-8 -*-
"""
MISIONERO
Modelo del diálogo de fichero

29-04-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from PyQt5 import QtGui

class ListModel:
    """Modelo de la lista de los ficheros Escel."""

    def __init__(self, ficheros):
        """
        :param ficheros: list ; lista con los ficheros Excel.
        """

        self.ficheros = ficheros

        self.model = QtGui.QStandardItemModel()

    def modelo(self):
        """Pasa los datos de la lista al modelo."""

        for fichero in self.ficheros:
            item = QtGui.QStandardItem(fichero)
            self.model.appendRow(item)

        return self.model

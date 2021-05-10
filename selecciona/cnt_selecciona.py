# -*- coding: utf-8 -*-
"""
MISIONERO
Controlador de la selección de ficheros

07-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from pyqt5_clases.pasaitemslistwidgetlistwidget import \
    PasaItemsListwidgetListwidget


class CntSelecciona:
    """Controlador de la selección de ficheros."""

    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""

        self.v = ventana

        self.pasa_items = PasaItemsListwidgetListwidget()

    def selecciona_ficheros(self):
        """Selecciona los ficheros para incluir en la base de datos."""

        self.pasa_items.listwidget1_listwidget2(
            self.v.lsw_ficheros, self.v.lsw_sql
        )

        mensaje = 'Ficheros seleccionados.'
        self.v.statusbar.showMessage(mensaje)

    def selecciona_todos_ficheros(self):
        """Selecciona todos los ficheros para incluir en la base de datos."""

        self.pasa_items.todos_listwidget1_listwidget2(
            self.v.lsw_ficheros, self.v.lsw_sql
        )

        mensaje = 'Todos los ficheros seleccionados.'
        self.v.statusbar.showMessage(mensaje)

    def deselecciona_ficheros(self):
        """Deselecciona los ficheros para incluir en la base de datos."""

        self.pasa_items.listwidget1_listwidget2(
            self.v.lsw_sql, self.v.lsw_ficheros
        )

        mensaje = 'Ficheros deseleccionados.'
        self.v.statusbar.showMessage(mensaje)

    def deselecciona_todos_ficheros(self):
        """Deselecciona todos los ficheros xlsx para incluir en la base de datos."""

        self.pasa_items.todos_listwidget1_listwidget2(
            self.v.lsw_sql, self.v.lsw_ficheros
        )

        mensaje = 'Todos los ficheros deseleccionados.'
        self.v.statusbar.showMessage(mensaje)

# -*- coding: utf-8 -*-
"""
MISIONERO
Transfiere los datos de las hojas Excel del directorio indicado a una base de
datos SQLite.

22-04-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import QLibraryInfo, QLocale, QTranslator
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QMainWindow

import qdarkstyle

from fichero.cnt_fichero import CntFichero
from fichero.dlg_tabla import DlgTabla
from selecciona.cnt_selecciona import CntSelecciona
from sql.cnt_sql import CntSQL


class MainWindow(QMainWindow):
    """
    Transfiere los datos de las hojas Excel del directorio indicado a una base
    de datos SQLite.
    """

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/misionero.ui', self)

        # Entorno virtual
        print('\nEntorno virtual:', sys.prefix)
        print('python', sys.version)
        print('qdarkstyle', qdarkstyle.__version__)

        # Icono y título de la ventana.
        self.setWindowIcon(QIcon("iconos/christian_icon.ico"))
        self.setWindowTitle("Misionero 0.0.0 beta")

        # Instancias de clase.
        self.cnt_fichero = CntFichero(self)
        self.cnt_selecciona = CntSelecciona(self)
        self.cnt_sql = CntSQL(self)

        # QObjects.
        self.rbt_csv_coma = self.radioButtonCSVComa
        self.rbt_csv_punto_coma = self.radioButtonCSVPuntoComa
        self.rbt_xls = self.radioButtonXLS
        self.rbt_xlsx = self.radioButtonXLSX
        self.rbt_tbl_fich = self.radioButtonTablaFichero
        self.rbt_tbl_db = self.radioButtonTablaBaseDatos
        self.btn_directorio = self.pushButtonDirectorio
        self.lsw_ficheros = self.listWidgetFicheros
        # Permite selección múltiple.
        self.lsw_ficheros.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.lsw_ficheros.setAcceptDrops(True)
        # self.lsw_ficheros.setDragEnabled(True)
        self.lsw_sql = self.listWidgetToSQL
        self.lsw_sql.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        # self.lsw_sql.setAcceptDrops(True)
        # self.lsw_sql.setDragEnabled(True)
        self.btn_selecciona = self.pushButtonSelecciona
        self.btn_selecciona_todos = self.pushButtonSeleccionaTodos
        self.btn_deselecciona = self.pushButtonDeselecciona
        self.btn_deselecciona_todos = self.pushButtonDeseleccionaTodos
        self.btn_convierte = self.pushButtonConvierte
        self.lbl_mensaje = self.labelMensaje
        fuente = QFont()
        fuente.setFamily('Consolas')
        fuente.setPointSize(8)
        self.lbl_mensaje.setFont(fuente)
        self.statusBar().setFont(fuente)

        # Variables.
        self.ruta = ''  # Ruta del directorio con los ficheros.
        self.ficheros = []  # Lista con los fichero del directorio.
        self.ruta_nombre_db = ''  # Ruta del directorio con el nombre de la base de datos.
        self.ficheros_db = []  # Lista con los ficheros a exportar en las tablas de la base de datos.
        self.nombre_tabla = ''  # nombre de la tabla única.

        # Eventos.
        self.btn_directorio.clicked.connect(
            self.cnt_fichero.directorio
        )
        self.btn_selecciona.clicked.connect(
            self.cnt_selecciona.selecciona_ficheros
        )
        self.btn_selecciona_todos.clicked.connect(
            self.cnt_selecciona.selecciona_todos_ficheros
        )
        self.btn_deselecciona.clicked.connect(
            self.cnt_selecciona.deselecciona_ficheros
        )
        self.btn_deselecciona_todos.clicked.connect(
            self.cnt_selecciona.deselecciona_todos_ficheros
        )
        self.btn_convierte.clicked.connect(
            self.cnt_sql.convierte_ficheros
        )

    # Salidas PyQt5.

    # Mensaje.
    def salida_mensaje(self, mensaje):
        """Salida del mensaje."""

        self.lbl_mensaje.setText(mensaje)

    # Diálogo tabla.
    def call_dialogo_tabla(self, tabla=None):
        """Llama al diálogo tabla"""

        self.dlg_tabla = DlgTabla(self)
        self.dlg_tabla.show()

    def get_dialogo_tabla(self):
        """Getter del nombre de la tabla del diálogo."""

        self.nombre_tabla = self.dlg_tabla.get_tabla()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Traducir el idiona del sistema operativo y texto predeterminado de PyQt.
    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    )
    app.installTranslator(qt_translator)

    # Dark style.
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # Fuente.
    fuente = QFont()
    fuente.setFamily('Consolas')
    fuente.setPointSize(11)
    app.setFont(fuente)

    # Ejecuta aplicación.
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

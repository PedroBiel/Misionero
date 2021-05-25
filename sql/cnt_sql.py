# -*- coding: utf-8 -*-
"""
MISIONERO
Controlador de la conversión de los ficheros a la base de datos SQL

07-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from sql.constantes_sql import Constantes
from sql.dts_tablassql import TablasSQL
from sql.dts_basedatos import BaseDatos

from pyqt5_clases.qfiledialog import FileDialog
from pyqt5_clases.pasaitemslistwidgetlist import PasaItemsListwidgetList


class CntSQL:
    """Controlador de la conversión de los ficheros a la base de datos SQL."""

    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""

        self.v = ventana

    def get_ruta(self):
        """Getter de la ruta del directorio con los ficheros."""

        return self.v.ruta

    def get_ficheros(self):
        """Getter de los ficheros del directorio."""

        return self.v.ficheros

    def get_ficheros_sql(self):
        """Getter de los ficheros a exportar en las tablas SQL."""

        pasa_items = PasaItemsListwidgetList(
            self.v.lsw_sql, self.v.ficheros_db
        )
        self.v.ficheros_db = pasa_items.listwidget_lista()

    def get_ruta_nombre_db(self):
        """
        Obtiene la ruta y el nombre del fichero a guardar de FileDialog.
        Type : str
        """
        constantes = Constantes()
        subtitulo = constantes.get_guardar_datos()
        tipo_fichero = constantes.get_tipo_ficheros_db()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        self.v.ruta_nombre_db = pfad.get_save_file_name()

        return self.v.ruta_nombre_db

    def tablas_sql(self):
        """
        Lista con las tablas de la base de datos.
        Cada fichero se corresponde con una tabla de la base de datos.
        """

        tablas_sql = TablasSQL(self.v.ficheros_db)
        tablas = tablas_sql.get_tablas()

        return tablas

    def modelos_sql(self):
        """
        Lista con los modelos de la base de datos.
        Caso de una tabla única y el nombre de cada fichero se
        incluye en una nueva columna de la tabla de la base de datos.
        """

        tablas_sql = TablasSQL(self.v.ficheros_db)
        modelos = tablas_sql.get_modelos()

        return modelos

    def convierte_ficheros(self):
        """Convierte los ficheros seleccionados en una base de datos."""

        mensaje = 'Exportando datos...'
        self.v.statusbar.showMessage(mensaje)

        if self.v.rbt_tbl_fich.isChecked():
            self.multiples_tablas()
        elif self.v.rbt_tbl_db.isChecked():
            self.unica_tabla()

        mensaje = 'Datos exportados.'
        self.v.statusbar.showMessage(mensaje)

        mensaje = 'Tus archivos ya están en la senda correcta.'
        self.v.salida_mensaje(mensaje)

    def multiples_tablas(self):
        """Por cada fichero se crea una tabla dentro de la base de datos."""

        self.get_ficheros_sql()
        self.get_ruta_nombre_db()
        tablas = self.tablas_sql()
        try:
            db = BaseDatos(
                self.v.rbt_csv_coma,
                self.v.rbt_csv_punto_coma,
                self.v.rbt_xls,
                self.v.rbt_xlsx,
                self.v.ruta,
                self.v.ficheros_db,
                tablas,
                self.v.ruta_nombre_db
            )
            db.base_datos_1()
        except EOFError as e:
            print('EOFError: {e}')

    def unica_tabla(self):
        """
        Todos los ficheros se agrupan en una única tabla dentro de la base de
        datos.
        """

        self.v.get_dialogo_tabla()
        self.get_ficheros_sql()
        self.get_ruta_nombre_db()
        modelos = self.modelos_sql()
        try:
            db = BaseDatos(
                self.v.rbt_csv_coma,
                self.v.rbt_csv_punto_coma,
                self.v.rbt_xls,
                self.v.rbt_xlsx,
                self.v.ruta,
                self.v.ficheros_db,
                modelos,
                self.v.ruta_nombre_db
            )
            db.base_datos_2(self.v.nombre_tabla)
        except EOFError as e:
            print('EOFError: {e}')

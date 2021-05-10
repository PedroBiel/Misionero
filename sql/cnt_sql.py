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

        ruta_nombre_db = self.get_ruta_nombre_db()
        print(ruta_nombre_db)

        ficheros = self.get_ficheros()
        tablas_sql = TablasSQL(ficheros)
        tablas = tablas_sql.get_tablas()

        return tablas

    def convierte_ficheros(self):
        """Convierte los ficheros seleccionados en una base de datos."""

        # TODO implementar la conversión de los ficheros xlsx en la base de datos
        print('hola convierte_ficheros')

        mensaje = 'Exportando datos...'
        self.v.statusbar.showMessage(mensaje)

        ficheros = self.get_ficheros()
        print(self.v.ruta_nombre_db)
        tablas = self.tablas_sql()
        print(tablas)
        db = BaseDatos(
            self.v.rbt_csv,
            self.v.rbt_xls,
            self.v.rbt_xlsx,
            self.v.ruta,
            ficheros,
            tablas,
            self.v.ruta_nombre_db
        )
        db.base_datos()



        mensaje = 'Datos exportados.'
        self.v.statusbar.showMessage(mensaje)


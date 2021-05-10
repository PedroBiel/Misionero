# -*- coding: utf-8 -*-
"""
MISIONERO
Pasa los datos de ficheros a tablas la base de datos SQL

07-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import pandas as pd

from transferenciadatos.pandasdfsqlite import PandasDFSQLite


class BaseDatos:
    """
    Pasa los datos de los ficheros a tablas de datos SQL.
    Comprueba la extensión de los ficheros, los convierta a DataFrames
    de pandas y éstos los pasa a una tabla de la base de datos.
    """

    def __init__(self, rbt_csv, rbt_xls, rbt_xlsx, ruta, ficheros, tablas,
                 ruta_nombre_db):
        """
        :param rbt_csv: radioButton ; ficheros csv.
        :param rbt_xls: radioButton ; ficheros xls.
        :param rbt_xlsx: radioButton ; ficheros xlsx.
        :param ruta : str ; ruta de los ficheros.
        :param ficheros: list ; lista con los ficheros a convertir.
        :param tablas: list ; lista con los nombre de las tablas de la base de datos.
        :param ruta : str ; ruta y nombre de la base de datos.
        """

        self.rbt_csv = rbt_csv
        self.rbt_xls = rbt_xls
        self.rbt_xlsx = rbt_xlsx
        self.ruta = ruta
        self.ficheros = ficheros
        self.tablas = tablas
        self.ruta_nombre_db = ruta_nombre_db

    def base_datos(self):
        """Crea la base de datos."""

        print('\nbase_datos')
        # ruta = r'H:\COMUN MT\5.CE\Codigo fuente\Python\Apps\Misionero\Misionero_0_0_0\xls_pruebas'
        # print(self.ficheros)
        # excel = ruta + '\\' + self.ficheros[0]
        # print(excel)
        # df = pd.read_excel(excel)
        # print(df)


        for fichero, tabla in zip(self.ficheros, self.tablas):
            print(fichero, '|', tabla)
            ruta_fichero = self.ruta + '\\' + fichero
            if self.rbt_csv.isChecked():
                print('rbt_csv.isChecked')
                try:
                    df = pd.read_table(ruta_fichero, delimiter=',')
                except ValueError as e:
                    print(f'ValueError: {e}')
            else:
                print('rbt_xls.isChecked')
                try:
                    df = pd.read_excel(ruta_fichero)
                except ValueError as e:
                    print(f'ValueError: {e}')

            try:
                df_sql = PandasDFSQLite(self.ruta_nombre_db, df, tabla)
                df_sql.df_to_sql()
            except ValueError as e:
                print(f'ValueError: {e}')
            else:
                print('Done!')


if __name__ == '__main__':

    print('\nbase_datos')
    ruta = r'H:\COMUN MT\5.CE\Codigo fuente\Python\Apps\Misionero\Misionero_0_0_0\xls_pruebas'
    nombre = 'ShipLoader 0_0_04 fem1.xls'
    excel = ruta + '\\' + nombre
    print(excel)
    df = pd.read_excel(excel)
    print(df)

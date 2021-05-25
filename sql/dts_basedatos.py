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

    def __init__(self, rbt_csv_c, rbt_csv_pc, rbt_xls, rbt_xlsx, ruta,
                 ficheros_db, tablas, ruta_nombre_db
                 ):
        """
        :param rbt_csv_c: radioButton ; ficheros csv con separador = ','.
        :param rbt_csv_pc: radioButton ; ficheros csv con separador = ';'.
        :param rbt_xls: radioButton ; ficheros xls.
        :param rbt_xlsx: radioButton ; ficheros xlsx.
        :param ruta : str ; ruta de los ficheros.
        :param ficheros_db: list ; lista con los ficheros a convertir.
        :param tablas: list ; lista con los nombre de las tablas de la base de datos.
        :param ruta : str ; ruta y nombre de la base de datos.
        """

        self.rbt_csv_coma = rbt_csv_c
        self.rbt_csv_punto_coma = rbt_csv_pc
        self.rbt_xls = rbt_xls
        self.rbt_xlsx = rbt_xlsx
        self.ruta = ruta
        self.ficheros_db = ficheros_db
        self.tablas = tablas
        self.ruta_nombre_db = ruta_nombre_db

    def base_datos_1(self):
        """Crea la base de datos con múltiples tablas."""

        # print('\nbase_datos_1')

        for fichero, tabla in zip(self.ficheros_db, self.tablas):
            ruta_fichero = self.ruta + '\\' + fichero
            if self.rbt_csv_coma.isChecked():
                try:
                    df = pd.read_table(ruta_fichero, delimiter=',')
                except ValueError as e:
                    print(f'ValueError: {e}')
            elif self.rbt_csv_punto_coma.isChecked():
                try:
                    df = pd.read_table(ruta_fichero, delimiter=';')
                except ValueError as e:
                    print(f'ValueError: {e}')
            else:
                try:
                    df = pd.read_excel(ruta_fichero)
                except ValueError as e:
                    print(f'ValueError: {e}')

            try:
                df_sql = PandasDFSQLite(self.ruta_nombre_db, df, tabla)
                df_sql.df_to_sql()
            except ValueError as e:
                print(f'ValueError: {e}')

    def base_datos_2(self, nombre_tabla):
        """Crea la base de datos con una única tabla."""

        modelos = self.tablas
        df = pd.DataFrame()

        for fichero, modelo in zip(self.ficheros_db, modelos):
            ruta_fichero = self.ruta + '\\' + fichero
            if self.rbt_csv_coma.isChecked():
                try:
                    dfi = pd.read_table(ruta_fichero, delimiter=',')
                    dfi['Modelo'] = modelo
                    df = pd.concat([df, dfi], ignore_index=True)
                except ValueError as e:
                    print(f'ValueError: {e}')
            elif self.rbt_csv_punto_coma.isChecked():
                try:
                    dfi = pd.read_table(ruta_fichero, delimiter=';')
                    dfi['Modelo'] = modelo
                    df = pd.concat([df, dfi], ignore_index=True)
                except ValueError as e:
                    print(f'ValueError: {e}')
            else:
                try:
                    dfi = pd.read_excel(ruta_fichero)
                    dfi['Modelo'] = modelo
                    df = pd.concat([df, dfi], ignore_index=True)
                except ValueError as e:
                    print(f'ValueError: {e}')

        mod = df['Modelo']
        df.drop(labels=['Modelo'], axis=1, inplace=True)
        df.insert(0, 'Modelo', mod)

        try:
            df_sql = PandasDFSQLite(self.ruta_nombre_db, df, nombre_tabla)
            df_sql.df_to_sql()
        except ValueError as e:
            print(f'ValueError: {e}')

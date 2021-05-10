# -*- coding: utf-8 -*-
"""
MISIONERO
Constantes para el diálogo de fichero

22-04-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class Constantes:
    """Valores constantes para el diálogo de fichero."""
    
    def __init__(self):
        """Crea constantes ABRIR_DATOS y TIPO_FICHEROS."""
    
        self.__SELECCIONAR_DIRECTORIO = 'Seleccionar directorio'
        self.__ABRIR_DATOS = 'Abrir datos'
        self.__TIPO_FICHEROS_DB = 'Tipo de ficheros (*.db)'
        self.__GUARDAR_EXCEL = 'Guardar hoja Excel'
        self.__TIPO_FICHEROS_CSV = 'Tipo de ficheros (*.csv)'
        self.__TIPO_FICHEROS_XLS = 'Tipo de ficheros (*.xls)'
        self.__TIPO_FICHEROS_XLSX = 'Tipo de ficheros (*.xlsx)'
        self.__GUARDAR_DATOS = 'Guardar datos de implantaciones'
        self.__EXTENSION_CSV = 'csv'
        self.__EXTENSION_XLS = 'xls'
        self.__EXTENSION_XLSX = 'xlsx'

    def get_seleccionar_directorio(self):
        """Getter de SELECCIONAR DIRECTORIO."""

        return self.__SELECCIONAR_DIRECTORIO

    def get_abrir_datos(self):
        """Getter de ABRIR_DATOS."""
        
        return self.__ABRIR_DATOS
    
    def get_tipo_ficheros_db(self):
        """Getter de TIPO_FICHEROS_DB."""
        
        return self.__TIPO_FICHEROS_DB
    
    def get_guardar_excel(self):
        """Getter de GUARDAR_EXCEL."""
        
        return self.__GUARDAR_EXCEL
    
    def get_tipo_ficheros_csv(self):
        """Getter de TIPO_FICHEROS_CSV."""
        
        return self.__TIPO_FICHEROS_CSV

    def get_tipo_ficheros_xls(self):
        """Getter de TIPO_FICHEROS_XLS."""

        return self.__TIPO_FICHEROS_XLS

    def get_tipo_ficheros_xlsx(self):
        """Getter de TIPO_FICHEROS_XLSX."""

        return self.__TIPO_FICHEROS_XLSX
    
    def get_guardar_datos(self):
        """Getter de GUARDAR_DATOS."""
        
        return self.__GUARDAR_DATOS

    def get_extension_csv(self):
        """Getter de EXTENSION_CSV."""

        return self.__EXTENSION_CSV

    def get_extension_xls(self):
        """Getter de EXTENSION_XLS."""

        return self.__EXTENSION_XLS

    def get_extension_xlsx(self):
        """Getter de EXTENSION_XLSX."""

        return self.__EXTENSION_XLSX

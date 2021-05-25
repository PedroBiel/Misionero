# -*- coding: utf-8 -*-
"""
MISIONERO
Datos del diálogo de fichero

Created on Tue Apr 27 14:30 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import os

class FicherosRuta:
    """Obtiene una lista con los ficheros de la ruta."""

    def __init__(self, ruta, extension):
        """
        :param ruta: str; directorio con los ficheros.
        :param extension: str; extensión de los ficheros.
        """

        self.ruta = ruta
        self.extension = extension

    def ficheros(self):
        """Lista con los ficheros del directorio."""

        try:
            os.chdir(self.ruta)
            os.getcwd()
            list_dir = os.listdir(self.ruta)
            ficheros = [
                fichero for fichero in list_dir if self.extension in fichero
            ]
        except EOFError as e:
            print('EOFError: {e}')

        return ficheros



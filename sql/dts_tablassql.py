# -*- coding: utf-8 -*-
"""
MISIONERO
Lista con las tablas de la base de datos SQL

07-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class TablasSQL:
    """Lista con las tablas de la base de datos."""

    def __init__(self, ficheros):
        """Inicializa la lista de los ficheros."""

        self.ficheros = ficheros

    def idx_carcater_string(self, fichero: str, caracter='.'):
        """Encuentra el índice de caracter en string."""

        try:
            idx = fichero.index(caracter)

        except ValueError as e:
            print('ValueError:', e)

        return idx

    def elimina_extension(self, fichero: str, idx: int):
        """Elimina la extensión del nombre del fichero en el índice idx."""

        try:
            return fichero[:idx]

        except ValueError as e:
            print('ValueError:', e)

    def prepara_string(self, fichero: str):
        """
        Prepara el string para que la base de datos tome el nombre:
        - Sustituye espación en blanco por guiones bajos.
        - Elimina tildes.
        - Carácteres en mayúsculas.
        """

        try:
            fichero = fichero.replace(' ', '_')
            for i, j in zip('áéíóúüÁÉÍÓÚÜ', 'aeiouuaeiouu'):
                fichero = fichero.replace(i, j)
            fichero = fichero.upper()

        except ValueError as e:
            print('ValueError:', e)

        return fichero

    def get_tablas(self):
        """Lita con las tablas de las bases de datos."""

        tablas = []
        for fichero in self.ficheros:
            idx = self.idx_carcater_string(fichero)
            fichero = self.elimina_extension(fichero, idx)
            fichero = self.prepara_string(fichero)
            tablas.append(fichero)

        tablas.sort()

        return tablas

    def get_modelos(self):
        """Lita con los modelos de las bases de datos."""

        modelos = []
        for fichero in self.ficheros:
            idx = self.idx_carcater_string(fichero)
            fichero = self.elimina_extension(fichero, idx)
            modelos.append(fichero)

        modelos.sort()

        return modelos


if __name__ == '__main__':

    ficheros = [
        'ShipLoader 0_0_04 fem1.xls', 'ShipLoader 0_0_04 fem2.xls',
        'ShipLoader 0_0_04 fem3.xls', 'ShipLoader 0_d10_04 fem1.xls',
        'ShipLoader 0_d10_04 fem2.xls', 'ShipLoader 0_d10_04 fem3.xls',
        'ShipLoader 0_u15_04 fem1.xls', 'ShipLoader 0_u15_04 fem2.xls',
        'ShipLoader 0_u15_04 fem3.xls'
        ]

    string = 'ab cd áéü.ext'
    tablas_sql = TablasSQL(ficheros)

    idx = tablas_sql.idx_carcater_string(string)
    print(idx)
    fichero = tablas_sql.elimina_extension(string, idx)
    print(fichero)
    fich = tablas_sql.prepara_string(fichero)
    print(fich)

    tbl = tablas_sql.get_tablas()
    print(tbl)

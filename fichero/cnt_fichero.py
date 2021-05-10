# -*- coding: utf-8 -*-
"""
MISIONERO
Controlador del diálogo de fichero

22-04-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from fichero.constantes_fichero import Constantes
from fichero.dts_fichero import FicherosRuta

from pyqt5_clases.qfiledialog import FileDialog
from pyqt5_clases.pasaitemslistwidgetlist import PasaItemsListwidgetList


class CntFichero:
    """
    Controlador de la clase QFileDialog proporciona un cuadro de diálogo que 
    permite seleccionar archivos o directorios.
    """

    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""

        self.v = ventana

    def directorio(self):
        """Directorio con los ficheros."""

        self.v.lsw_ficheros.clear()
        self.v.lsw_sql.clear()

        # Ruta de los ficheros.
        constantes = Constantes()
        subtitulo = constantes.get_seleccionar_directorio()
        file_dialog = FileDialog(subtitulo, '', '')
        self.v.ruta = file_dialog.get_existing_directory()
        print(self.v.ruta)

        # Ficheros en la ruta.
        extension = ''
        if self.v.rbt_csv.isChecked():
            extension = constantes.get_extension_csv()
        if self.v.rbt_xls.isChecked():
            extension = constantes.get_extension_xls()
        if self.v.rbt_xlsx.isChecked():
            extension = constantes.get_extension_xlsx()

        ficheros_ruta = FicherosRuta(self.v.ruta, extension)
        self.v.ficheros = ficheros_ruta.ficheros()
        print(self.v.ficheros)

        # listWidget con los ficheros.
        pasa_items = PasaItemsListwidgetList(
            self.v.lsw_ficheros, self.v.ficheros
        )
        pasa_items.lista_listwidget()

        # Mensaje de tarea realizada.
        mensaje = 'Lista de ficheros.'
        self.v.statusbar.showMessage(mensaje)

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
        try:
            constantes = Constantes()
            subtitulo = constantes.get_seleccionar_directorio()
            file_dialog = FileDialog(subtitulo, '', '')
            self.v.ruta = file_dialog.get_existing_directory()
        except EOFError as e:
            print('EOFError: {e}')

        # Ficheros en la ruta.
        extension = ''
        if self.v.rbt_csv_coma.isChecked():
            extension = constantes.get_extension_csv()
        if self.v.rbt_xls.isChecked():
            extension = constantes.get_extension_xls()
        if self.v.rbt_xlsx.isChecked():
            extension = constantes.get_extension_xlsx()

        if self.v.ruta != '':
            ficheros_ruta = FicherosRuta(self.v.ruta, extension)
            self.v.ficheros = ficheros_ruta.ficheros()

        # listWidget con los ficheros.
        if self.v.ficheros != '':
            pasa_items = PasaItemsListwidgetList(
                self.v.lsw_ficheros, self.v.ficheros
            )
            pasa_items.lista_listwidget()

        # ¿Es una única tabla?
        if self.v.rbt_tbl_db.isChecked():
            self.tabla_unica()

        # Mensaje de tarea realizada.
        mensaje = 'Lista de ficheros.'
        self.v.statusbar.showMessage(mensaje)

    def tabla_unica(self):
        """Llama al diálogo para obtener el nombre de la tabla única."""

        self.v.call_dialogo_tabla(self.v.nombre_tabla)

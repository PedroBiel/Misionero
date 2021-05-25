"""
MISIONERO
Diálogo del nombre de la tabla única

13-05-2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from sql.cnt_sql import CntSQL

class DlgTabla(QDialog):
    """Diálodo del nombre de la tabla única."""

    print('DlgTabla')

    def __init__(self,  parent=None):
        """Inicializa el diálogo."""

        QDialog.__init__(self, parent)
        uic.loadUi('../vistas/dlg_tabla.ui', self)

        # Objetos de la aplicación.
        self.tabla = ''

        # Instancias de las clases.
        self.cnt_sql = CntSQL(self)

        # Widgets PyQt5.
        self.lne_tabla = self.lineEditNombreTabla
        self.btn_aceptar = self.pushButtonAceptar
        self.btn_rechazar = self.pushButtonRechazar

        # Titulo del diálogo.
        self.setWindowTitle('Tabla única')

        # Eventos.
        self.btn_aceptar.clicked.connect(self.acepta)
        self.btn_rechazar.clicked.connect(self.rechaza)

    def acepta(self):
        """Acepta el nombre de la tabla."""

        self.tabla = self.lne_tabla.text()
        self.close()

    def rechaza(self):
        """Rechaza el nombre de la tabla."""

        self.close()

    def get_tabla(self):
        """Getter del nombre de la tabla."""

        return self.tabla


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    myapp = DlgTabla()
    myapp.show()
    sys.exit(app.exec_())

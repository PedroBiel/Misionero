# -*- coding: utf-8 -*-


class EliminaItemLista:
    """Elimina item de lista QlistWidget."""

    def __init__(self, item, lst):

        self.item = item  # Item a eliminar.
        self.lst = lst  # Lista QlistWidget.

    def elimina_item(self):

        try:

            items = [str(self.lst.item(i).text())
                     for i in range(self.lst.count())
                     ]  # Pasa los items de QlistWidget a una lista.
            items.remove(self.item)  # Elimina el iten de la lista.
            self.lst.clear()  # Borra QlistWidget original.
            self.lst.addItems(items)  # Pasa los items a la QlistWidget.

        except Exception:

            print('El item a eliminar no está en la lista.')


class PasaItems_lista_lst:
    """Pasa items de una lista de Python a una lista QlistWidget."""

    def __init__(self, lista, lst):

        self.lista = lista  # Lista Python.
        self.lst = lst  # Lista QlistWidget.

    def lista_lst(self):

        for item in self.lista:

            self.lst.addItem(item)


class PasaItems_lst_lista:
    """Pasa items de una lista QlistWidget a una lista de Python."""

    def __init__(self, lst):

        self.lst = lst  # Lista QlistWidget.
        self.lista = []  # Lista Python.

    def lst_lista(self):

        self.lista = [self.lst.item(i).text() for i in range(self.lst.count())]

        return self.lista


class PasaItems_lst_lst:
    """Intercambio de items entre listas QListWidget."""

    def __init__(self, lst_1, lst_2):

        self.lst_1 = lst_1  # Lista 1.
        self.lst_2 = lst_2  # Lista 2.

    def lst_lst(self):  # Pasa items de la lista lst_1 a la lista lst_2.

        for item in self.lst_1.selectedItems():

            self.lst_2.addItem(item.text())  # Añade items a lst_2.
            self.lst_1.takeItem(self.lst_1.row(item))  # Elimina items de lst_1.

        self.lst_2.sortItems()  # Ordena items en lst_2.

    def pasa_todos_items(self):  # Pasa todos los items de la lista lst_1 a la lista lst_2.

        for index in range(self.lst_1.count()):  # Añade items a lst_2.

            index = self.lst_1.item(index).text()
            self.lst_2.addItem(index)

        self.lst_2.sortItems()  # Ordena items en lst_2.
        self.lst_1.clear()  # Elimina items de lst_1.


class PasaItems_lst_ln:
    """
    Intercambio de items de una lista QListWidget y una linea QLineEdit.
    """

    def __init__(self, lst, ln):

        self.lst = lst  # Lista.
        self.ln = ln  # Línea.
        self.str_nudos = ''  # String con la lista de nudos para implantación.
        self.str_nudos_temp = ''  # String temporal.

    def lst1_ln(self):
        """Pasa un item de una lista QListWidget a una linea QLineEdit."""

        if self.ln.text() == '':  # Comprueba si ln está en blanco.

            self.settext_takeitem()

        else:  # ln no está en blanco.

            self.add_sort_clear()
            self.settext_takeitem()

    def lst_ln(self):
        """Pasa items de una lista QListWidget a una linea QLineEdit."""

        ln_text = self.ln.text()  # Conserva los datos de ln.

        for selected_item in self.lst.selectedItems():

            self.str_nudos_temp += selected_item.text() + ' '  # Nuevos datos de lst.
            self.lst.takeItem(self.lst.row(selected_item))  # Elimina item de lst.

        self.str_nudos = ln_text + self.str_nudos_temp

        self.ln.clear()
        self.ln.setText(self.str_nudos)

    def ln1_lst(self):
        """Pasa item de una linea QLineEdit a una lista QListWidget."""

        if self.ln.text() == '':  # Comprueba si ln está en blanco.

            pass

        else:  # ln no está en blanco.

            self.add_sort_clear()

    def ln_lst(self):
        """
        Pasa items de una línea QLineEdit separados por espacios a una lista
        QListWidget.
        """

        for item in self.ln.text().split():

            self.lst.addItem(item)

        self.ln.clear()

    def settext_takeitem(self):
        """Copia item en ln y elimina item de list."""

        self.ln.setText(self.lst.currentItem().text())  # Copia item en ln.

        for selected_item in self.lst.selectedItems():  # Elimina items de lst.

            self.lst.takeItem(self.lst.row(selected_item))

    def add_sort_clear(self):
        """
        Devuelve item de ln a lst, ordena items en lst y borra item de ln.
        """

        self.lst.addItem(self.ln.text())  # Devuelve el item a lst.
        self.lst.sortItems()  # Ordena items de lst.
        self.ln.clear()  # Borra item de ln.


class ComboBox:
    """Operaciones con el widget QComboBox."""

    def __init__(self, cbx):

        self.cbx = cbx

    def item_text_current_index(self):
        """Obtiene el texto del item seleccionado."""

        current_idx = self.cbx.currentIndex()
        item = self.cbx.itemText(current_idx)

        return item

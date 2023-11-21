from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


import sys
import csv
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout,QComboBox, QPushButton, QMessageBox, QTextEdit
from time import sleep
from Pizzeria.Gui.gui import PizzeriaApp
from Pizzeria.Csv.csv import Csv
from Pizzeria.Builder.director import Director
from Pizzeria.Builder.builderPizza import BuilderPizza


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass
    

class Pizza(Component):

    def __init__(self, pizza) -> None:
        #Si la pizza es una pizza predeterminada del menu, retornamos el tipo de pizza
        if pizza in ['Margarita', 'Barbacoa', '4 quesos', 'Carbonara', 'Vegetariana', 'Prosciuto', 'Ninguna']:
            self.ingredientes = pizza
        else:
            #Si no, es una pizza personalizada, y retornamos los ingredientes
            app = QApplication(sys.argv)
            ventana = PizzeriaApp()
            ventana.show()
            app.exec_()   
            
            print('Procesando su pedido...')
            sleep(2)

            director = Director()
            builder = BuilderPizza(ventana.getSeleccion())
            director.builder = builder

            director.build_pizza()
            builder.pizza.list_parts()


    #Esta funcion sera llamada como crear_pizza (o no) en un futuro (primero me tengo que aclarar xd)
    def operation(self) -> Pizza:
        return self


class Bebida(Component):

    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes

    def operation(self) -> str:
        return self
    

class Postre(Component):

    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes

    def operation(self) -> str:
        return self


class Entrada(Component):
    
    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes

    def operation(self) -> str:
        return self
    

class Menu(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        # Función para obtener el último ID del archivo CSV
        def obtener_ultimo_id(archivo_csv):
            try:
                with open(archivo_csv, 'r', newline='') as archivo:
                    lector_csv = csv.reader(archivo)
                    lineas = list(lector_csv)
                    return len(lineas)
            except:
                return 1  # Si el archivo no existe, el primer ID será 0

        escribir_csv = []

        id = obtener_ultimo_id('Ejercicio1/pedidos_menu.csv')
        escribir_csv.append(id)

        print('Su menu es:')
        for child in self._children:
            print(child.ingredientes)
            escribir_csv.append(child.ingredientes)

        #Escribimos el menu en un csv
        with open('Ejercicio1/pedidos_menu.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(escribir_csv)
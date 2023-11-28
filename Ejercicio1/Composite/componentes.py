from __future__ import annotations
import sys
from PyQt5.QtWidgets import QApplication
from time import sleep
from Pizzeria.Gui.gui import PizzeriaApp
from Pizzeria.Builder.director import Director
from Pizzeria.Builder.builderPizza import BuilderPizza
from Composite.component import Component



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
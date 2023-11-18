import sys
from PyQt5.QtWidgets import QApplication
from time import sleep
from Pizzeria.Gui.gui import PizzeriaApp
from Pizzeria.Csv.csv import Csv
from Pizzeria.Builder.director import Director
from Pizzeria.Builder.builderPizza import BuilderPizza

class Lanzador():
    def __init__(self) -> None:
        pass

    def lanzar(self) -> None:
        app = QApplication(sys.argv)
        ventana = PizzeriaApp()
        ventana.show()
        app.exec_()   
            
        print('Procesando su pedido...')
        sleep(2)

        director = Director()
        builder = BuilderPizza(ventana.get_seleccion())
        director.builder = builder

        director.build_pizza()
        builder.pizza.list_parts()
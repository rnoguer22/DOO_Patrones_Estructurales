import sys
from PyQt5.QtWidgets import QApplication
from time import sleep
from Gui.gui import PizzeriaApp
from Csv.csv import Csv
from Builder.director import Director
from Builder.builderPizza import BuilderPizza

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
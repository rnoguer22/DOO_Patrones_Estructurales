import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from interface import Interface_Menu
from Pizzeria.lanzador import LanzadorPizzeria

class Lanzador(QWidget):

    def lanzar(self):
        app = QApplication(sys.argv)
        lanzador = QMessageBox.question(self, 'Delizioso', '¿Desea menu?',
                                 QMessageBox.Yes | QMessageBox.No)
        #Si decimos que si, agregamos la salsa recomendada correspondiente
        if lanzador == QMessageBox.Yes:   
            ventana = Interface_Menu()
            ventana.show()
            app.exec_() 
            if ventana.getSeleccion()[1] == 'Pizza: Margarita':
                director = Director()
                builder = BuilderPizza(ventana.getSeleccion())
                director.builder = builder

                director.build_pizza()
                builder.pizza.list_parts()
        else:
            lanzadorPizzeria = LanzadorPizzeria()
            lanzadorPizzeria.lanzar()
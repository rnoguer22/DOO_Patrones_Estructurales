import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from interface import Interface_Menu
from Pizzeria.lanzador import LanzadorPizzeria
from Pizzeria.Builder.director import Director
from Pizzeria.Builder.builderPizza import BuilderPizza  


class Lanzador(QWidget):

    def lanzar(self):
        app = QApplication(sys.argv)
        lanzador = QMessageBox.question(self, 'Delizioso', '¿Desea menu?',
                                 QMessageBox.Yes | QMessageBox.No)
        #Si decimos que si, lanzamos la interfaz del menu
        if lanzador == QMessageBox.Yes:   
            ventana = Interface_Menu()
            ventana.show()
            app.exec_() 
            #LLamamos a la clase director para hacer un builder y asi construir la pizza
            director = Director()
            #Creamos una lista con los ingredientes de cada pizza
            if ventana.getSeleccion()[1] == 'Pizza: Margarita':
                ingredientes = ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Tomate', 'Albahaca', 'Orégano', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: Barbacoa':
                ingredientes = ['Masa Fina', 'Salsa Barbacoa', 'Queso Mozarella', 'Carne Picada', 'Cebolla', 'Bacon', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: 4 quesos':
                ingredientes = ['Masa Gruesa', 'Salsa Tomate', 'Queso Mozarella', 'Queso Parmesano', 'Queso Cheddar', 'Queso Provolone', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: Carbonara':
                ingredientes = ['Masa Gruesa', 'Salsa Carbonara', 'Queso Mozarella', 'Bacon', 'Cebolla', 'Huevo', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: Vegetariana':
                ingredientes = ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Champiñones', 'Cebolla', 'Pimiento', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: Prosciuto':
                ingredientes = ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Jamón', 'Orégano', 'Champiñones', 'Horno', 'Caja de Cartón']
            elif ventana.getSeleccion()[1] == 'Pizza: Ninguna':
                QMessageBox.warning(self, 'Delizioso', 'No ha seleccionado ninguna pizza')
            
            #Control de excepciones para manejar errores en la seleccion de ingredientes
            try:
                #De esta manera construimos nuestra pizza elegida en el menu
                builder = BuilderPizza(ingredientes)
            except:
                QMessageBox.warning(self, 'Delizioso', 'Ha habido un error con su menu, intentelo de nuevo')

            director.builder = builder
            director.build_pizza_menu()
            print(builder.pizza.parts)

        else:
            lanzadorPizzeria = LanzadorPizzeria()
            lanzadorPizzeria.lanzar()
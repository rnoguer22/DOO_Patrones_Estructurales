import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from Composite.Interface.interface import Interface_Menu
from Pizzeria.lanzador import LanzadorPizzeria
from Pizzeria.Builder.director import Director
from Pizzeria.Builder.builderPizza import BuilderPizza  
from Composite.componentes import Pizza, Bebida, Postre, Entrada
from Composite.menu import Menu
from Composite.Precio.precio import Precio
import random
import time


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
            precio = Precio()
            #Creamos una lista con los ingredientes de cada pizza
            if ventana.getSeleccion()[1] == 'Pizza: Margarita':
                ingredientes = precio.tipos_pizzas['Margarita']
            elif ventana.getSeleccion()[1] == 'Pizza: Barbacoa':
                ingredientes = precio.tipos_pizzas['Barbacoa']
            elif ventana.getSeleccion()[1] == 'Pizza: 4 quesos':
                ingredientes = precio.tipos_pizzas['4 quesos']
            elif ventana.getSeleccion()[1] == 'Pizza: Carbonara':
                ingredientes = precio.tipos_pizzas['Carbonara']
            elif ventana.getSeleccion()[1] == 'Pizza: Vegetariana':
                ingredientes = precio.tipos_pizzas['Vegetariana']
            elif ventana.getSeleccion()[1] == 'Pizza: Prosciuto':
                ingredientes = precio.tipos_pizzas['Prosciuto']
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

            lista_menu = []
            for elemento in ventana.getSeleccion():
                # Vamos a dividir cada elemento por los dos puntos y acceder al segundo elemento (índice 1)
                # Luego eliminamos los espacios en blanco adicionales con strip()
                contenido = elemento.split(':', 1)[1].strip()
                lista_menu.append(contenido)
            
            #Creamos el menu con los elementos seleccionados
            menu = Menu()
            entrada = Entrada(lista_menu[0])
            pizza = Pizza(lista_menu[1])
            bebida = Bebida(lista_menu[2])
            postre = Postre(lista_menu[3])
            menu.add(entrada)
            menu.add(pizza)
            menu.add(bebida)
            menu.add(postre)
            #Mostramos el menu por pantalla
            print('\nProcesando su menu...')
            time.sleep(2)
            print('Su menu es: ', ', '.join(lista_menu))
            menu.operation()

        #Si decimos que no, lanzamos la interfaz de la pizzeria
        elif lanzador == QMessageBox.No:
            lanzadorPizzeria = LanzadorPizzeria()
            lanzadorPizzeria.lanzar()
        
        print('Duracion estimada del pedido: ', random.randint(1, 59), ' minutos')
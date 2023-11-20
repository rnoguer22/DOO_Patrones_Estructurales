import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout,QComboBox, QPushButton, QMessageBox, QTextEdit

class MenuPizza(QWidget):

    def __init__(self):
        super().__init__()

        self.entrantes_disponibles = ["Ensalada", "Pan de ajo", "Palitos de queso", "Alitas de pollo", "Ninguno"]
        self.pizzas_disponibles = ["Margarita", "Barbacoa", "4 quesos", "Prosciuto", "Vegetariana", "Ninguna"]
        self.bebidas_disponibles = ["Cerveza", "Vino", "Refresco", "Agua", "Ninguno"]
        self.postres_disponibles = ["Tiramisu", "Helado", "Brownie", "Ninguno"]

        self.seleccion = []

        self.iniciar_gui()
    
    def iniciar_gui(self):
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        label = QLabel("Seleccione su menu: ")
        layout_horizontal1.addWidget(label)

        # Lista desplegable para seleccionar el entrante
        box_entrantes = QComboBox(self)
        box_entrantes.addItems(self.entrantes_disponibles)
        layout_horizontal2.addWidget(box_entrantes)        
        
        # Lista desplegable para seleccinar la pizza
        box_pizzas = QComboBox(self)
        box_pizzas.addItems(self.pizzas_disponibles)
        layout_horizontal2.addWidget(box_pizzas)

        # Lista desplegable para seleccinar la bebida
        box_bebidas = QComboBox(self)
        box_bebidas.addItems(self.bebidas_disponibles)
        layout_horizontal2.addWidget(box_bebidas)

        # Lista desplegable para seleccinar los postres
        box_postres = QComboBox(self)
        box_postres.addItems(self.postres_disponibles)
        layout_horizontal2.addWidget(box_postres)

        


        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        self.setLayout(layout_vertical)

        self.show()

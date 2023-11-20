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
    
    
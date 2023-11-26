import csv
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from Datos.guardar import Guardar

class Interface_Documents(QWidget):

    def __init__(self):
        super().__init__()

        self.dialogo = QMessageBox()
        self.dialogo.setWindowTitle("Inicio")
        self.dialogo.setText("Desea crear un nuevo documento o modificar uno existente?")

        # Agregamos los botones para crear o modificar
        crear_archivo = QPushButton("Crear archivo")
        modificar_archivo = QPushButton("Modificar archivo")
        self.dialogo.addButton(crear_archivo, QMessageBox.YesRole)
        self.dialogo.addButton(modificar_archivo, QMessageBox.NoRole)
        
        self.dialogo.exec_()

        # Verificar qué botón fue presionado
        if self.dialogo.clickedButton() == crear_archivo:
            self.dialogo.close()
            self.crearArchivo()
        elif self.dialogo.clickedButton() == modificar_archivo:
            self.modificarArchivo()
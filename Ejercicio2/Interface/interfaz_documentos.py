import csv
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox
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
    

    def crearArchivo(self):
        #Creamos los layouts
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()

        #Agregamos los elementos a los layouts
        label_name = QLabel("Nombre del archivo: ")
        name = QLineEdit()
        name.setPlaceholderText("Nombre")
        layout_horizontal1.addWidget(label_name)
        layout_horizontal1.addWidget(name)

        label_type = QLabel("Tipo de archivo: ")
        tipos = {"Texto":".txt",
                 "Imagen":".png", 
                 "Video":".mp4", 
                 "Audio":".mp3"}
        tipo = QComboBox()
        tipo.addItems(tipos.keys())
        layout_horizontal2.addWidget(label_type)
        layout_horizontal2.addWidget(tipo)

        label_content = QLabel("Contenido del archivo: ")
        content = QLineEdit()
        content.setPlaceholderText("Contenido")
        layout_horizontal3.addWidget(label_content)
        layout_horizontal3.addWidget(content)

        confirmar = QPushButton("Confirmar")
        cancelar = QPushButton("Cancelar")
        confirmar.clicked.connect(lambda: self.guardarArchivo(name.text(), tipos[tipo.currentText()], content.text()))
        cancelar.clicked.connect(self.close)
        layout_horizontal4.addWidget(confirmar)
        layout_horizontal4.addWidget(cancelar)

        #Agregamos los layouts al layout vertical
        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)
        layout_vertical.addLayout(layout_horizontal4)

        self.setLayout(layout_vertical)

        self.show()

    
    def guardarArchivo(self, nombre, tipo, contenido):
        datos = [nombre, tipo, contenido]
        # Guardamos los datos en el archivo CSV
        guardar = Guardar('Ejercicio2/Datos/txt_doc.csv')
        guardar.guardar(datos)
        self.close()



app = QApplication(sys.argv)
interfaz = Interface_Documents()
app.exec_()

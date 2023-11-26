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
        self.crear_archivo = QMessageBox()
        self.crear_archivo.setWindowTitle("Crear archivo")
        self.crear_archivo.setText("¿Que tipo de archivo desea crear?")

        # Agregamos los botones para crear o modificar
        crear_carpeta = QPushButton("Carpeta")
        crear_documento = QPushButton("Documento")
        crear_link = QPushButton("Enlace")
        self.crear_archivo.addButton(crear_carpeta, QMessageBox.YesRole)
        self.crear_archivo.addButton(crear_documento, QMessageBox.NoRole)
        self.crear_archivo.addButton(crear_link, QMessageBox.NoRole)
        
        self.crear_archivo.exec_()

        # Verificar qué botón fue presionado
        if self.crear_archivo.clickedButton() == crear_carpeta:
            self.crear_archivo.close()
            self.crearArchivo()
        elif self.crear_archivo.clickedButton() == crear_documento:
            self.crear_archivo.close()
            self.crearDocumento()
        elif self.crear_archivo.clickedButton() == crear_link:
            self.crear_archivo.close()
            self.crearArchivo()


    def crearDocumento(self):
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
        confirmar.clicked.connect(lambda: self.guardarArchivo([name.text(), tipos[tipo.currentText()], content.text()], 'txt_doc.csv'))
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

    
    def guardarArchivo(self, datos, nombre_archivo):
        # Guardamos los datos en el archivo CSV
        guardar = Guardar('Ejercicio2/Datos/{}'.format(nombre_archivo))
        guardar.guardar(datos)
        QMessageBox.information(self, "Archivo", "Archivo creado correctamente")
        self.close()

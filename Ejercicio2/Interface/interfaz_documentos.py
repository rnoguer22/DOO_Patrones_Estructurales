import csv
import sys
import pandas as pd
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
            self.seleccionarArchivo()
        elif self.dialogo.clickedButton() == modificar_archivo:
            self.seleccionarArchivoModificar()

    def seleccionarArchivoModificar(self):
        self.crear_archivo = QMessageBox()
        self.crear_archivo.setWindowTitle("Modificar archivo")
        self.crear_archivo.setText("¿Que archivo desea modificar?")

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
            self.modificarArchivo("carpeta")
        elif self.crear_archivo.clickedButton() == crear_documento:
            self.crear_archivo.close()
            self.modificarArchivo("documento")
        elif self.crear_archivo.clickedButton() == crear_link:
            self.crear_archivo.close()
            self.modificarArchivo("enlace")  


    def modificarArchivo(self, tipo_archivo):
        #Creamos los layouts
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()

        #Agregamos los elementos a los layouts
        label_name = QLabel(f"{tipo_archivo} a modificar: ")
        name = QComboBox(self)
        layout_horizontal1.addWidget(label_name)
        layout_horizontal1.addWidget(name)

        if tipo_archivo == "documento":
            archivo_csv = "documentos.csv"
        elif tipo_archivo == "carpeta":
            archivo_csv = "carpetas.csv"
        elif tipo_archivo == "enlace":
            archivo_csv = "enlaces.csv"
        
        df = pd.read_csv('Ejercicio2/Datos/{}'.format(archivo_csv))
        lista_nombres = df['nombre'].tolist()
        name.addItems(lista_nombres)

        layout_vertical.addLayout(layout_horizontal1)
        self.setLayout(layout_vertical)
        self.show()
    

    def seleccionarArchivo(self):
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
            self.crearArchivo("carpeta")
        elif self.crear_archivo.clickedButton() == crear_documento:
            self.crear_archivo.close()
            self.crearArchivo("documento")
        elif self.crear_archivo.clickedButton() == crear_link:
            self.crear_archivo.close()
            self.crearArchivo("enlace")


    def crearArchivo(self, tipo_archivo):
        #Creamos los layouts
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()

        #Agregamos los elementos a los layouts
        label_name = QLabel(f"Nombre {tipo_archivo}: ")
        name = QLineEdit()
        name.setPlaceholderText("Nombre")
        archivo_csv = "carpetas.csv"
        if tipo_archivo == "enlace":
            label_name = QLabel("Enlace: ")
            name.setPlaceholderText("Enlace a otro archivo")
            archivo_csv = "enlaces.csv"
        layout_horizontal1.addWidget(label_name)
        layout_horizontal1.addWidget(name)

        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        if tipo_archivo == "documento":
            archivo_csv = "documentos.csv"
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

            layout_vertical.addLayout(layout_horizontal2)
            layout_vertical.addLayout(layout_horizontal3)            

        confirmar = QPushButton("Confirmar")
        cancelar = QPushButton("Cancelar")
        confirmar.clicked.connect(lambda: self.guardarArchivo([name.text(), tipos[tipo.currentText()], content.text()], archivo_csv) if tipo_archivo == "documento" else self.guardarArchivo([name.text()], archivo_csv))
        cancelar.clicked.connect(self.close)
        layout_horizontal4.addWidget(confirmar)
        layout_horizontal4.addWidget(cancelar)

        #Agregamos los demas layouts al layout vertical
        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal4)

        self.setLayout(layout_vertical)
        self.show()

    
    def guardarArchivo(self, datos, nombre_archivo):
        # Guardamos los datos en el archivo CSV
        guardar = Guardar('Ejercicio2/Datos/{}'.format(nombre_archivo))
        guardar.guardar(datos)
        QMessageBox.information(self, "Archivo", "Archivo creado correctamente")
        self.close()
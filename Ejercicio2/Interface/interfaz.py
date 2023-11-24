import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from Datos.guardar import Guardar

class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.dialogo = QMessageBox()
        self.dialogo.setWindowTitle("Inicio")
        self.dialogo.setText("¿Deseas registrarte o ya dispones de una cuenta?")

        # Agregamos los botones para registrarse o hacer el inicio de sesion
        registro = QPushButton("Registrarse")
        inicio_sesion = QPushButton("Iniciar sesion")
        self.dialogo.addButton(registro, QMessageBox.YesRole)
        self.dialogo.addButton(inicio_sesion, QMessageBox.NoRole)
        
        self.dialogo.exec_()

        # Verificar qué botón fue presionado
        if self.dialogo.clickedButton() == registro:
            self.dialogo.close()
            self.registrarse()
        elif self.dialogo.clickedButton() == inicio_sesion:
            self.iniciar_sesion()


    def registrarse(self):
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        label = QLabel("Introduce tu nombre de usuario: ")
        layout_horizontal1.addWidget(label)
        # Campo de texto para introducir el nombre de usuario
        self.nombre_usuario = QLineEdit()
        layout_horizontal1.addWidget(self.nombre_usuario)

        label_contrasena = QLabel("Introduce tu contraseña: ")
        layout_horizontal2.addWidget(label_contrasena)
        # Campo de texto para introducir la contraseña
        self.contrasena = QLineEdit()
        self.contrasena.setEchoMode(QLineEdit.Password)
        layout_horizontal2.addWidget(self.contrasena)

        # Botón para confirmar el registro
        boton_confirmar = QPushButton("Confirmar")
        boton_confirmar.clicked.connect(self.confirmar_registro)
        layout_horizontal3.addWidget(boton_confirmar)

        # Botón para cancelar el registro
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.clicked.connect(self.cancelar_registro)
        layout_horizontal3.addWidget(boton_cancelar)

        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        self.setLayout(layout_vertical)
        self.setWindowTitle("Registro")
        self.show()

    def confirmar_registro(self):
        datos = [self.nombre_usuario.text(), self.contrasena.text()]
        # Guardamos los datos en el archivo CSV
        guardar = Guardar('Ejercicio2/Datos/usuarios.csv')
        guardar.guardar(datos)
        # Mostramos un mensaje de confirmación
        QMessageBox.information(self, "Registro", "Registro completado correctamente")
        self.close()
        
    def cancelar_registro(self):
        self.nombre_usuario.setText("")
        self.contrasena.setText("")
        QMessageBox.information(self, "Registro", "Registro cancelado")
        self.close()


    def iniciar_sesion(self):
        print('Con este metodo iniciaremos sesion')
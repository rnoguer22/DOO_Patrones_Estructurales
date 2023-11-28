import csv
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from Datos.guardar import Guardar

class Interface(QWidget):

    def __init__(self):
        super().__init__()
        self.acceso = False

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
        self.ventana('Registrarse')
        self.repetir_contrasena = QLineEdit()
        self.repetir_contrasena.setPlaceholderText("Repetir contraseña")
        self.repetir_contrasena.setEchoMode(QLineEdit.Password)
        self.layout_horizontal2.addWidget(self.repetir_contrasena)


    def iniciar_sesion(self):
        self.ventana('Iniciar sesión')


    def ventana(self, titulo):
        self.titulo = titulo
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        self.layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        label = QLabel("Introduce tu nombre de usuario: ")
        layout_horizontal1.addWidget(label)
        # Campo de texto para introducir el nombre de usuario
        self.nombre_usuario = QLineEdit()
        self.nombre_usuario.setPlaceholderText("usuario")
        layout_horizontal1.addWidget(self.nombre_usuario)

        label_contrasena = QLabel("Introduce tu contraseña: ")
        self.layout_horizontal2.addWidget(label_contrasena)
        # Campo de texto para introducir la contraseña
        self.contrasena = QLineEdit()
        self.contrasena.setPlaceholderText("contraseña")
        self.contrasena.setEchoMode(QLineEdit.Password)
        self.layout_horizontal2.addWidget(self.contrasena)

        # Botón para confirmar el registro
        boton_confirmar = QPushButton("Confirmar")
        boton_confirmar.clicked.connect(self.confirmar_registro)
        layout_horizontal3.addWidget(boton_confirmar)

        # Botón para cancelar el registro
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.clicked.connect(self.cancelar_registro)
        layout_horizontal3.addWidget(boton_cancelar)

        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(self.layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        self.setLayout(layout_vertical)
        self.setWindowTitle(titulo)
        self.show()
    

    def confirmar_registro(self):
        datos = [self.nombre_usuario.text(), self.contrasena.text()]
        if self.titulo == 'Registrarse':
            if datos[0] == '' or datos[1] == '':
                QMessageBox.warning(self, "Registro", "Por favor, introduce usuario y contraseña")
                self.acceso = False
                self.close()
            elif datos[1] != self.repetir_contrasena.text():
                QMessageBox.warning(self, "Registro", "Las contraseñas no coinciden")
                self.acceso = False
                self.close()
            else:
                # Guardamos los datos en el archivo CSV
                guardar = Guardar('Ejercicio2/Datos/usuarios.csv')
                guardar.guardar(datos)
                # Mostramos un mensaje de confirmación
                QMessageBox.information(self, "Registro", "Registro completado correctamente")
                self.close()
        elif self.titulo == 'Iniciar sesión':
            self.verificar_credenciales(datos[0], datos[1])
        self.close()
        

    def cancelar_registro(self):
        self.nombre_usuario.setText("")
        self.contrasena.setText("")
        QMessageBox.information(self, "Registro", "Registro cancelado")
        self.close()


    def verificar_credenciales(self, user, password):
        if user == '' or password == '':
            QMessageBox.warning(self, "Inicio de sesión", "Por favor, introduce usuario y contraseña")
            self.acceso = False
            return False
        try:
            with open('Ejercicio2/Datos/usuarios.csv', 'r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                for linea in lector_csv:
                    if user == linea[1] and password == linea[2]:
                        QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
                        #Los usuarios con id par son los que tienen acceso a los documentos, para modificarlos, eliminarlos, etc.
                        if int(linea[0]) % 2 != 0:
                            self.acceso = True
                        else:
                            QMessageBox.warning(self, "Inicio de sesión", "Este usuario no tiene acceso a los documentos")
                        return self.acceso
            QMessageBox.warning(self, "Inicio de sesión", "Credenciales inválidas, recuerde registrarse previamente antes de iniciar sesion")
            self.acceso = False
            return False
        except FileNotFoundError:
            QMessageBox.warning(self, "Inicio de sesión", "No se encontró el archivo de usuarios")
            self.acceso = False
            return False


    def getUser(self):
        return self.nombre_usuario.text()

    def getPassword(self):
        return self.contrasena.text()
    
    def getAcceso(self):
        return self.acceso
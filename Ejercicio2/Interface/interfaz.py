import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton

class Interface(QWidget):

    def __init__(self):
        super().__init__()

        dialogo = QMessageBox()
        dialogo.setWindowTitle("Inicio")
        dialogo.setText("¿Deseas registrarte o ya dispones de una cuenta?")

        # Agregamos los botones para registrarse o hacer el inicio de sesion
        registro = QPushButton("Registrarse")
        inicio_sesion = QPushButton("Iniciar sesion")
        dialogo.addButton(registro, QMessageBox.YesRole)
        dialogo.addButton(inicio_sesion, QMessageBox.NoRole)
        
        dialogo.exec_()

        # Verificar qué botón fue presionado
        if dialogo.clickedButton() == registro:
            self.registrarse()
        elif dialogo.clickedButton() == inicio_sesion:
            self.iniciar_sesion()


    def registrarse(self):
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()

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
        boton_confirmar.onClick.connect(confirmar_registro)
        layout_horizontal3.addWidget(boton_confirmar)

        # Botón para cancelar el registro
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.onClick.connect(cancelar_registro)
        layout_horizontal3.addWidget(boton_cancelar)



    def iniciar_sesion(self):
        print('Con este metodo iniciaremos sesion')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interface()
    app.exec_()
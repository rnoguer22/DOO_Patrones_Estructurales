import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton

class Interface(QWidget):

    def __init__(self):
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
        print('Con este metodo realizaremos el registro')
    
    def iniciar_sesion(self):
        print('Con este metodo iniciaremos sesion')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interface()
    sys.exit(app.exec_())
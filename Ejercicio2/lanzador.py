from PyQt5.QtWidgets import QApplication
import sys

from Proxy.subject import Subject
from Proxy.realSubject import RealSubject
from Proxy.proxy import Proxy
from Interface.interfaz import Interface

class Lanzador:

    def lanzar(self):

        app = QApplication(sys.argv)
        ventana = Interface()

        print(ventana.getAcceso())
        app.exec_()
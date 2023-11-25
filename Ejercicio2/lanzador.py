from PyQt5.QtWidgets import QApplication
import sys

from Proxy.subject import Subject
from Proxy.realSubject import RealSubject
from Proxy.proxy import Proxy
from Interface.interfaz import Interface

class Lanzador:

    def lanzar(self):
        #usuario = RealSubject()
        #proxy = Proxy(usuario)

        app = QApplication(sys.argv)
        ventana = Interface()
        app.exec_()
        usuario = RealSubject(ventana.getUser(), ventana.getPassword(), ventana.getAcceso())
        proxy = Proxy(usuario)
        proxy.request()

from PyQt5.QtWidgets import QApplication
import sys

from Proxy.subject import Subject
from Proxy.realSubject import RealSubject
from Proxy.proxy import Proxy
from Interface.interfaz import Interface
from Interface.interfaz_documentos import Interface_Documents

from Composite.documento import Documento
from Composite.enlace import Enlace
from Composite.carpeta import Carpeta

class Lanzador:

    def lanzar(self):
        app = QApplication(sys.argv)
        ventana = Interface()
        app.exec_()
        usuario = RealSubject(ventana.getUser(), ventana.getPassword(), ventana.getAcceso())
        proxy = Proxy(usuario)
        proxy.request()


        #AÑADIR COMPOSITE AL PROXY, AL CREAR LAS CARPETAS 
        #ESTRUCTURAR EL COMPOSITE DEL EJERCICIO 1

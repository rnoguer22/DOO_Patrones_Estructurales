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
        '''
        app = QApplication(sys.argv)
        ventana = Interface()
        app.exec_()
        usuario = RealSubject(ventana.getUser(), ventana.getPassword(), ventana.getAcceso())
        proxy = Proxy(usuario)
        proxy.request()

        # Creamos los documentos
        doc1 = Documento("documento1.txt", "Texto", "Contenido del documento")
        doc2 = Documento("Imagen.png", "Imagen", "Contenido de la imagen")

        # Creamos un enlace
        enlace = Enlace("Enlace a Carpeta", Carpeta("Carpeta de enlaces"))

        # Creamos la carpeta y añadimos el enlace y los documentos
        carpeta = Carpeta("Mi Carpeta")
        carpeta.agregar_elemento(doc1)
        carpeta.agregar_elemento(doc2)
        carpeta.agregar_elemento(enlace)

        # Accedemos a la carpeta
        carpeta.acceder(usuario)
        print(f"Tamaño de la carpeta: {carpeta.getTamanio()} bytes")

        # Accedemos al documento
        doc1.acceder(usuario)
        '''

        app = QApplication(sys.argv)
        interfaz = Interface_Documents()
        app.exec_()


        #FALTA VINCULAR LOS USUARIOS DE LOS DOCUMENTOS Y CARPETAS CON LOS DEL PROXY
        #METODOS PARA MODIFICAR EL CONTENIDO DE LOS DOCUMENTOS POR USUARIOS AUTORIZADOS
        #ESTRUCTURAR EL COMPOSITE DEL EJERCICIO 1

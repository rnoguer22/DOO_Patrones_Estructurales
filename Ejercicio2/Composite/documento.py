from documentosSistema import DocumentoSistema
import datetime


class Documento(DocumentoSistema):
    def __init__(self, nombre, tipo, tamanio, contenido):
        self.nombre = nombre
        self.tipo = tipo
        self.tamanio = tamanio
        self.contenido = contenido

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getTamanio(self):
        return self.tamanio

    def acceder(self, usuario):
        self.ultimo_acceso = datetime.now()
        print(f"Acceso al documento '{self.nombre}' por '{usuario}' a las {self.ultimo_acceso}")
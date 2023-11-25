from Composite.documentosSistema import DocumentosSistema

class Enlace(DocumentosSistema):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return "Enlace"

    def getTamanio(self):
        return 0

    def acceder(self, usuario):
        print(f"Acceso al enlace '{self.nombre}' por '{usuario}', redirigiendo a '{self.destino.obtener_nombre()}'")
from Composite.documentosSistema import DocumentosSistema


class Carpeta(DocumentosSistema):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return "Carpeta"

    def getTamanio(self):
        # El tamaño de una carpeta es la suma de los tamaños de sus elementos
        return sum(elemento.getTamanio() for elemento in self.elementos)

    # Método para agregar un elemento a la carpeta
    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def acceder(self, usuario) -> None:
        print(f"Acceso a la carpeta '{self.nombre}' por '{usuario.getUser()}', contiene:")
        for elemento in self.elementos:
            print(f"- {elemento.getNombre()} ({elemento.getTipo()})")
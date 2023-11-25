from documentosSistema import DocumentoSistema

class Carpeta(DocumentoSistema):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return "Carpeta"

    def getTamanio(self):
        # El tamaño de una carpeta es la suma de los tamaños de sus elementos
        return sum(elem.obtener_tamanio() for elem in self.elementos)

    # Método para agregar un elemento a la carpeta
    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def acceder(self, usuario):
        print(f"Acceso a la carpeta '{self.nombre}' por '{usuario}', contiene:")
        for elemento in self.elementos:
            print(f"- {elemento.obtener_nombre()} ({elemento.obtener_tipo()})")
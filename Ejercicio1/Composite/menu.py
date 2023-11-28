from typing import List
import csv
from Composite.Precio.precio import Precio
from Composite.component import Component



class Menu(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        # Función para obtener el último ID del archivo CSV
        def obtener_ultimo_id(archivo_csv):
            try:
                with open(archivo_csv, 'r', newline='') as archivo:
                    lector_csv = csv.reader(archivo)
                    lineas = list(lector_csv)
                    return len(lineas)
            except:
                return 1  # Si el archivo no existe, el primer ID será 1

        escribir_csv = [] #En esta lista guardaremos los componentes del menu
        for child in self._children:
            escribir_csv.append(child.ingredientes)

        precio = Precio()
        prize = precio.calcular_precio(escribir_csv) #Calculamos el precio del menu
        escribir_csv.append(prize)
        print('El precio de su menu es: ', prize, '€')

        id = obtener_ultimo_id('Ejercicio1/pedidos_menu.csv')
        escribir_csv.insert(0, id) #Insertamos el id del menu en la primera posicion de la lista

        #Escribimos el menu en un csv
        with open('Ejercicio1/pedidos_menu.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(escribir_csv)
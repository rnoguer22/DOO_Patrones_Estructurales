from __future__ import annotations
from typing import Any
from Pizzeria.Csv.csv import Csv
from Composite.Precio.precio import Precio


class AgregarPizza():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        csv = Csv('Ejercicio1/orden.csv')
        csv.guardar_en_csv(self.parts)
        print('Pedido realizado con exito!')
        print("Su pedido es: ", end="")
        print(f"{', '.join(self.parts)}")

        #Calculamos el precio del pedido
        precio = Precio()
        print('El precio de su pedido es: ', precio.calcular_precio(self.parts), '€')
        
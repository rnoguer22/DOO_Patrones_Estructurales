import csv

class Guardar:

    def __init__(self, ruta):
        self.ruta = ruta

    def guardar(self, datos):
        with open(self.ruta, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(datos)
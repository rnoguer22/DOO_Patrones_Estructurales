import csv


class Guardar:

    def __init__(self, ruta):
        self.ruta = ruta

    #Metodo para guardar los datos en el archivo CSV
    def guardar(self, datos):
        with open(self.ruta, 'a') as csv_file:
            ultimo_id = self.obtener_ultimo_id()
            nuevo_id = ultimo_id + 1
            datos.insert(0, nuevo_id) #Insertamos el nuevo id en la primera posicion de la lista
            csv_file.write(','.join(map(str, datos)) + '\n')  # Escribimos los datos en el archivo CSV

    # Función para obtener el último ID del archivo CSV
    def obtener_ultimo_id(self):
        try:
            with open(self.ruta, 'r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv, None)  # Saltar la primera línea (encabezados)
                lineas = list(lector_csv)
                if lineas:
                    ids = [int(linea[0]) for linea in lineas]
                    return max(ids)
                else:
                    return 0  # Si el archivo está vacío, el último ID será 0
        except:
            return 0
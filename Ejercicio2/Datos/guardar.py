import csv

class Guardar:

    def __init__(self, ruta):
        self.ruta = ruta

    def guardar(self, datos):
        with open(self.ruta, 'a') as csv_file:
            writer = csv.writer(csv_file)    
            id = self.obtener_ultimo_id(self.ruta)
            datos.insert(0, id) #Insertamos el id del menu en la primera posicion de la lista
            writer.writerow(datos)

    # Función para obtener el último ID del archivo CSV
    def obtener_ultimo_id(self):
        try:
            with open(self.ruta, 'r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                lineas = list(lector_csv)
                return len(lineas)
        except:
            return 1  # Si el archivo no existe, el primer ID será 1
        
    
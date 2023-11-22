class Precio:

    def __init__(self):
        self.precios_ingredientes = {
            'Masa Fina': 1.50, 'Salsa Tomate': 0.75, 'Queso Mozarella': 2.00, 'Tomate': 0.50, 'Albahaca': 0.25,
            'Orégano': 0.20, 'Horno': 1.00, 'Caja de carton': 0.10, 'Caja de Cartón': 0.10, 'Salsa Barbacoa': 0.80, 'Carne Picada': 2.50,
            'Cebolla': 0.40, 'Bacon': 1.80, 'Masa Gruesa': 1.60, 'Queso Parmesano': 2.20, 'Queso Cheddar': 2.00,
            'Queso Provolone': 2.10, 'Salsa Carbonara': 0.90, 'Huevo': 0.60, 'Champiñones': 0.70, 'Pimiento': 0.45,
            'Jamón': 1.70, 'Masa Rellena': 2.00, 'Masa Calzone': 3.00, 'Masa Siciliana': 1.80,
            'Masa Integral': 2.20, 'Masa Sin gluten': 2.50, 'Salsa Pesto': 0.90, 'Salsa Picante': 0.80, 'Salsa De ajo': 0.50,
            'Salsa de queso': 0.60, 'Salsa Sin salsa': 0.00, 'Queso Parmesano': 2.10, 'Queso Cheddar': 2.20, 'Queso Provolone': 2.30,
            'Queso Sin queso': 0.00, 'Pepperoni': 1.60, 'Jamon': 1.50, 'Aceitunas': 0.75, 'Tomate natural': 0.60, 'Ninguno': 0.00,
            'Parrilla': 2.00, 'Frito': 3.00, 'Cocido': 0.30, 'Crudo': 0.00, 'Gourmet': 3.00,
            'Cerveza': 2.50, 'Vino': 10.00, 'Refresco': 1.00, 'Agua': 0.50, 'Jugo': 1.20, 'Ensalada': 4.50, 'Pan de ajo': 3.20,
            'Palitos de queso': 5.00, 'Alitas de pollo': 7.80, 'Tiramisu': 6.50, 'Helado': 4.00, 'Brownie': 5.50
        }

        self.tipos_pizzas = {
            "Margarita": ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Tomate', 'Albahaca', 'Orégano', 'Horno', 'Caja de Cartón'], 
            "Barbacoa": ['Masa Fina', 'Salsa Barbacoa', 'Queso Mozarella', 'Carne Picada', 'Cebolla', 'Bacon', 'Horno', 'Caja de Cartón'], 
            "4 quesos": ['Masa Gruesa', 'Salsa Tomate', 'Queso Mozarella', 'Queso Parmesano', 'Queso Cheddar', 'Queso Provolone', 'Horno', 'Caja de Cartón'], 
            "Prosciuto": ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Jamón', 'Orégano', 'Champiñones', 'Horno', 'Caja de Cartón'], 
            "Vegetariana": ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Champiñones', 'Cebolla', 'Pimiento', 'Horno', 'Caja de Cartón'], 
            "Carbonara": ['Masa Gruesa', 'Salsa Carbonara', 'Queso Mozarella', 'Bacon', 'Cebolla', 'Huevo', 'Horno', 'Caja de Cartón'],
            "Ninguna": []
            }

    def calcular_precio(self, ingredientes):
        precio = 0
        for ingrediente in ingredientes:
            if ingrediente in self.tipos_pizzas:
                for componente in self.tipos_pizzas[ingrediente]:
                    precio += self.precios_ingredientes[componente]
            else:
                precio += self.precios_ingredientes[ingrediente]
        return round(precio, 2)
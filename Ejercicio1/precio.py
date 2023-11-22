lista = []
def agregar(ingredientes):
    for ingrediente in ingredientes:
        if ingrediente not in lista:
            lista.append(ingrediente)

agregar(['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Tomate', 'Albahaca', 'Orégano', 'Horno', 'Caja de Cartón'])
agregar(['Masa Fina', 'Salsa Barbacoa', 'Queso Mozarella', 'Carne Picada', 'Cebolla', 'Bacon', 'Horno', 'Caja de Cartón'])
agregar(ingredientes = ['Masa Gruesa', 'Salsa Tomate', 'Queso Mozarella', 'Queso Parmesano', 'Queso Cheddar', 'Queso Provolone', 'Horno', 'Caja de Cartón'])
agregar(ingredientes = ['Masa Gruesa', 'Salsa Carbonara', 'Queso Mozarella', 'Bacon', 'Cebolla', 'Huevo', 'Horno', 'Caja de Cartón'])
agregar(ingredientes = ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Champiñones', 'Cebolla', 'Pimiento', 'Horno', 'Caja de Cartón'])
agregar(ingredientes = ['Masa Fina', 'Salsa Tomate', 'Queso Mozarella', 'Jamón', 'Orégano', 'Champiñones', 'Horno', 'Caja de Cartón'])
agregar(["Fina", "Gruesa", "Rellena", "Calzone", "Siciliana", "Integral", "Sin gluten"])
agregar(["Pesto", "Tomate", "Barbacoa", "Picante", "De ajo", "de queso", "Sin salsa"])
agregar(["Mozarella", "Parmesano", "Cheddar", "Provolone", "Sin queso"])
agregar(["Pepperoni", "Champiñones", "Jamon", "Aceitunas", "Cebolla", "Tomate natural", "Ninguno"])
agregar(["Horno", "Parrilla", "Frito", "Cocido", "Crudo"])
agregar(["Caja de carton", "Gourmet"])
agregar(["Cerveza", "Vino", "Refresco", "Agua", "Jugo", "Ninguno"])
agregar(["Ensalada", "Pan de ajo", "Palitos de queso", "Alitas de pollo", "Ninguno"])
agregar(["Tiramisu", "Helado", "Brownie", "Ninguno"])

print(lista)

# Precios de los ingredientes (valores realistas)
precios_ingredientes = {
    'Masa Fina': 1.50, 'Salsa Tomate': 0.75, 'Queso Mozarella': 2.00, 'Tomate': 0.50, 'Albahaca': 0.25,
    'Orégano': 0.20, 'Horno': 1.00, 'Caja de Cartón': 0.10, 'Salsa Barbacoa': 0.80, 'Carne Picada': 2.50,
    'Cebolla': 0.40, 'Bacon': 1.80, 'Masa Gruesa': 1.60, 'Queso Parmesano': 2.20, 'Queso Cheddar': 2.00,
    'Queso Provolone': 2.10, 'Salsa Carbonara': 0.90, 'Huevo': 0.60, 'Champiñones': 0.70, 'Pimiento': 0.45,
    'Jamón': 1.70, 'Masa Rellena': 2.00, 'Masa Calzone': 3.00, 'Masa Siciliana': 1.80,
    'Masa Integral': 2.20, 'Masa Sin gluten': 2.50, 'Salsa Pesto': 0.90, 'Salsa Picante': 0.80, 'SalsaDe ajo': 0.50,
    'Salsa de queso': 0.60, 'Salsa Sin salsa': 0.00, 'Queso Parmesano': 2.10, 'Queso Cheddar': 2.20, 'Queso Provolone': 2.30,
    'Queso Sin queso': 0.00, 'Pepperoni': 1.60, 'Jamon': 1.50, 'Aceitunas': 0.75, 'Tomate natural': 0.60, 'Ninguno': 0.00,
    'Parrilla': 2.00, 'Frito': 3.00, 'Cocido': 0.30, 'Crudo': 0.00, 'Gourmet': 3.00,
    'Cerveza': 2.50, 'Vino': 10.00, 'Refresco': 1.00, 'Agua': 0.50, 'Jugo': 1.20, 'Ensalada': 4.50, 'Pan de ajo': 3.20,
    'Palitos de queso': 5.00, 'Alitas de pollo': 7.80, 'Tiramisu': 6.50, 'Helado': 4.00, 'Brownie': 5.50
}


'''
'Fina': 0.10, 'Gruesa': 0.10, 'Rellena': 0.20, 'Calzone': 0.30, 'Siciliana': 0.40,
    'Integral': 1.20, 'Sin gluten': 1.50, 'Pesto': 0.90, 'Barbacoa': 1.00, 'Picante': 0.80, 'De ajo': 0.50,
    'de queso': 0.60, 'Sin salsa': 0.00, 'Mozarella': 1.90, 'Parmesano': 2.10, 'Cheddar': 2.20, 'Provolone': 2.30,
    'Sin queso': 0.00,'''

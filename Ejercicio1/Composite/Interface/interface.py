from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout,QComboBox, QPushButton, QMessageBox, QTextEdit

class Interface_Menu(QWidget):

    def __init__(self):
        super().__init__()

        self.entrantes_disponibles = ["Ensalada", "Pan de ajo", "Palitos de queso", "Alitas de pollo", "Ninguno"]
        self.pizzas_disponibles = ["Margarita", "Barbacoa", "4 quesos", "Prosciuto", "Vegetariana", "Ninguna"]
        self.bebidas_disponibles = ["Cerveza", "Vino", "Refresco", "Agua", "Ninguno"]
        self.postres_disponibles = ["Tiramisu", "Helado", "Brownie", "Ninguno"]

        self.seleccion = []

        self.iniciar_gui()
    
    def iniciar_gui(self):
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        label = QLabel("Seleccione su menu: ")
        layout_horizontal1.addWidget(label)

        # Lista desplegable para seleccionar el entrante
        self.box_entrantes = QComboBox(self)
        self.box_entrantes.addItems(self.entrantes_disponibles)
        layout_horizontal2.addWidget(self.box_entrantes)        
        
        # Lista desplegable para seleccinar la pizza
        self.box_pizzas = QComboBox(self)
        self.box_pizzas.addItems(self.pizzas_disponibles)
        layout_horizontal2.addWidget(self.box_pizzas)

        # Lista desplegable para seleccinar la bebida
        self.box_bebidas = QComboBox(self)
        self.box_bebidas.addItems(self.bebidas_disponibles)
        layout_horizontal2.addWidget(self.box_bebidas)

        # Lista desplegable para seleccinar los postres
        self.box_postres = QComboBox(self)
        self.box_postres.addItems(self.postres_disponibles)
        layout_horizontal2.addWidget(self.box_postres)

        # Boton para confirmar la seleccion
        boton_confirmar = QPushButton("Confirmar")
        layout_horizontal3.addWidget(boton_confirmar)
        boton_confirmar.clicked.connect(self.confirmar_seleccion)

        # Boton para cancelar la seleccion
        boton_cancelar = QPushButton("Cancelar")
        layout_horizontal3.addWidget(boton_cancelar)
        boton_cancelar.clicked.connect(self.cancelar_seleccion)

        # Área de texto para mostrar la orden
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setMinimumSize(400, 300) #Hacemos que el area de texto sea un poco mas grande
        layout_horizontal3.addWidget(self.text_area)


        #FALTA AÑADIR UN BOTON PARA ENVIAR EL MENU 


        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        self.setLayout(layout_vertical)

        self.show()
    

    def confirmar_seleccion(self):
        self.seleccion = []
        self.seleccion.append(f"Entrante: {self.box_entrantes.currentText()}")
        self.seleccion.append(f"Pizza: {self.box_pizzas.currentText()}")
        self.seleccion.append(f"Bebida: {self.box_bebidas.currentText()}")
        self.seleccion.append(f"Postre: {self.box_postres.currentText()}")
        #Si la orden es correcta, la guardamos en una variable
        self.orden = ", ".join(self.seleccion)
        #Mostramos la orden en la interfaz
        self.text_area.clear()
        self.text_area.append(f"Tu orden es: {self.orden}")
        QMessageBox.about(self, "Confirmacion", "Su menu ha sido confirmado")
    
    def cancelar_seleccion(self):
        self.seleccion = []
        QMessageBox.about(self, "Cancelacion", "Su menu ha sido cancelado")
        self.text_area.clear()
        self.text_area.append("Su menu ha sido cancelado")

    def getSeleccion(self):
        return self.seleccion
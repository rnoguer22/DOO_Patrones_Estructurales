from Pizzeria.Builder.builder import Builder
from Pizzeria.Builder.agregarPizza import AgregarPizza

class BuilderPizza(Builder):
    def __init__(self, orden) -> None:
        self.reset()
        #Vamos a crear la pizza con la orden del pedido que nos llega a traves de la GUI
        self.orden = orden

    def reset(self) -> None:
        self._pizza = AgregarPizza()

    @property
    def pizza(self) -> AgregarPizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def produce_masa(self) -> None:
        try:
            self._pizza.add(self.orden[0])
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_salsa(self) -> None:
        try:
            self._pizza.add(self.orden[1])
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_queso(self) -> None:
        try:
            self._pizza.add(self.orden[2])
        except:
            print('Ha habido un error al procesar su pedido')
    
    def produce_ingrediente1(self) -> None:
        try:
            self._pizza.add(self.orden[3])    
        except:
            print('Ha habido un error al procesar su pedido')
        
    def produce_ingrediente2(self) -> None:
        try:
            self._pizza.add(self.orden[4])    
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_ingrediente3(self) -> None:
        try:
            self._pizza.add(self.orden[5])
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_coccion(self) -> None:
        try:
            self._pizza.add(self.orden[6])
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_presentacion(self) -> None:
        try:
            self._pizza.add(self.orden[7]) 
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_maridaje(self) -> None:
        try:
            self._pizza.add(self.orden[8])
        except:
            print('Ha habido un error al procesar su pedido')

    def produce_extras(self) -> None:
        try:
            self._pizza.add(self.orden[9])
        except:
            print('Ha habido un error al procesar su pedido')
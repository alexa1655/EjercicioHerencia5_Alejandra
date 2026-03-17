from Herencia1.figura import Figura

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    
    def __str__(self):
        return super().__str__() + " " + str(self.radio)
    
    def Dibujar(self):
        print("Dibujando Circulo...")
        
    def EstablecerColor(self):
        print("Estableciendo color...")
    
    def ObtenerColor(self):
        print("Obteniendo color...")
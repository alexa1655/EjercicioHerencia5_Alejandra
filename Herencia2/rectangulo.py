from Herencia1.figura import Figura

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def __str__(self):
        return super().__str__() + " " + str(self.base) + " " + str(self.altura)
    
    def Dibujar(self):
        print("Dibujando Rectangulo...")
        
    def EstablecerColor(self):
        print("Estableciendo color...")
    
    def ObtenerColor(self):
        print("Obteniendo color...")
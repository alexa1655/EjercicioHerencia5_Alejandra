from Herencia1.figura import Figura

class Triangulo(Figura):
    def __init__(self, nombre, punto1, punto2):
        super().__init__(nombre)
        self.punto1 = punto1
        self.punto2 = punto2
    
    def __str__(self):
        return super().__str__() + " " + str(self.punto1) + " " + str(self.punto2)
    
    def Dibujar(self):
        print("Dibujando Triangulo...")
        
    def EstablecerColor(self):
        print("Estableciendo color...")
    
    def ObtenerColor(self):
        print("Obteniendo color...")
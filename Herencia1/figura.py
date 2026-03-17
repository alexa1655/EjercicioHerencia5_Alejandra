class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__ (self):
        return self.nombre + " "
    
    def Dibujarfig(self):
        print("Dibujando Figura...")
        
    def EstablecerColor(self):
        print("Estableciendo color...")
    
    def ObtenerColor(self):
        print("Obteniendo color...")
from Herencia2.circulo import Circulo
from Herencia2.rectangulo import Rectangulo
from Herencia2.triangulo import Triangulo

def MenuPrincipal():
    circ = Circulo("Círculo", 140)
    rect = Rectangulo("Rectángulo", 20, 45)
    tria = Triangulo("Triángulo", "(5,2)", "(8,0)")
    
    while True:
        print("::Menú::")
        print("1. Círculo")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Salir")
        OP = int(input("Ingresa la opción: "))
        match(OP):
            case 1:
                print(circ)
                circ.Dibujarfig()
                circ.Dibujar()
                circ.EstablecerColor()
                circ.ObtenerColor()
                print()
            case 2:
                print(rect)
                rect.Dibujarfig()
                rect.Dibujar()
                rect.EstablecerColor()
                rect.ObtenerColor()
                print()
            case 3:
                print(tria)
                tria.Dibujarfig()
                tria.Dibujar()
                tria.EstablecerColor()
                tria.ObtenerColor()
                print()
            case 4:
                print("Saliendo, hasta pronto...")
                break
            case _:
                print("Opción inválida, intente nuevamente")
                print()
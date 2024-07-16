import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')


from package.maths.model import Cena
from package.maths.terms import *
from handle import *

def workspace():
    circulo = Circulo(3,5,3)
    x_coordinates = [1, 2, 6]
    y_coordinates = [3, 5, 3]
    triangulo1 = triangulo(x=x_coordinates,y= y_coordinates)
    Cena.add_forma(circulo)
    Cena.add_forma(triangulo1)
    lista = Cena.get_forma()


    for forma in lista:
        print(forma.__class__.__name__)
        print(forma.__class__.area(forma))
        print(forma.__class__.perimetro(forma))
        print(forma.__class__.model(forma))


if __name__ == '__main__':
        
    workspace()

def test_workspace():
    handle_reta()


if __name__ == '__main__':
        
    workspace()
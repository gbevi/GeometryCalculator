import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import Circulo


def workspace():

    circulo_1 = Circulo(3,5,3)
    circulo_1.model()
    circulo_1.distancia()
    print(f'A área do circulo é: {circulo_1.area()}')
    print(f'O perímetro do circulo é: {circulo_1.perimetro()}')

if __name__ == "__main__":
    workspace()


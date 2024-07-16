import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import quadrado
import math

def workspace():

    x_coordinates = [1, 2]
    y_coordinates = [3, 5]
    quadrado_1 = quadrado(x=x_coordinates, y=y_coordinates)
    quadrado_1.model()
    print(f'A área do quadrado é: {quadrado_1.area():.2f}')
    print(f'O perímetro do quadrado é: {quadrado_1.perimetro():.2f}')

    perimetro = abs(4 * math.sqrt((2 - 1) ** 2 + (5 - 3) ** 2))
    area = abs((math.sqrt((2 - 1) ** 2 + (5 - 3) ** 2)) ** 2)

    print(f'O perímetro correto do quadrado é: {perimetro:.2f}')
    print(f'A área correta do quadrado é: {area:.2f}')



if __name__ == '__main__':
        
    workspace()
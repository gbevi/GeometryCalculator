import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import triangulo
import math


def workspace():
    x_coordinates = [1, 2, 6]
    y_coordinates = [3, 5, 3]
    triangulo_1 = triangulo(x=x_coordinates, y=y_coordinates)
    if triangulo_1.isValidTriangle() == False:
        print('O triângulo não é válido')
    else:
        triangulo_1.model()
        print(f'A área do triângulo é: {triangulo_1.area():.2f}')
        print(f'O perímetro do triângulo é: {triangulo_1.perimetro():.2f}')

        # Calculando a área do triângulo usando a fórmula do determinante
        area = 0.5 * abs(x_coordinates[0]*(y_coordinates[1] - y_coordinates[2]) + 
                        x_coordinates[1]*(y_coordinates[2] - y_coordinates[0]) + 
                        x_coordinates[2]*(y_coordinates[0] - y_coordinates[1]))

        # Calculando os comprimentos dos lados do triângulo
        side_AB = math.sqrt((x_coordinates[1] - x_coordinates[0])**2 + (y_coordinates[1] - y_coordinates[0])**2)
        side_BC = math.sqrt((x_coordinates[2] - x_coordinates[1])**2 + (y_coordinates[2] - y_coordinates[1])**2)
        side_CA = math.sqrt((x_coordinates[2] - x_coordinates[0])**2 + (y_coordinates[2] - y_coordinates[0])**2)

        # Calculando o perímetro do triângulo
        perimeter = side_AB + side_BC + side_CA
        print(f'O valor correto daárea do triângulo é: {area:.2f}')
        print(f'O valor correto do perímetro do triângulo é: {perimeter:.2f}')

if __name__ == '__main__':
        
    workspace()

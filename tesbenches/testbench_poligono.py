import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import Poligono

def workspace():

    x_coordinates = [1, 2, 2, 6, 10]
    y_coordinates = [2, 4, 4, 8, 6]

    poligono_1 = Poligono(vertices=list(zip(x_coordinates, y_coordinates)))
    if poligono_1.verificarPoligono == False:
        print('Polígono inválido')
    else:
        print(f'O perímetro do polígono é: {poligono_1.perimetro():.2f}')
        print(f'O tipo do polígono é: {poligono_1.TipoPoligono()}')

if __name__ == '__main__':
    workspace()
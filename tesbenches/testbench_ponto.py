import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import ponto


def workspace():

    ponto_1 = ponto(2,6)
    ponto_1.model()
    print(f'A distância do meu ponto para a origem é: {ponto_1.distanciaDe0()}')
    
if __name__ == "__main__":
    workspace()
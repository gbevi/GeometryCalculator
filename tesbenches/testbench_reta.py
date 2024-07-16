import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import Reta



def workspace():

    segmento_1 = Reta(2,3,4,5)
    segmento_1.model()
    segmento_1.coordenadas()
    print(f'Interpolando, y = {segmento_1.interpolar():.2f}')



if __name__ == "__main__":

    workspace()


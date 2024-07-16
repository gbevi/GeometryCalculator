import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import trapezio
import math

def workspace():
    x = [1,4,8,10]
    y = [2,6,6,2]
    trapezio1 = trapezio(x,y)
    if trapezio1.trapezio_valido == False:
       print('Tra pezio inválido')
    else:
        print(f"a área do trapézio é {trapezio1.area():.2f}")
        print(f"o perímetro do trapézio é {trapezio1.perimetro():.2f}")
        print(trapezio1.model())

if __name__ == '__main__':
    workspace()
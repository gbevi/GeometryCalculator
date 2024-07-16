import sys
sys.path.append('/Users/gabrielbevilaqua/Desktop/workspace/OO')

from package.maths.terms import retangulo

def workspace():

    x = [1,2,3]
    y = [3,4,5]
    retangulo1 = retangulo(x,y)
    print(f"a área do retângulo é: {retangulo1.area():.2f}")
    print(f"o perímetro do retângulo é: {retangulo1.perimetro():.2f}")
    retangulo1.model()

if __name__ == "__main__":
    workspace()
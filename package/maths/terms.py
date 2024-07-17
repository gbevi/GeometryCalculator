import math
from package.maths.model import Model

class ponto(Model):


    def __init__(self,x=None,y=None):
        super().__init__(x,y)

    def distanciaDe0(self):
        distancia = math.sqrt(self._x[0] ** 2 + self._y[0] ** 2)
        return distancia
    
    def model(self):

        print(str(self))

class Reta(Model):
    def __init__(self,a,b,x=None,y=None):

        super().__init__(x,y)
        self._a = a
        self._b = b

    def setA(self, a):
        self._a = a if a.isdigit() else 0
    
    def setB(self, b):
        self._b = b if b.isdigit() else 0

    def getA(self): 

        return self._a
    
    def getB(self): 
            
        return self._b

    def interpolar(self):

        y = self._a * self._x[0] + self._b
        return y

    def coordenadas(self):

        print(f'As coordenadas do segmento de reta a partir de x na origem são: x1 = 0, y1 = {self._b} e x2 = {self._x[0]}, y2 = {self.interpolar()}')
    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: a={self._a}, b={self._b}')

class Circulo(Model):

    def __init__(self, raio, x=None, y=None):
        super().__init__(x, y)
        self._raio = raio
        self.num_lados = 1

    def setRaio(self,raio):
            
        self._raio = raio if raio.isdigit() else 0
        
    def getRaio(self):

        return self._raio
    
    
    def area(self):
        # o raio precisa ser definido antes
        return math.pi * (self._raio ** 2)
    
    def perimetro(self):
        # o raio precisa ser definido antes
        return 2 * math.pi * self._raio

    def model(self):

        print(str(self))

    def is_point_inside_circle(self, x, y):
        distance = math.sqrt((x - self._x[0]) ** 2 + (y - self._y[0]) ** 2)
        return distance <= self._raio

class triangulo(Model):

    def __init__(self,x=None,y=None):
        super().__init__(x,y)


    def isValidTriangle(self):
        # Calculate side lengths
        side1 = math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2)
        side2 = math.sqrt((self._x[2] - self._x[1]) ** 2 + (self._y[2] - self._y[1]) ** 2)
        side3 = math.sqrt((self._x[0] - self._x[2]) ** 2 + (self._y[0] - self._y[2]) ** 2)
        area = abs(((self._x[0] * (self._y[1] - self._y[2])) + (self._x[2] * (self._y[0] - self._y[1])) + (self._x[1] * (self._y[2] - self._y[0]))) / 2)

        # Check Triangle Inequality Theorem
        if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2) and area > 0:
            return True
        else:
            return False
    
    def TipoTriangulo(self):

        if self._x == self._x[1] and self._x[1] == self._x[2]:
            return 'Equilátero'
        elif self._x == self._x[1] or self._x[1] == self._x[2] or self._x == self._x[2]:
            return 'Isósceles'
        else:
            return 'Escaleno'
        
    def perimetro(self):

        perimetro = math.sqrt((self._x[0] - self._x[1]) ** 2 + (self._y[0] - self._y[1]) ** 2) + math.sqrt((self._x[1] - self._x[2]) ** 2 + (self._y[1] - self._y[2]) ** 2) + math.sqrt((self._x[0] - self._x[2]) ** 2 + (self._y[0] - self._y[2]) ** 2)
        return perimetro
        
    def area(self):

        area = abs(((self._x[0] * (self._y[1] - self._y[2])) + (self._x[2] * (self._y[0] - self._y[1])) + (self._x[1] * (self._y[2] - self._y[0]))) / 2)
        return area
    
    def model(self):

        print(str(self))

    def is_point_inside_triangle(self, x, y):
        # Calculate area of triangle ABC
        A = 0.5 * (-self._y[1] * self._x[2] + self._x[0] * -self._y[1] + self._y[0] * self._x[2] - self._x[0] * self._y[2] + self._y[1] * self._x[2] - self._x[1] * self._y[0])
        # Calculate area of triangle PBC
        A1 = 0.5 * (-y * self._x[2] + self._x[0] * -self._y[1] + self._y[0] * self._x[2] - self._x[0] * -self._y[2] + self._y[1] * self._x[2] - self._x[1] * self._y[0])
        # Calculate area of triangle PAC
        A2 = 0.5 * (-self._y[1] * x + x * -self._y[2] + self._y[0] * self._x[2] - self._x[0] * -self._y[2] + self._y[1] * -self._y[2] - x * self._y[0])
        # Calculate area of triangle PAB
        A3 = 0.5 * (-self._y[1] * self._x[2] + self._x[0] * -y + self._y[0] * self._x[2] - self._x[0] * self._y[2] + y * self._x[2] - self._x[1] * self._y[0])
        # Check if sum of A1, A2 and A3 is same as A
        return A == A1 + A2 + A3

class quadrado(Model):
    
    def __init__(self,x=None,y=None):
        super().__init__(x,y)

    def isValidSquare(self):
        area = (math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2)) ** 2
        if area > 0:
            return True
        else:
            raise ValueError("Quadrado inválido")

    def perimetro(self):

        perimetro = 4 * math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[0] - self._y[1]) ** 2)
        return abs(perimetro)
    
    def area(self):

        area = (math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2)) ** 2

        return abs(area)
    
    def model(self):
    
        print(str(self))

    def is_point_inside_square(self, x, y):
        # Check if the point is inside the square
        return self._x[0] <= x <= self._x[1] and self._y[0] <= y <= self._y[1]



class retangulo(Model):
    
    def __init__(self,x=None,y=None):
        super().__init__(x,y)

    def area(self):
            
        lado1 = math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2)
        lado2 = math.sqrt((self._x[2] - self._x[1]) ** 2 + (self._y[2] - self._y[1]) ** 2)
        area = lado1 * lado2
        return area
    
    def isValidRectangle(self):
        lado1 = math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2)
        lado2 = math.sqrt((self._x[2] - self._x[1]) ** 2 + (self._y[2] - self._y[1]) ** 2)
        area = lado1 * lado2
        if area > 0:
            return True
        else:
            raise ValueError("Retângulo inválido")
    
    def perimetro(self):
            
        perimetro = 2 * (math.sqrt((self._x[1] - self._x[0]) ** 2 + (self._y[1] - self._y[0]) ** 2) + math.sqrt((self._x[2] - self._x[1]) ** 2 + (self._y[2] - self._y[1]) ** 2))
        return perimetro
    
    def model(self):

        print(str(self))

    def is_point_inside_rectangle(self, x, y):
        # Check if the point is inside the rectangle
        return self._x[0] <= x <= self._x[1] and self._y[0] <= y <= self._y[1] and self._x[1] <= x <= self._x[2] and self._y[1] <= y <= self._y[2]

class trapezio(Model):
    def __init__(self, x, y):
        super().__init__(x, y) # Chama o construtor da classe pai

    def calcular_inclinacao(self, x1, y1, x2, y2):
        if x2 - x1 != 0:
            return (y2 - y1) / (x2 - x1)
        else:
            return float('inf')  # Caso especial para inclinação vertical

    def verificar_trapezio(self):
        # Calcular as inclinações dos lados opostos
        m1 = self.calcular_inclinacao(self._x[0], self._y[0], self._x[1], self._y[1])
        m2 = self.calcular_inclinacao(self._x[2], self._y[2], self._x[3], self._y[3])
        m3 = self.calcular_inclinacao(self._x[1], self._y[1], self._x[2], self._y[2])
        m4 = self.calcular_inclinacao(self._x[0], self._y[0], self._x[3], self._y[3])

        # Verificar se pelo menos um par de lados opostos é paralelo
        if m1 == m2 or m3 == m4 or m1 == m4 or m2==m3:
            return True
        else:
            return False

    def verificar_quadrilatero_fechado(self):
        # Verificar se os vértices formam um quadrilátero fechado
        # Isso pode ser feito verificando se os lados se conectam corretamente
       return (self._x[0], self._y[0]) != (self._x[1], self._y[1]) and \
               (self._x[1], self._y[1]) != (self._x[2], self._y[2]) and \
               (self._x[2], self._y[2]) != (self._x[3], self._y[3]) and \
               (self._x[3], self._y[3]) != (self._x[0], self._y[0])

    def isValidTrapezium(self):
        if self.verificar_quadrilatero_fechado() and self.verificar_trapezio():
            return True
        else:
            return False

    def area(self):
        # Calcular a área usando a fórmula do trapézio
        base_maior = math.sqrt((self._x[2] - self._x[3]) ** 2 + (self._y[2] - self._y[3]) ** 2)
        base_menor = math.sqrt((self._x[0] - self._x[1]) ** 2 + (self._y[0] - self._y[1]) ** 2)
        maiorY = max(self._y)
        menorY = min(self._y)   
        altura = maiorY - menorY

        area = 0.5 * (base_maior + base_menor) * altura
        return area

    def perimetro(self):
        # Calcular o perímetro somando todos os lados do trapézio
        perimetro = (math.sqrt((self._x[0] - self._x[1]) ** 2 + (self._y[0] - self._y[1]) ** 2) +
                     math.sqrt((self._x[1] - self._x[2]) ** 2 + (self._y[1] - self._y[2]) ** 2) +
                     math.sqrt((self._x[2] - self._x[3]) ** 2 + (self._y[2] - self._y[3]) ** 2) +
                     math.sqrt((self._x[3] - self._x[0]) ** 2 + (self._y[3] - self._y[0]) ** 2))

        return perimetro
    
    def is_point_inside_trapezium(self, x, y):
        # Verificar se o ponto está dentro do trapézio
        # Calcular a área total do trapézio
        area_total = self.area()
        # Calcular a área dos quatro triângulos formados pelo ponto e os vértices do trapézio
        area1 = 0.5 * abs((self._x[0] * (self._y[1] - self._y[3]) + self._x[1] * (self._y[3] - self._y[0]) + self._x[3] * (self._y[0] - self._y[1])))
        area2 = 0.5 * abs((self._x[1] * (self._y[2] - self._y[0]) + self._x[2] * (self._y[0] - self._y[1]) + self._x[0] * (self._y[1] - self._y[2])))
        area3 = 0.5 * abs((self._x[2] * (self._y[3] - self._y[1]) + self._x[3] * (self._y[1] - self._y[2]) + self._x[1] * (self._y[2] - self._y[3])))
        area4 = 0.5 * abs((self._x[3] * (self._y[0] - self._y[2]) + self._x[0] * (self._y[2] - self._y[3]) + self._x[2] * (self._y[3] - self._y[0])))
        # Verificar se a soma das áreas dos triângulos é igual à área total
        return area_total == area1 + area2 + area3 + area4
    
    def model(self):
        
        print(str(self))

class Poligono():
    def __init__(self, vertices):
        # Ensure vertices is a list of tuples and does not exceed ten vertices
        if not isinstance(vertices, list) or not all(isinstance(v, tuple) and len(v) == 2 for v in vertices) or len(vertices) > 10:
            raise ValueError("Vertices precisam ser uma lista de tuplas com dois elementos e não pode exceder 10 vertices.")
        
        self.vertices = [ponto(x=v[0], y=v[1]) for v in vertices]
        
        

    def perimetro(self):
        perimetro = 0
        for i in range(len(self.vertices)):
            perimetro += math.sqrt((self.vertices[i]._x[0] - self.vertices[(i + 1) % len(self.vertices)]._x[0]) ** 2 + (self.vertices[i]._y[0] - self.vertices[(i + 1) % len(self.vertices)]._y[0]) ** 2)
        return perimetro
    
    def TipoPoligono(self):
        if len(self.vertices) == 3:
            return 'Triângulo'
        elif len(self.vertices) == 4:
            return 'Quadrilátero'
        elif len(self.vertices) == 5:
            return 'Pentágono'
        elif len(self.vertices) == 6:
            return 'Hexágono'
        elif len(self.vertices) == 7:
            return 'Heptágono'
        elif len(self.vertices) == 8:
            return 'Octógono'
        elif len(self.vertices) == 9:
            return 'Eneágono'
        elif len(self.vertices) == 10:
            return 'Decágono'
        else:
            return 'Polígono não identificado'
        
    def verificarPoligono(self):
        if len(self.vertices) >= 3:
            return True
        else:
            return False




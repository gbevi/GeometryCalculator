class Model:

    def __init__(self, x=None, y=None):
        # Garante que x e y sejam listas
        self._x = list(x) if isinstance(x, (list, tuple)) else [x] if x is not None else [0]
        self._y = list(y) if isinstance(y, (list, tuple)) else [y] if y is not None else [0]

    # Restante da classe...

    def set_coords(self, x, y):
        if str.isdigit(str(x)) and str.isdigit(str(y)):
            self._x = x
            self._y = y
        else: 
            raise ValueError("As coordenadas devem ser números")

    def getX(self):

        return self._x
    
    def getY(self):

        return self._y

    def translate(self, dx, dy):
        """
        Translada a forma geométrica por dx unidades no eixo x e dy unidades no eixo y.
        """
        for i in range(len(self._x)):
            self._x[i] += dx
            self._y[i] += dy

    def centroid(self):
        """
        Calcula o centroide da forma geométrica.
        Retorna uma tupla com as coordenadas do centroide.
        """
        if not self._x or not self._y:
            return None
        
        cx = sum(self._x) / len(self._x)
        cy = sum(self._y) / len(self._y)
        return f"O centro da forma geometrica é: {(cx, cy)}"

    def __eq__(self, other):
        """
        Verifica se duas formas geométricas são iguais.
        """
        if not isinstance(other, Model):
            return False
        
        return (self._x == other._x and self._y == other._y)

    def __str__(self):
        """
        Retorna uma representação string da forma geométrica.
        """
        return f"Forma geometrica com coordenadas x={self._x}, y={self._y}"
    
class Cena:
    _instance = None
    lista_formas = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cena, cls).__new__(cls)
            return cls._instance
    @classmethod
    def get_forma(cls):
        return cls.lista_formas
        
    @classmethod
    def add_forma(cls, forma):
        cls.lista_formas.append(forma)
    
    @classmethod
    def delete_forma(cls, forma):
        cls.lista_formas.remove(forma)
    
    
    

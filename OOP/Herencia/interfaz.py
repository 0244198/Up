import math

class Figura:
    def calcular_area(self)->float:
        raise NotImplementedError
    def calcular_perimetro(self)->float:
        raise NotImplementedError

class Triangulo(Figura):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.perimetro = None
        self.semiperimetro = None
        self.area = None
    def calcular_perimetro(self) ->float:
        self.perimetro = self.l1 + self.l2 + self.l3
        return float(self.perimetro)
    def calcular_area(self) ->float:
        self.calcular_perimetro()
        self.semiperimetro = self.perimetro/2
        self.area = math.sqrt(self.semiperimetro*(self.semiperimetro-self.l1)*(self.semiperimetro-self.l2)*
                              (self.semiperimetro-self.l3))
        return float(self.area)

class Circulo(Figura):
    def __init__(self, radio):
        self.area = None
        self.perimetro = None
        self.radio = radio

    def calcular_perimetro(self) ->float:
        self.perimetro = math.pi*2*self.radio
        return float(self.perimetro)

    def calcular_area(self)->float:
        self.area = math.pi*(self.radio**2)
        return float(self.area)


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        self.perimetro = (2*self.base)+(2*self.altura)
        return float(self.perimetro)

    def calcular_area(self) -> float:
        self.area = self.base * self.altura
        return float(self.area)

t1 = Triangulo(3,4,5)
r1 = Rectangulo(base=4,altura=10)
c1 = Circulo(radio=2)
for figura in [t1,c1,r1]:
    print(f"El area es {figura.calcular_area()} y el perimetro es {figura.calcular_perimetro()}")

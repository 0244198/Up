class Trabajador:
    def __init__(self, antiguedad, nombre):
        self.antiguedad = antiguedad
        self.nombre = nombre
        self.salario = None
        self.salario_base = None

    def calcular_salario(self):
        self.salario = self.salario_base + (self.antiguedad * 1000)
        return self.salario

    def trabaja(self):
        raise NotImplementedError


class Secretario(Trabajador):
    def __init__(self, antiguedad, nombre):
        super().__init__(antiguedad, nombre)
        self.salario_base = 15000

    def trabaja(self):
        print("Apoya")


class Programador(Trabajador):
    def __init__(self, antiguedad, nombre):
        super().__init__(antiguedad, nombre)
        self.salario_base = 25000

    def trabaja(self):
        print("Programa")


class Gerente(Trabajador):
    def __init__(self, antiguedad, nombre):
        super().__init__(antiguedad, nombre)
        self.salario_base = 50000

    def calcular_salario(self):
        return 50000

    def modificar_salario(self, objeto, aumento):
        objeto.salario_base += aumento

    def trabaja(self):
        print("Gerencia")

#Pruebas
marcos = Programador(1, "Marcos")
laura = Secretario(2, "Laura")
adolfo = Gerente(3, "Adolfo")
marcos.trabaja()
laura.trabaja()
adolfo.trabaja()
print(marcos.calcular_salario())
print(laura.calcular_salario())
print(adolfo.calcular_salario())
adolfo.modificar_salario(laura, 1)
print(laura.calcular_salario())

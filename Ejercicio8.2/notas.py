import math

class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcularPromedio(self):
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += self.listaNotas[i]
        return suma / len(self.listaNotas)

    def calcularDesviacion(self):
        prom = self.calcularPromedio()
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += (self.listaNotas[i] - prom) ** 2
        return math.sqrt(suma / len(self.listaNotas))

    def calcularMenor(self):
        menor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] < menor:
                menor = self.listaNotas[i]
        return menor

    def calcularMayor(self):
        mayor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] > mayor:
                mayor = self.listaNotas[i]
        return mayor
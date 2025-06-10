from figuraGeometrica import FiguraGeometrica
import math

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcularSuperficie(self):
        areaLateral = 2.0 * math.pi * self.radio * self.altura
        areaBases = 2.0 * math.pi * self.radio ** 2
        return areaLateral + areaBases
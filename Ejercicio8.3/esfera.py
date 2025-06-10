from figuraGeometrica import FiguraGeometrica
import math

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (4.0/3.0) * math.pi * self.radio ** 3

    def calcularSuperficie(self):
        return 4.0 * math.pi * self.radio ** 2
from figuraGeometrica import FiguraGeometrica

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (self.base ** 2) * self.altura / 3.0

    def calcularSuperficie(self):
        areaBase = self.base ** 2
        areaLados = 2.0 * self.base * self.apotema
        return areaBase + areaLados
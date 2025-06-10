import tkinter as tk
from ventanaCilindro import VentanaCilindro
from ventanaEsfera import VentanaEsfera
from ventanaPiramide import VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        self.btnCilindro = tk.Button(self, text="Cilindro", command=self.abrirCilindro)
        self.btnCilindro.place(x=20, y=50, width=80, height=23)

        self.btnEsfera = tk.Button(self, text="Esfera", command=self.abrirEsfera)
        self.btnEsfera.place(x=125, y=50, width=80, height=23)

        self.btnPiramide = tk.Button(self, text="Pirámide", command=self.abrirPiramide)
        self.btnPiramide.place(x=225, y=50, width=100, height=23)

    def abrirCilindro(self):
        VentanaCilindro(self)

    def abrirEsfera(self):
        VentanaEsfera(self)

    def abrirPiramide(self):
        VentanaPiramide(self)
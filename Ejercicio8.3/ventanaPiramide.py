import tkinter as tk
from tkinter import messagebox
from piramide import Piramide

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        self.lblBase = tk.Label(self, text="Base (cms):")
        self.lblBase.place(x=20, y=20, width=90, height=23)
        self.campoBase = tk.Entry(self)
        self.campoBase.place(x=120, y=20, width=135, height=23)

        self.lblAltura = tk.Label(self, text="Altura (cms):")
        self.lblAltura.place(x=20, y=50, width=90, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135, height=23)

        self.lblApotema = tk.Label(self, text="Apotema (cms):")
        self.lblApotema.place(x=20, y=80, width=90, height=23)
        self.campoApotema = tk.Entry(self)
        self.campoApotema.place(x=120, y=80, width=135, height=23)

        self.btnCalcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btnCalcular.place(x=120, y=110, width=135, height=23)

        self.lblVolumen = tk.Label(self, text="Volumen (cm3):")
        self.lblVolumen.place(x=20, y=140, width=135, height=23)

        self.lblSuperficie = tk.Label(self, text="Superficie (cm2):")
        self.lblSuperficie.place(x=20, y=170, width=135, height=23)

    def calcular(self):
        try:
            base = float(self.campoBase.get())
            altura = float(self.campoAltura.get())
            apotema = float(self.campoApotema.get())
            piramide = Piramide(base, altura, apotema)
            self.lblVolumen.config(text=f"Volumen (cm3): {piramide.calcularVolumen():.2f}")
            self.lblSuperficie.config(text=f"Superficie (cm2): {piramide.calcularSuperficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
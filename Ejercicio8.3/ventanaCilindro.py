import tkinter as tk
from tkinter import messagebox
from cilindro import Cilindro

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        self.lblRadio = tk.Label(self, text="Radio (cms):")
        self.lblRadio.place(x=20, y=20, width=90, height=23)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=120, y=20, width=135, height=23)

        self.lblAltura = tk.Label(self, text="Altura (cms):")
        self.lblAltura.place(x=20, y=50, width=90, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135, height=23)

        self.btnCalcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btnCalcular.place(x=120, y=80, width=135, height=23)

        self.lblVolumen = tk.Label(self, text="Volumen (cm3):")
        self.lblVolumen.place(x=20, y=110, width=135, height=23)

        self.lblSuperficie = tk.Label(self, text="Superficie (cm2):")
        self.lblSuperficie.place(x=20, y=140, width=135, height=23)

    def calcular(self):
        try:
            radio = float(self.campoRadio.get())
            altura = float(self.campoAltura.get())
            cilindro = Cilindro(radio, altura)
            self.lblVolumen.config(text=f"Volumen (cm3): {cilindro.calcularVolumen():.2f}")
            self.lblSuperficie.config(text=f"Superficie (cm2): {cilindro.calcularSuperficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
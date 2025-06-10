import tkinter as tk
from tkinter import messagebox
from notas import Notas

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        # Etiquetas y campos de notas
        self.nota1 = tk.Label(self, text="Nota 1:")
        self.nota1.place(x=0, y=20, width=135, height=23)
        self.campoNota1 = tk.Entry(self)
        self.campoNota1.place(x=105, y=20, width=135, height=23)

        self.nota2 = tk.Label(self, text="Nota 2:")
        self.nota2.place(x=0, y=50, width=135, height=23)
        self.campoNota2 = tk.Entry(self)
        self.campoNota2.place(x=105, y=50, width=135, height=23)

        self.nota3 = tk.Label(self, text="Nota 3:")
        self.nota3.place(x=0, y=80, width=135, height=23)
        self.campoNota3 = tk.Entry(self)
        self.campoNota3.place(x=105, y=80, width=135, height=23)

        self.nota4 = tk.Label(self, text="Nota 4:")
        self.nota4.place(x=0, y=110, width=135, height=23)
        self.campoNota4 = tk.Entry(self)
        self.campoNota4.place(x=105, y=110, width=135, height=23)

        self.nota5 = tk.Label(self, text="Nota 5:")
        self.nota5.place(x=0, y=140, width=135, height=23)
        self.campoNota5 = tk.Entry(self)
        self.campoNota5.place(x=105, y=140, width=135, height=23)

        # Botones
        self.calcular = tk.Button(self, text="Calcular", command=self.calcularValores)
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self, text="Limpiar", command=self.limpiarCampos)
        self.limpiar.place(x=125, y=170, width=80, height=23)

        # Etiquetas de resultados
        self.promedio = tk.Label(self, text="Promedio = ")
        self.promedio.place(x=8, y=210, width=135, height=23)

        self.desviacion = tk.Label(self, text="Desviación = ")
        self.desviacion.place(x=-22, y=240, width=200, height=23)

        self.mayor = tk.Label(self, text="Nota mayor = ")
        self.mayor.place(x=20, y=270, width=120, height=23)

        self.menor = tk.Label(self, text="Nota menor = ")
        self.menor.place(x=20, y=300, width=120, height=23)

    def calcularValores(self):
        try:
            notas = Notas()
            notas.listaNotas[0] = float(self.campoNota1.get())
            notas.listaNotas[1] = float(self.campoNota2.get())
            notas.listaNotas[2] = float(self.campoNota3.get())
            notas.listaNotas[3] = float(self.campoNota4.get())
            notas.listaNotas[4] = float(self.campoNota5.get())

            self.promedio.config(text="Promedio = {:.2f}".format(notas.calcularPromedio()))
            self.desviacion.config(text="Desviación estándar = {:.2f}".format(notas.calcularDesviacion()))
            self.mayor.config(text="Valor mayor = {:.2f}".format(notas.calcularMayor()))
            self.menor.config(text="Valor menor = {:.2f}".format(notas.calcularMenor()))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese sólo valores numéricos.")

    def limpiarCampos(self):
        self.campoNota1.delete(0, tk.END)
        self.campoNota2.delete(0, tk.END)
        self.campoNota3.delete(0, tk.END)
        self.campoNota4.delete(0, tk.END)
        self.campoNota5.delete(0, tk.END)
        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")
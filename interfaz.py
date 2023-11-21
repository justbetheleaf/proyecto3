import tkinter as tk
from tkinter import ttk, messagebox
import turtle
import time
from fractal import *
from fractal_LevyC import *
from fractal_Curva_Koch import *
from fractal_Dragon import *
from fractal_Inspo_Gosper_Curve import *
from fractal_Flecha_Sierpinski import *
from constructor import *

class SistemaVentanas:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Ventanas con Graficador de Fractales")

        self.configurar_interfaz()
        self.fractales = ["CurvaLecyC", "FlechaSierpinski", "Curva de Koch", "Inpiración de Gosper pero en curva", "Curva de dragón"]
        self.combobox_fractales = ttk.Combobox(master, values=self.fractales, state="readonly")
        self.combobox_fractales.pack(pady=10)
        self.combobox_fractales.set("Seleccione un fractal")
        self.boton_recomendaciones = tk.Button(master, text="Recomendaciones", command=self.mostrar_recomendaciones)
        self.boton_recomendaciones.pack(pady=5)
        self.entry_iteraciones = self.crear_campo_iteraciones(master)
        self.boton_venta = tk.Button(master, text="Dibujar", command=self.realizar_venta)
        self.boton_venta.pack(pady=20)
        self.boton_salir = tk.Button(master, text="Salir", command=self.salir_programa)
        self.boton_salir.pack(pady=10)
        self.fractal_seleccionado = tk.StringVar()
        self.turtle_window = turtle.Screen()

    def configurar_interfaz(self):
        self.etiqueta = tk.Label(self.master, text="¡Bienvenido a nuestro sistema para graficar fractales!")
        self.etiqueta.pack(pady=10)

    def crear_campo_iteraciones(self, master):
        etiqueta_iteraciones = tk.Label(master, text="Número de Iteraciones:")
        etiqueta_iteraciones.pack()
        entry_iteraciones = tk.Entry(master)
        entry_iteraciones.pack(pady=10)
        return entry_iteraciones

    def salir_programa(self):
        self.master.destroy()
        self.turtle_window.bye()
        exit()

    def realizar_venta(self):
        fractal_elegido = self.combobox_fractales.get()
        num_iteraciones = self.obtener_numero_iteraciones()

        if fractal_elegido and fractal_elegido != "Seleccione un fractal" and num_iteraciones is not None:
            self.fractal_seleccionado.set(fractal_elegido)
            graficador = GraficadorFractales(self.master, self)
            self.boton_venta.config(state=tk.DISABLED)
            graficador.graficar_fractal(fractal_elegido, num_iteraciones)
            self.boton_venta.config(state=tk.NORMAL)
        else:
            print("Por favor, seleccione un tipo de fractal válido y/o ingrese un número de iteraciones válido.")

    def obtener_numero_iteraciones(self):
        try:
            num_iteraciones = int(self.entry_iteraciones.get())
            if num_iteraciones > 0:
                return num_iteraciones
            else:
                messagebox.showerror("Error", "Por favor, ingrese un número de iteraciones válido (entero positivo).")
                return None
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número de iteraciones válido (entero positivo).")
            return None

    def mostrar_recomendaciones(self):
        fractal_elegido = self.combobox_fractales.get()
        if fractal_elegido and fractal_elegido != "Seleccione un fractal":
            recomendacion = self.obtener_recomendacion(fractal_elegido)
            messagebox.showinfo("Recomendación", recomendacion)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un tipo de fractal.")

    def obtener_recomendacion(self, tipo_fractal):
        recomendacion = ""
        recomendaciones = {
            "CurvaLecyC": "Se recomienda usar 8 iteraciones",
            "FlechaSierpinski": "Se recomienda usar 4 iteraciones",
            "Curva de Koch": "Se recomienda usar 3 iteraciones",
            "Inpiración de Gosper pero en curva": "Se recomienda usar 4 iteraciones",
            "Curva de dragón": "Se recomienda usar 7 iteraciones"
        }
        if tipo_fractal in recomendaciones:
            recomendacion = recomendaciones[tipo_fractal]
        return recomendacion


class GraficadorFractales:
    def __init__(self, master, sistema_ventanas):
        self.master = master
        self.sistema_ventanas = sistema_ventanas

    def graficar_fractal(self, tipo_fractal, num_iteraciones):
        configuracion_fractal = self.configurar_fractal(tipo_fractal, num_iteraciones)

        while True:
            turtle.bgcolor(configuracion_fractal["bgcolor"])
            configuracion_fractal["constructor"].construir_y_dibujar()

            time.sleep(3)
            respuesta = messagebox.askyesno("Continuar", "¿Desea graficar otro fractal?")

            if respuesta:
                turtle.reset()
                turtle.clear()
                return
            else:
                self.master.destroy()
                self.sistema_ventanas.turtle_window.bye()
                return

    def configurar_fractal(self, tipo_fractal, num_iteraciones):
        colores = {
            "CurvaLecyC": {"bgcolor": "lightblue", "pencolor": "blue", "penup_pos": (-100, 0)},
            "FlechaSierpinski": {"bgcolor": "lightgreen", "pencolor": "green", "penup_pos": (100, -100)},
            "Curva de Koch": {"bgcolor": "lightcoral", "pencolor": "red", "penup_pos": (100, 0)},
            "Inpiración de Gosper pero en curva": {"bgcolor": "hotpink", "pencolor": "purple", "penup_pos": (-100, 0)},
            "Curva de dragón": {"bgcolor": "khaki", "pencolor": "orange", "penup_pos": (0, 0)},
        }

        turtle.bgcolor(colores[tipo_fractal]["bgcolor"])
        turtle.pencolor(colores[tipo_fractal]["pencolor"])
        turtle.pensize(2)
        turtle.penup()
        turtle.goto(colores[tipo_fractal]["penup_pos"])
        turtle.pendown()

        if tipo_fractal == "CurvaLecyC":
            fractal = CurvaLecyC(num_iteraciones, 10)
        elif tipo_fractal == "FlechaSierpinski":
            fractal = FlechaSierpinski(num_iteraciones, 10)
            turtle.left(180)  # Ajuste de orientación para FlechaSierpinski
        elif tipo_fractal == "Curva de Koch":
            fractal = Koch(num_iteraciones, 12)
            turtle.left(180)  # Ajuste de orientación para Koch
        elif tipo_fractal == "Inpiración de Gosper pero en curva":
            fractal = GosperInspiredCurve(num_iteraciones, 10)
        elif tipo_fractal == "Curva de dragón":
            fractal = DragonCurve(num_iteraciones, 10)

        constructor_fractal = ConstructorFiguras(fractal)
        return {"bgcolor": colores[tipo_fractal]["bgcolor"], "constructor": constructor_fractal}


def main():
    ventana = tk.Tk()
    app = SistemaVentanas(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()

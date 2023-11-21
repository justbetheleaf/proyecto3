import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from Clases_Fractales import *
import turtle
import time  

class SistemaVentanas:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Ventanas con Graficador de Fractales")

        # Etiqueta
        self.etiqueta = tk.Label(master, text="¡Bienvenido a nuestro sistema para graficar fractales!")
        self.etiqueta.pack(pady=10)

        # Lista de fractales
        self.fractales = ["CurvaLecyC","FlechaSierpinski","Koch","Gosper","Curva de dragón"]

        # Cuadro de lista desplegable para el tipo de fractal
        self.combobox_fractales = ttk.Combobox(master, values=self.fractales, state="readonly")
        self.combobox_fractales.pack(pady=10)
        self.combobox_fractales.set("Seleccione un fractal")  # Texto predeterminado

         # Botón Recomendaciones
        self.boton_recomendaciones = tk.Button(master, text="Recomendaciones", command=self.mostrar_recomendaciones)
        self.boton_recomendaciones.pack(pady=5)

        # Campo de entrada para el número de iteraciones
        self.etiqueta_iteraciones = tk.Label(master, text="Número de Iteraciones:")
        self.etiqueta_iteraciones.pack()
        self.entry_iteraciones = tk.Entry(master)
        self.entry_iteraciones.pack(pady=10)

        # Botón Dibujar
        self.boton_venta = tk.Button(master, text="Dibujar", command=self.realizar_venta)
        self.boton_venta.pack(pady=20)

        # Botón para salir
        self.boton_salir = tk.Button(master, text="Salir", command=self.salir_programa)
        self.boton_salir.pack(pady=10)

        # Variable para almacenar el fractal seleccionado
        self.fractal_seleccionado = tk.StringVar()
        # Ventana Turtle
        self.turtle_window = turtle.Screen()
        
    def salir_programa(self):
        # Cierra ambas ventanas y termina el programa
        self.master.destroy()
        self.turtle_window.bye()
        exit()

    def realizar_venta(self):
        fractal_elegido = self.combobox_fractales.get()
        num_iteraciones = self.obtener_numero_iteraciones()

        if fractal_elegido and fractal_elegido != "Seleccione un fractal" and num_iteraciones is not None:
            self.fractal_seleccionado.set(fractal_elegido)
            graficador = GraficadorFractales(self.master, self)
            self.boton_venta.config(state=tk.DISABLED)  # Desactivar el botón
            graficador.graficar_fractal(fractal_elegido, num_iteraciones)
            self.boton_venta.config(state=tk.NORMAL)   # Reactivar el botón después del ciclo
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
        if tipo_fractal == "CurvaLecyC":
            recomendacion = "Se recomienda usar 8 iteraciones"
        elif tipo_fractal == "FlechaSierpinski":
            recomendacion = "Se recomienda usar 4 iteraciones"
        elif tipo_fractal == "Koch":
            recomendacion = "Se recomienda usar 3 iteraciones"
        elif tipo_fractal == "Gosper":
            recomendacion = "Se recomienda usar 4 iteraciones"
        elif tipo_fractal == "Curva de dragón":
            recomendacion = "Se recomienda usar 7 iteraciones"
        return recomendacion


class GraficadorFractales:
    def __init__(self, master, sistema_ventanas):
        self.master = master
        self.sistema_ventanas = sistema_ventanas

    def graficar_fractal(self, tipo_fractal, num_iteraciones):
        while True:
            # Cambiar el fondo de la ventana de Turtle para cada fractal
            if tipo_fractal == "CurvaLecyC":
                turtle.bgcolor("lightblue")
            elif tipo_fractal == "FlechaSierpinski":
                turtle.bgcolor("lightgreen")
            elif tipo_fractal == "Koch":
                turtle.bgcolor("lightcoral")
            elif tipo_fractal == "Gosper":
                turtle.bgcolor("hotpink")
            elif tipo_fractal == "Curva de dragón":
                turtle.bgcolor("khaki")

            if tipo_fractal == "CurvaLecyC":
                curva_levy = CurvaLecyC(num_iteraciones, 10)
                constructor_curva_levy = ConstructorFiguras(curva_levy)

                # Configuración gráfica adicional para CurvaLecyC
                turtle.pencolor("blue")
                turtle.pensize(2)

                constructor_curva_levy.construir_y_dibujar()

            elif tipo_fractal == "FlechaSierpinski":
                flecha_sierpinski = FlechaSierpinski(num_iteraciones, 10)
                constructor_flecha_sierpinski = ConstructorFiguras(flecha_sierpinski)

                # Configuración gráfica adicional para FlechaSierpinski
                turtle.pencolor("green")
                turtle.pensize(2)

                constructor_flecha_sierpinski.construir_y_dibujar()

            elif tipo_fractal == "Koch":
                koch = Koch(num_iteraciones, 10)
                constructor_koch = ConstructorFiguras(koch)

                # Configuración gráfica adicional para Koch
                turtle.pencolor("red")
                turtle.pensize(2)

                constructor_koch.construir_y_dibujar()

            elif tipo_fractal == "Gosper":
                gosper = Gosper(num_iteraciones, 10)
                constructor_gosper = ConstructorFiguras(gosper)

                # Configuración gráfica adicional para Gosper
                turtle.pencolor("purple")
                turtle.pensize(2)

                constructor_gosper.construir_y_dibujar()

            elif tipo_fractal == "Curva de dragón":
                dragon_curve = DragonCurve(num_iteraciones, 10)
                constructor_dragon_curve = ConstructorFiguras(dragon_curve)

                # Configuración gráfica adicional para Curva de dragón
                turtle.pencolor("orange")
                turtle.pensize(2)

                constructor_dragon_curve.construir_y_dibujar()

            # Espera 3 segundos
            time.sleep(3)
            
            respuesta = messagebox.askyesno("Continuar", "¿Desea graficar otro fractal?")
            
            if respuesta:
                # Restablece la posición de la tortuga al centro
                turtle.goto(0, 0)
                # Borra lo graficado en la ventana Turtle
                turtle.clear()
                return
            else:
                # Cierra ambas ventanas
                self.master.destroy()
                self.sistema_ventanas.turtle_window.bye()
                return

def main():
    ventana = tk.Tk()
    app = SistemaVentanas(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()

""" Curva del Dragón """

from turtle import *
import time
import random

class DragonCurve:
    def __init__(self):
        self.iteraciones = 13
        self.tam = 3

    def set_iteraciones(self, iteraciones):
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")
        self.iteraciones = iteraciones

    def get_iteraciones(self):
        return self.iteraciones

    def set_tam(self, tam):
        if type(tam) != int or tam <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tam = tam

    def get_tam(self):
        return self.tam

    def alterar_color(self, incremento):
        colores = pencolor()
        nuevo_color = (colores[0] + incremento) % 255, (colores[1] + incremento) % 255, (colores[2] + incremento) % 255
        pencolor(nuevo_color)

    def color_aleatorio(self):
        pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def generar_lista(self):
        L = ["D"]
        for i in range(self.iteraciones):
            L = L + ["D"] + ["I" if x == "D" else "D" for x in L[::-1]]
        return L

    def dibujar_curva(self):
        for instruccion in self.lista:
            forward(self.tam)
            if instruccion == "D":
                right(90)
            else:
                left(90)
        forward(self.tam)

    def curva_dragon(self):
        tracer(0, 0)
        reset()
        hideturtle()
        pensize(2)
        colormode(255)
        bgcolor(0, 0, 0)
        for direccion in range(0, 360, 90):
            self.lista = self.generar_lista()
            penup()
            home()
            setheading(direccion)
            pendown()
            self.color_aleatorio()
            self.dibujar_curva()
            update()

if __name__ == "__main__":
    dragon_curve = DragonCurve()
    dragon_curve.curva_dragon()
    time.sleep(25)
    done()

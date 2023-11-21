""" Curva del Dragón """

from turtle import *
import random
from Clases_Fractales import Fractal

class DragonCurve(Fractal):
    
    def alterar_color(self, incremento):
        colores = pencolor()
        nuevo_color = (colores[0] + incremento) % 255, (colores[1] + incremento) % 255, (colores[2] + incremento) % 255
        pencolor(nuevo_color)

    def color_aleatorio(self):
        pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def generar_lista(self):
        self.lista = ["D"]
        for i in range(self.get_iteraciones()):
            self.lista = self.lista + ["D"] + ["I" if x == "D" else "D" for x in self.lista[::-1]]
        return self.lista

    def dibujar_curva(self):
        for instruccion in self.lista:
            forward(self.get_tamano())
            if instruccion == "D":
                right(90)
            else:
                left(90)
        forward(self.get_tamano())

    def curva_dragon(self):
        tracer(0, 0)
        reset()
        hideturtle()
        pensize(2)
        colormode(255)
        bgcolor(0, 0, 0)
        for direccion in range(0, 360, 90):
            self.generar_lista()  
            penup()
            home()
            setheading(direccion)
            pendown()
            self.color_aleatorio()
            self.dibujar_curva()
            update()
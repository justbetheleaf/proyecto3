""" Curva de Levy C"""

from turtle import *
from Clases_Fractales import Fractal

class CurvaLecyC(Fractal):
    def generar_lista(self):
        lista = ['A']
        for _ in range(self.get_iteraciones()):
            nuevaLista = []
            for elemento in lista:
                if elemento == 'A':
                    nuevaLista.extend([45, 'A', -45, -45, 'A', 45])
                else:
                    nuevaLista.append(elemento)
            lista = nuevaLista
        return lista

    def dibujar_curva(self):
        lista_instrucciones = self.generar_lista()
        for instruccion in lista_instrucciones:
            if instruccion == 'A':
                forward(self.get_tamano())
            elif isinstance(instruccion, int):
                right(instruccion)

    def curvaLevy_grafico(self):
        tracer(0, 0)
        reset()
        hideturtle()
        pensize(2)
        colormode(255)
        bgcolor(0, 0, 0)
        penup()
        home()
        pendown()
        pencolor(255, 255, 255)
        self.dibujar_curva()
        update()
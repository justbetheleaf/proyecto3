""" Curva de punta de flecha Sierpinski """
from turtle import *
from fractal import Fractal

class FlechaSierpinski(Fractal):
    def generar_lista(self):
        lista = ['D', 'D']
        for _ in range(self.get_iteraciones()):
            nuevaLista = []
            direccionAnterior = 'I' if lista[0] == 'D' else 'D'
            nuevaLista.extend([direccionAnterior, direccionAnterior])
            for i, elemento in enumerate(lista):
                nuevaLista.append(elemento)
                direccion = 'I' if direccionAnterior == 'D' else 'D'
                nuevaLista.extend([direccion, direccion])
                direccionAnterior = direccion
            lista = nuevaLista
        return lista

    def dibujar_curva(self):
        lista_instrucciones = self.generar_lista()
        for instruccion in lista_instrucciones:
            forward(self.get_tamano())
            if instruccion == 'D':
                right(60)
            elif instruccion == 'I':
                left(60)

    def curvaSierpinski_grafico(self):
        tracer(0, 0)
        reset()
        hideturtle()
        pensize(2)
        colormode(255)
        bgcolor(0, 0, 0)
        penup()
        home()
        left(90)
        #pendown()
        pencolor(44, 54, 206)
        self.dibujar_curva()
        update()
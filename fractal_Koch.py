from turtle import *
from fractal import Fractal

class Koch(Fractal):
    def generar_lista(self):
        lista = ['F']
        for _ in range(self.get_iteraciones()):
            nueva_lista = []
            for elemento in lista:
                if elemento == 'F':
                    nueva_lista.extend(['F', '-', 'F', '+', '+', 'F', '-', 'F'])
                else:
                    nueva_lista.append(elemento)
            lista = nueva_lista
        return lista

    def dibujar_curva(self):
        lista = self.generar_lista()
        for elemento in lista:
            if elemento == 'F':
                forward(self.get_tamano())
            elif elemento == '+':
                left(60)
            elif elemento == '-':
                right(60)
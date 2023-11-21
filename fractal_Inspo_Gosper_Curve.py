""" fractal Helecho  """

from turtle import *
from fractal import Fractal

class GosperInspiredCurve(Fractal):
    def generar_lista(self):
        instrucciones = ['A']
        for _ in range(self.get_iteraciones()):
            nuevas_instrucciones = []
            for instruccion in instrucciones:
                if instruccion == 'A':
                    nuevas_instrucciones.extend(['B', '-', 'A', '-', 'B'])
                elif instruccion == 'B':
                    nuevas_instrucciones.extend(['A', '+', 'B', '+', 'A'])
                else:
                    nuevas_instrucciones.append(instruccion)
            instrucciones = nuevas_instrucciones
        return instrucciones

    def dibujar_curva(self):
        instrucciones = self.generar_lista()
        for instruccion in instrucciones:
            if instruccion == 'A' or instruccion == 'B':
                forward(self.get_tamano())
            elif instruccion == '+':
                left(45)
            elif instruccion == '-':
                right(45)
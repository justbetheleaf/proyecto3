""" fractal Helecho  """

from turtle import *
import time
import random

from turtle import *
import time
import random

class HeptagonoGosper:
    def __init__(self):
        self.iteraciones = 3
        self.tamano = 5

    def set_iteraciones(self, iteraciones):
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")
        self.iteraciones = iteraciones

    def set_tamano(self, tamano):
        if type(tamano) != int or tamano <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tamano = tamano

    def generar_lista(self):
        instrucciones = ['A']

        for _ in range(self.iteraciones):
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

    def dibujar(self, instrucciones):
        for instruccion in instrucciones:
            if instruccion == 'A' or instruccion == 'B':
                forward(self.tamano)
            elif instruccion == '+':
                left(45)
            elif instruccion == '-':
                right(45)

def main():
    ventana = Screen()
    ventana.bgcolor("white")

    tortuga = Turtle()
    
    tortuga.speed(0)
    tortuga.color("blue")

    heptagono_gosper = HeptagonoGosper()
    heptagono_gosper.set_iteraciones(10)  # Puedes ajustar el número de iteraciones aquí
    heptagono_gosper.set_tamano(5)

    instrucciones = heptagono_gosper.generar_lista()
    heptagono_gosper.dibujar(instrucciones)

    ventana.exitonclick()

if __name__ == "__main__":
    main()



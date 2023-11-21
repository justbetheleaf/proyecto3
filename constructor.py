from turtle import *

class ConstructorFiguras:
    def __init__(self, figura):
        self.figura = figura

    def construir_y_dibujar(self):
        iteraciones = self.figura.get_iteraciones()
        tamano = self.figura.get_tamano()
        self.figura.generar_lista()
        self.figura.dibujar_curva()


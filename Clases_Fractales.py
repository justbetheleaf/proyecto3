from turtle import *

class Fractal:
    def __init__(self, iteraciones, tamano):
        self._iteraciones = iteraciones
        self._tamano = tamano

    def get_iteraciones(self):
        return self._iteraciones

    def set_iteraciones(self, iteraciones):
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")
        self._iteraciones = iteraciones

    def get_tamano(self):
        return self._tamano

    def set_tamano(self, tamano):
        if type(tamano) != int or tamano <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self._tamano = tamano

class ConstructorFiguras:
    def __init__(self, figura):
        self.figura = figura

    def construir_y_dibujar(self):
        iteraciones = self.figura.get_iteraciones()
        tamano = self.figura.get_tamano()
        self.figura.generar_lista()
        self.figura.dibujar_curva()





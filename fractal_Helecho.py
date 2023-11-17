""" fractal Helecho  """

import turtle
import random

class BarnsleyFernTurtle:
    def __init__(self):
        self._iteraciones = 5000
        self._tamaño = 35
        self._turtle = turtle.Turtle()
        self._screen = turtle.Screen()
        self._screen.bgcolor('black')
        self._points = [(0, 0)]

    def set_iteraciones(self, iteraciones):
        self._iteraciones = iteraciones

    def get_iteraciones(self):
        return self._iteraciones

    def set_tamaño(self, tamaño):
        self._tamaño = tamaño

    def get_tamaño(self):
        return self._tamaño

    def generar_helecho(self):
        x, y = 0, 0

        for _ in range(self._iteraciones):
            r = random.uniform(0, 100)

            if r < 1:
                x, y = 0, 0.16 * y
            elif r < 86:
                x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
            elif r < 93:
                x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
            else:
                x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

            self._points.append((x, y))

    def dibujar_helecho(self):
        self._turtle.speed(0)
        self._turtle.penup()
        self._screen.tracer(0)

        for point in self._points:
            x, y = point
            scaled_x = x * self._tamaño
            scaled_y = y * self._tamaño

            # Asignar un color aleatorio a cada punto
            color = (random.random(), random.random(), random.random())
            self._turtle.color(color)
            
            self._turtle.goto(scaled_x, scaled_y)
            self._turtle.dot(2)

            self._screen.update()

        self._screen.exitonclick()

if __name__ == "__main__":
    helecho_tortuga = BarnsleyFernTurtle()
    helecho_tortuga.set_iteraciones(5000)
    helecho_tortuga.set_tamaño(35)
    helecho_tortuga.generar_helecho()
    helecho_tortuga.dibujar_helecho()

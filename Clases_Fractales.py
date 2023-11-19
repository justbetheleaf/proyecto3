from turtle import *
import random
import time

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
        left(180)
        pendown()
        pencolor(255, 255, 255)
        self.dibujar_curva()
        update()

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

class Gosper(Fractal):
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

class ConstructorFiguras:
    def __init__(self, figura):
        self.figura = figura

    def construir_y_dibujar(self):
        iteraciones = self.figura.get_iteraciones()
        tamano = self.figura.get_tamano()
        self.figura.generar_lista()
        self.figura.dibujar_curva()

if __name__ == "__main__":
    
    curva_levy = CurvaLecyC(4, 10)
    flecha_sierpinski = FlechaSierpinski(4, 10) # Recuerde que estos valores se pueden modificar 
    koch = Koch(4, 10)
    gosper = Gosper(4, 10)
    dragon_curve = DragonCurve(4, 10)

    constructor_curva_levy = ConstructorFiguras(curva_levy)
    constructor_flecha_sierpinski = ConstructorFiguras(flecha_sierpinski)
    constructor_koch = ConstructorFiguras(koch)
    constructor_gosper = ConstructorFiguras(gosper)
    constructor_dragon_curve = ConstructorFiguras(dragon_curve)

    """No se pueden ejecutar todos al mismo tiempo pero dependen cuando se llamen"""
    
    #constructor_curva_levy.construir_y_dibujar()
    #time.sleep(5)

    #constructor_flecha_sierpinski.construir_y_dibujar()
    #time.sleep(5)

    #constructor_koch.construir_y_dibujar()
    #time.sleep(5)

    #constructor_dragon_curve.construir_y_dibujar()
    #time.sleep(5)

    constructor_gosper.construir_y_dibujar()
    time.sleep(5)

    done()



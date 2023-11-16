""" Curva de punta de flecha Sierpinski """


from turtle import *
import time

class Flecha_Sierpinski:  # Clase principal
    
    def __init__(self):  # Constructor de la clase
        self.iteraciones = 0  # Propiedades
        self.tam = 1

    def set_iteraciones(self, iteraciones):  # Para cambiar la cantidad de iteraciones
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")  # Verifica que sea entero positivo
        self.iteraciones = iteraciones

    def get_iteraciones(self):  # Devuelve la cantidad de iteraciones
        return self.iteraciones

    def set_tam(self, tam):  # Cambia el tamaño de la forma
        if type(tam) != int or tam <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tam = tam

    def get_tam(self):  # Devuelve el tamaño actualizado
        return self.tam

    def generar_lista(self):
        lista = ['D', 'D']  # Inicializa con la curva más simple [D, D]
        for _ in range(self.iteraciones):
            nuevaLista = []
            direccion = 'I' if lista[0] == 'D' else 'D'  # Determina la dirección inicial
            for i, elemento in enumerate(lista):
                nuevaLista.extend([direccion, direccion])
                nuevaLista.append(elemento)
                direccion = 'D' if direccion == 'I' else 'I'
            lista = nuevaLista
        return lista

    def dibujar_curva(self, lista):
        for instruccion in lista:
            forward(self.tam)
            if instruccion == 'D':
                right(60)  # Ángulo de 60 grados a la derecha
            elif instruccion == 'I':
                left(60)   # Ángulo de 60 grados a la izquierda

    def curvaSierpinski_grafico(self):  # Corregido la indentación aquí
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
        lista_instrucciones = self.generar_lista()
        self.dibujar_curva(lista_instrucciones)
        update()

if __name__ == "__main__":
    sierpinski_main = Flecha_Sierpinski()  # Creando una instancia de la nueva clase
    sierpinski_main.set_iteraciones(8)  # Configurando las iteraciones
    sierpinski_main.curvaSierpinski_grafico()  # Llamada a la función para dibujar la curva
    time.sleep(5)
    done()

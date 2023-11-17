""" Curva de punta de flecha Sierpinski """


from turtle import *
import time

class Flecha_Sierpinski:  # Clase principal
    
    def __init__(self):  # Constructor de la clase
        self.iteraciones = 0  # Propiedades
        self.tamano = 3

    def set_iteraciones(self, iteraciones):  # Para cambiar la cantidad de iteraciones
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")  # Verifica que sea entero positivo
        self.iteraciones = iteraciones

    def get_iteraciones(self):  # Devuelve la cantidad de iteraciones
        return self.iteraciones

    def set_tamano (self, tamano):  # Cambia el tamaño de la forma
        if type(tamano ) != int or tamano <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tamano = tamano 

    def get_tamano (self):  # Devuelve el tamaño actualizado
        return self.tamano     
    
    def generar_lista(self):
        lista = ['D', 'D']  
        for _ in range(self.iteraciones):
            nuevaLista = []
            direccionAnterior = 'I' if lista[0] == 'D' else 'D'  # Determina la dirección inicial
            nuevaLista.extend([direccionAnterior, direccionAnterior])
            for i, elemento in enumerate(lista):
                nuevaLista.append(elemento)
                direccion = 'I' if direccionAnterior == 'D' else 'D'  # Determina la dirección inicial
                nuevaLista.extend([direccion, direccion])
                direccionAnterior = direccion
            lista = nuevaLista
        return lista

    def dibujar_curva(self, lista):
        for instruccion in lista:
            forward(self.tamano )
            if instruccion == 'D':
                right(60)  # Ángulo de 60 grados a la derecha
            elif instruccion == 'I':
                left(60)   # Ángulo de 60 grados a la izquierda

    def curvaSierpinski_grafico(self):  
        tracer(0, 0)  #desactiva la animación
        reset()   # reinicia la ventana 
        hideturtle()  # oculta el cursos (turtle) 
        pensize(2) #grueso de linea
        colormode(255)  # modo de color 
        bgcolor(0, 0, 0) #el fondo de la ventana(negro)
        penup() #el dibujo no dejarán una marca en la ventana de dibujo cuando se mueva la tortuga
        home() #mueve la tortuga a su posición de inicio (0, 0) 
        left(180)
        pendown() #o que permite que las instrucciones de dibujo dejen una marca en la ventana
        pencolor(255, 255, 255) #color del lápiz de dibujo en (blanco)
        lista_instrucciones = self.generar_lista()
        self.dibujar_curva(lista_instrucciones)
        update()

if __name__ == "__main__":
    sierpinski_main = Flecha_Sierpinski()  # Creando una instancia de la nueva clase
    sierpinski_main.set_iteraciones(8)  # Configurando las iteraciones
    sierpinski_main.curvaSierpinski_grafico()  # Llamada a la función para dibujar la curva
    time.sleep(5)
    done()

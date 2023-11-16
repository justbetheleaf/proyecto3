""" Curva de Levy C"""

from turtle import *
import time

class curvaLecyC:  #clase principal
    
    def __init__(self): #constructor de la clase
        self.iteraciones = 0  #propiedades
        self.tam = 8

    def set_iteraciones(self, iteraciones):  #para cambiar la cantidad de iteraciones 
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.") #verifica que sea entero positivo
        self.iteraciones = iteraciones

    def get_iteraciones(self): #devuelve la cantidad de iteraciones
        return self.iteraciones

    def set_tam(self, tam): #cambia el tamaño de la forma
        if type(tam) != int or tam <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tam = tam

    def get_tam(self): #devuelve el tamaño actualizado
        return self.tam

    def generar_lista(self):  # da las instrucciones para dibujar la curva 
        lista = ['A']  # Inicializa en A
        
        for _ in range(self.iteraciones): #bucle con cantidad de iteraciones configuradas
            nuevaLista = [] #inicia una lista en cada iteración
            
            for elemento in lista:
                if elemento == 'A':  #verifica si el elemento es = a A
                    nuevaLista.extend([45, 'A', -45, -45, 'A', 45]) #sustitución: A -> D A I I A D
                else:
                    nuevaLista.append(elemento) #si el elemento no es A no se realiza la susti
            lista = nuevaLista #actualiza en el lista
            
        return lista #devuelve la lista

    def dibujar_curva(self, lista): #utiliza instrucciones para dibujar en la clase levy
        
        for instruccion in lista: #recorre cada elem de la lista
            
            if instruccion == 'A': #si encuentra una A avanza en la misma dirección
                forward(self.tam) #distancia que se avanza se config por el valor de self.tam
                
            elif isinstance(instruccion, int): #si no es igual a A se ve si es un entero enla fun instance
                right(instruccion)  # Instrucción de ángulo

    def curvaLevy_grafico(self): #combina todos los metodos para generar la curva
        
        tracer(0, 0)  #desactiva la animación
        reset()   # reinicia la ventana 
        hideturtle()  # oculta el cursos (turtle) 
        pensize(2) #grueso de linea
        colormode(255)  # modo de color 
        bgcolor(0, 0, 0) #el fondo de la ventana(negro)
        penup() #el dibujo no dejarán una marca en la ventana de dibujo cuando se mueva la tortuga
        home() #mueve la tortuga a su posición de inicio (0, 0) 
        pendown() #o que permite que las instrucciones de dibujo dejen una marca en la ventana
        pencolor(255, 255, 255) #color del lápiz de dibujo en (blanco)
        lista_instrucciones = self.generar_lista()  #llama metodo  parar obtener instrucciones y se almacenan 
        self.dibujar_curva(lista_instrucciones)  #pasa la lista de instrucciones parae dibujar la curva
        update()  #actualiza

if __name__ == "__main__": # principal
    levy_main = curvaLecyC() #crea instancia de la clase
    levy_main.set_iteraciones(10)  # Puede cambiar el número de iteraciones aquí
    levy_main.curvaLevy_grafico() #llama la curva para generarla
    time.sleep(25) #25 segundos antes de cerrar la ventana 
    done() #cierra ventana

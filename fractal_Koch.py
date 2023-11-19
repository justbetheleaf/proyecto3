from turtle import *

class CopoDeNieveKoch:
    def __init__(self):
        self.iteraciones = 0
        self.tamano = 8

    def set_iteraciones(self, iteraciones):
        if type(iteraciones) != int or iteraciones < 0:
            raise ValueError("Las iteraciones deben ser un entero no negativo.")
        self.iteraciones = iteraciones

    def set_tamano(self, tamano):
        if type(tamano) != int or tamano <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.tamano = tamano

    def generar_instrucciones(self):
        instrucciones = ['F']

        for _ in range(self.iteraciones):
            nuevas_instrucciones = []

            for instruccion in instrucciones:
                if instruccion == 'F':
                    nuevas_instrucciones.extend(['F', '-', 'F', '+', '+', 'F', '-', 'F'])
                else:
                    nuevas_instrucciones.append(instruccion)

            instrucciones = nuevas_instrucciones

        return instrucciones

    def dibujar_curva(self, instrucciones):
        for instruccion in instrucciones:
            if instruccion == 'F':
                forward(self.tamano)
            elif instruccion == '+':
                left(60)
            elif instruccion == '-':
                right(60)

def main():
    ventana = Screen()
    ventana.bgcolor("white")

    tortuga = Turtle()
    
    tortuga.speed(0)
    tortuga.color("blue")

    copo_nieve = CopoDeNieveKoch()
    copo_nieve.set_iteraciones(10)  # Puedes ajustar el número de iteraciones aquí
    copo_nieve.set_tamano(6)

    instrucciones = copo_nieve.generar_instrucciones()
    copo_nieve.dibujar_curva(instrucciones)

    ventana.exitonclick()

if __name__ == "__main__":
    main()




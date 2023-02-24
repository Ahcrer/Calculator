#Se hará una calculadora sencilla, esta deberá:
#1.Sumar
#2.Restar
#3.Multiplicar
#4.Dividir

import funciones

def main():
    continuar = True
    while continuar:
        print('Seleccione una operación:')
        print('1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n0-Salir')
        operacion = input()
        if operacion == "1":
            #codigo para sumar
            funciones.sumar()
        elif operacion == "2":
            #codigo para restar
            funciones.restar()
        elif operacion == "3":
            #codigo para multiplicar
            funciones.multiplicar()
        elif operacion== "4":
            #codigo para dividir
            funciones.dividir()
        elif operacion== "0":
            #Finalizar
            continuar = False
        else:
            print('Entrada incorrecta')

if __name__ == "__main__":
    main()
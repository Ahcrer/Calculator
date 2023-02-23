#Se hará una calculadora sencilla, esta deberá:
#1.Sumar
#2.Restar
#3.Multiplicar
#4.Dividir

def main():
    continuar = True
    while continuar:
        print('Seleccione una operación:')
        print('1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n0-Salir')
        operacion = input()
        if operacion == "1":
            #codigo para sumar
            sumar()
        elif operacion == "2":
            #codigo para restar
            restar()
        elif operacion == "3":
            #codigo para multiplicar
            multiplicar()
        elif operacion== "4":
            #codigo para dividir
            dividir()
        elif operacion== "0":
            #Finalizar
            continuar = False
        else:
            print('Entrada incorrecta')

def sumar():
    num1 = input("Ingresar el primer número: ")
    num2 = input("ingresar el segundo número: ")
    print("La suma es: " + str(int(num1) + int(num2)))

def restar():
    num1 = input("Ingresar el primer número: ")
    num2 = input("ingresar el segundo número: ")
    print("La resta es: " + str(int(num1) - int(num2)))

def multiplicar():
    num1 = input("Ingresar el primer número: ")
    num2 = input("ingresar el segundo número: ")
    print("La multiplicación es: " + str(int(num1) * int(num2)))

def dividir():
    num1 = input("Ingresar el primer número: ")
    num2 = input("ingresar el segundo número: ")
    print("La división es: " + str(int(num1) / int(num2)))

if __name__ == "__main__":
    main()
#Se hará una calculadora sencilla, esta deberá:
#1.Sumar
#2.Restar
#3.Multiplicar
#4.Dividir

import funciones

def main():
    print("")
    usuario = ""
    contrasena = ""
    continuar0 = "a"
    while continuar0 == "a":
        print("Bienvenido a calculadora para GCS\n¿Qué desea hacer?")
        print("1-Ingresar\n2-Registrarse\n0-Salir")
        operacion0 = input()
        if operacion0 == "1":
            usuario = input("Ingresar usuario: ")
            contrasena = input("Ingresar contraseña: ")
            validar_credenciales(usuario, contrasena)
            while True:
                operaciones()
                return False
        elif operacion0 == "2":
            usuario = input("Crear usuario: ")
            contrasena = input("Crear contraseña: ")
            crear_usuario(usuario, contrasena)
        elif operacion0 == "0":
            #Se sale del ciclo y cierra el programa
            continuar0 = "b"
        else:
            print("Opcion invalida")

def operaciones():
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

def crear_usuario(usuario, contrasena):
    with open("password.txt", "a") as archivo:
        archivo.write(f"{usuario},{contrasena}\n")

def validar_credenciales(usuario, contrasena):
    with open("password.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            usuario_archivo, contrasena_archivo = linea.strip().split(",")
            if usuario == usuario_archivo and contrasena == contrasena_archivo:
                return True
        return False

if __name__ == "__main__":
    main()
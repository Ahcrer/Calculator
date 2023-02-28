#Se hará una calculadora sencilla, esta deberá:
#1.Sumar
#2.Restar
#3.Multiplicar
#4.Dividir
#Tendrá un sistema de usuario y contraseña para que solo los miembros registrados
#puedan utilizarla.

import funciones
import csv

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
            verifica_usuario(usuario, contrasena)
            while True: #Problema
                operaciones()
                return False
        elif operacion0 == "2":
            usuario = input("Crear usuario: ")
            contrasena = input("Crear contraseña: ")
            crear_usuario(usuario, contrasena, 'usuarios.csv')
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
            try:
                funciones.dividir()
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        elif operacion== "0":
            #Finalizar
            continuar = False
        else:
            print('Entrada incorrecta')

def crear_usuario(usuario, contrasena, archivo):
    with open(archivo, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([usuario, contrasena])

def leer_archivo_csv(archivo:str)->str:
    '''lee el archivo y regresa un lista de listas'''
    data = []
    try:
        with(open(archivo,'r', encoding='utf-8')) as a:
            data = csv.reader(a)
            data = [linea for linea in data]
    except(FileNotFoundError, IOError):
        print(f'No existe el archivo {archivo}')
    return data

def verifica_usuario(usuario:str, contrasena:str)->bool:
    '''Verifica que el usuario y la contraseña sean correctos'''
    lista = leer_archivo_csv("usuarios.csv")
    diccionario = {usuario[0]:usuario[1] for usuario in lista}
    if usuario in diccionario:
        if diccionario[usuario] == contrasena:
            return True
    return False

if __name__ == "__main__":
    main()
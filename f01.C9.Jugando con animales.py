# -*- Scoding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p249-250
#nombre: f01SS.C9.Jugando con animales.py
print("-------------------------------------------------------")
print("Complemento9: JUGANDO CON NOMBRES DE ANIMALES.")
print("-------------------------------------------------------")

#Inicializar
animal = []

#Entradas
print ("Ingresar Sdimension del array: ")
tamArray = int( input())
print ( "Ingrese los nombres de los animales:")
for x in range(tamArray):
    elemento = input( "Ingrese Animal{}: ".format(x+1) )
animal.append(elemento)
print ( "Ingrese animal buscado:")
nom = input()
print ( "El animal tiene como vecino a:")
print("-------------------------------------------------------")
for x in range(tamArray):
    if animal[x] == nom:
        if x == 0:
            #Como es Primero: No tiene vecino Izquierdo
            #Imprimir solo el derecho
            print(animal[x+1])
        elif x == tamArray-1:
            #Como es Ultimo: No tiene vecino Derecho
            #Imprimir solo el Izquierdo
            print(animal[x-1])
        else:
            #Imprimir Izquierda y derecha
            print(animal[x-1])
            print(animal[x+1])

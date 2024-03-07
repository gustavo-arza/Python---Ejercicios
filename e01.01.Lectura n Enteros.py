# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p209
#Nombre del Algoritmo: 01.Lectura n Enteros.py 
print("-------------------------------------------------------")
print("Vector1: LECTURA DE N ELEMENTOS ENTEROS.")
print("-------------------------------------------------------")
#inicializar
i = 1
F = [] #Inicializamos una LISTA VACÍA
#Entrada
print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())
#Proceso
while i <= numElementos:
elemento = int( input("Ingrese Elemento: "))
F.append(elemento) #Agregamos el elemento a la lista
i = i + 1
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(F) #Imprimimos la lista


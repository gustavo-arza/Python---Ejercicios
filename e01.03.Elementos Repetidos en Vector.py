# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p212
#Nombre del Algoritmo: e01.03.Elementos Repetidos en Vector.py
print("-------------------------------------------------------")
print("Vector3: ORDENAR Y QUITAR ELEMENTOS REPETIDOS DEL VECTOR.")
print("-------------------------------------------------------")

#Inicializar
VEC = [] #Inicializamos una lista vacía

#Entradas
print("Ingrese número de elementos del vector")
N = int( input())

#Proceso
if 1 <= N and N <= 200:
for i in range(1,N+1):
elemento = int( input("Ingrese Entero {0}: ".format(i)))
VEC.append(elemento)
i = 0
#TODO:Reportar Array como Imcompleto
lista_nueva = [] #Una lista vacía para poner los elementos sin repetición.
for elemento in VEC:

#Si el elemento no esta en la lista_nueva:
if elemento not in lista_nueva:
lista_nueva.append(elemento) #Agregamos elemento

#ordenamos la lista usando una función de lista en Python
#USANDO SORT
lista_nueva.sort()

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(lista_nueva)

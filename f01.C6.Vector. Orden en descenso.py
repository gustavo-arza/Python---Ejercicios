# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p242
#nombre: f01.C6.Vector. Orden en descenso.py
print("-------------------------------------------------------")
print("Complemento6: ORDENAR DESCENDENTEMENTE EL VECTOR.")
print("-------------------------------------------------------")

#Inicializar
V1 = []

#Entradas
print ( "Ingrese cantidad de elementos del vector: ")
n = int( input())
print ( "Ingrese los valores del vector: ")
for x in range(n):
valor = int( input("V{}: ".format(x+1)))
V1.append(valor)

#Proceso
print ( "Los elementos del vector son: ")
for y in range(n):
for x in range(n-1):
if V1[x] < V1[x+1]:
m = V1[x]
V1[x] = V1[x+1]
V1[x+1] = m
print(V1)

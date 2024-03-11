# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p244
#nombre: f01.C7.Vector. Orden en ascenso.py
print("-------------------------------------------------------")
print("Complemento7: INGRESAR VALOR EN EL VECTOR ASCENDENTE.")
print("-------------------------------------------------------")

#Inicializar
V = []

#Entradas
print("Ingrese los 10 valores del vector: ")
for i in range(10):
valor = int( input("valor {}: ".format(i+1)))
V.append(valor)
valor11 = int( input("Ingrese valor a insertar: "))
V.append(valor11)

#Proceso
#Ordenar el vector
for x in range(11):
for y in range(10):
if V[y] > V[x]:
a = V[y]
V[y] = V[x]
V[x] = a

#Mostrar los elementos del vector
for x in range(11):
print(V[x])

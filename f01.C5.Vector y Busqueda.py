# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p340
#nombre: f01.C5.Vector y Busqueda.py
print("-------------------------------------------------------")
print("Complemento5: BUSCAR ELEMENTO DENTRO DEL ARRAY.")
print("-------------------------------------------------------")

#Inicializar
valor = []

#Entradas
print ("Ingrese n�mero de elementos del arreglo")
m = int( input())
print ("Ingrese los elementos del arreglo")
for i in range(m) :
elemento = int( input("Ingrese Elemento: "))
valor.append(elemento)

#B�squeda del valor dentro del arreglo
print ("Ingrese el valor buscado: ")
bus = int( input())
print ("La posici�n del valor buscado ser�:")
for i in range(m) :
if valor[i] == bus :
r = i
print ("La posici�n del elemento es", r+1)
break

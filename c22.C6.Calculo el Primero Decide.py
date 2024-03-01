# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p140
#nombre: c22.C6.Calculo el Primero Decide.py
# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento6: NÚMEROS, EL PRIMERO DECIDE.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese los 3 números:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))
#Proceso
if a < 0 :
r = a*b*c
else:
r = a + b + c
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(r)

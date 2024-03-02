# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p142-143
#nombre: c23.C7.RaicesCuadraticas.py
print("-------------------------------------------------------")
print("Complemento7: RAÍCES DE ECUACIÓN CUADRÁTICA.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese valores de la ecuación cuadrática:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))

#Proceso
d = b**2 - 4*a*c

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if d > 0 :
x1 = ( (-b) + d**0.5 )/ 2*a
x2 = ( (-b) - d**0.5 )/ 2*a
print("Raíces reales:", x1, x2)
else:
print("Raíces Irracionales")

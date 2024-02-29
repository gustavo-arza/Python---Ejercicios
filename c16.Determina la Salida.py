# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p124-125
#nombre: c16.Determina la Salida.py
print("-------------------------------------------------------")
print("Ejercicio16: DETERMINA LA SALIDA.")
print("-------------------------------------------------------")
#Entradas
A = int( input("Ingrese A: "))
B = int( input("Ingrese B: "))
C = int( input("Ingrese C: "))
print("\nSALIDA: ")
print("-------------------------------------------------------")
#Proceso
if A > B :
if A > C:
if B > C:
print(A, B, C)
else:
print(A,C,B)
else:
print(C,A,B)
else:
if B > C :
if A > C :
print(B,A,C)
else:
print(B,C,A)
else:
print(C,B,A)

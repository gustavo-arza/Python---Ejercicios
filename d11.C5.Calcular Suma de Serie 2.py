# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p178
#nombre: d11.C5.Calcular Suma de Serie 2.py
print("-------------------------------------------------------")
print("Complemento5: CALCULAR SUMA DE SERIE 2.")
print("-------------------------------------------------------")

#Inicializar
S = 0

#Entradas
print ("Ingrese número de términos:")
N = int( input())

#Proceso
for x in range(1, N+1):
if x % 2 == 0 :
S = S - (1/x)
else:
S = S + (1/x)

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("La suma será:", S)

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p175-176
#nombre: d10.C4.Calcular Suma de Serie.py
print("-------------------------------------------------------")
print("Complemento4: CALCULAR SUMA DE SERIE.")
print("-------------------------------------------------------")

#Entradas
print( "Ingrese el número de términos: ")
n = int( input())

#Inicializar
s = 5
ser = 0

#Proceso
for a in range(1, n+1):
s = s + 5
ser = ser + s

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("La suma de la serie es:", ser)

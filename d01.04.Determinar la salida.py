# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p162
#nombre: d01.04.Determinar la salida.py
print("-------------------------------------------------------")
print("Ejercicio4: DETERMINAR LA SALIDA.")
print("-------------------------------------------------------")
#Constantes
#Entradas
print("Introduce un n�mero: ")
N = int( input())
while N > 0 :
RESTO = N % 10
print(RESTO)
N = N // 10 #Divisi�n Entera, N/10, es una divisi�n decimal

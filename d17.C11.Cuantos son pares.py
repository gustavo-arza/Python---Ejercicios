# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p195
#nombre: d17.C11.Cuantos son pares.py
print("-------------------------------------------------------")
print("Complemento11: CONTAR CUANTOS SON PARES.")
print("-------------------------------------------------------")

#Inicializar
i = 1
c = 0
numEntradas = 10

#proceso
print("Ingrese", numEntradas, "N�meros:")
while i <= numEntradas:
n = int( input("Ingrese n�mero: "))
if n%2 == 0 :
c = c + 1
i = i + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("En", numEntradas, "n�meros enteros hay", c, "n�meros pares")

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p168-169
#nombre: d07.C1.Contar Pares.py
print("-------------------------------------------------------")
print("Complemento1: CONTAR N�MEROS PARES.")
print("-------------------------------------------------------")

#Inicializar
c = 0

#Proceso
print("Ingrese 10 n�meros: ")
for i in range(1, 10 + 1):
num = int( input("Ingrese N�mero: "))
if num % 2 == 0 :
c = c + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Hay", c, "n�meros pares")

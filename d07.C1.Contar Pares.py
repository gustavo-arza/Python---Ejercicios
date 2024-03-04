# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p168-169
#nombre: d07.C1.Contar Pares.py
print("-------------------------------------------------------")
print("Complemento1: CONTAR NÚMEROS PARES.")
print("-------------------------------------------------------")

#Inicializar
c = 0

#Proceso
print("Ingrese 10 números: ")
for i in range(1, 10 + 1):
num = int( input("Ingrese Número: "))
if num % 2 == 0 :
c = c + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Hay", c, "números pares")

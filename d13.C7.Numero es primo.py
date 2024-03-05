# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p182-183
#nombre: d13.C7.Numero es primo.py
print("-------------------------------------------------------")
print("Complemento7: DETERMINAR SI UN NUMERO ES PRIMO.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese un numero:")
n = int( input())

#Inicializar
con = 0

#Proceso
for i in range(2, n):
if n % i == 0 :
con = con + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if con == 0:
print (n, " Es un numero primo")
else:
print (n, " No es un numero primo")

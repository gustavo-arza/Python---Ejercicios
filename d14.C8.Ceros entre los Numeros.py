# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p186
#nombre: d14.C8.Ceros entre los Numeros.py
print("-------------------------------------------------------")
print("Complemento8: NÚMERO DE CEROS ENTRE NÚMEROS.")
print("-------------------------------------------------------")

#Entradas
print ("Ingrese la cantidad de números a evaluar:")
n = int( input())
#Inicializar
c = 0

#Proceso
for i in range(1, n+1):
num = int( input("Ingrese número: "))
if num == 0 :
c = c+1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Hay ", c, " números ceros")

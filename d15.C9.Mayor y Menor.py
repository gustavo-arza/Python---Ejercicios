# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p190
#nombre: d15.C9.Mayor y Menor.py
print("-------------------------------------------------------")
print("Complemento8: N�MERO DE CEROS ENTRE N�MEROS.")
print("-------------------------------------------------------")

#Entradas
print ("Ingrese la cantidad de n�meros a evaluar:")
n = int( input())
#Inicializar
c = 0

#Proceso
for i in range(1, n+1):
num = int( input("Ingrese n�mero: "))
if num == 0 :
c = c+1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Hay ", c, " n�meros ceros")

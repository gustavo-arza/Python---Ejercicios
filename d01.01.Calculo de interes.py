# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p155
#nombre: d01.01.Calculo de interes.py
print("-------------------------------------------------------")
print("Ejercicio1: CALCULA EL INTER�S.")
print("-------------------------------------------------------")
#Inicializaci�n
C = -1
I = 0
M = 0
#Entradas
while (C<0) or (I<=0) or (I>=100) or (M <=0):
print("Introduce el capital, el inter�s y el tiempo apropiados")
C = int( input("Capital: "))
I = int( input("Inter�s: "))
M = int( input("Tiempo en A�os: "))
#Proceso
for i in range(M):
C = C*( 1 + I/100)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Tienes", C , "soles")
------------------------------------------------------

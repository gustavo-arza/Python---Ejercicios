# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p109-110
#nombre: c02.Imprimir el menor.py
print("-------------------------------------------------------")
print("Ejemplo2: IMPRIMIR EL MENOR DE DOS N�MEROS.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese 2 n�meros: ")
x = int( input("Primer N�mero: "))
y = int( input("Segundo N�mero: "))

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
#NOTA: No olvidarse de las indentaci�n.
if x > y :
#Esto esta dentro del IF
print("El menor es:", y)
else:
#Esto esta dentro del ELSE
print("El menor es:", x)
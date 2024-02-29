# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p109-110
#nombre: c02.Imprimir el menor.py
print("-------------------------------------------------------")
print("Ejemplo2: IMPRIMIR EL MENOR DE DOS NÚMEROS.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese 2 números: ")
x = int( input("Primer Número: "))
y = int( input("Segundo Número: "))

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
#NOTA: No olvidarse de las indentación.
if x > y :
#Esto esta dentro del IF
print("El menor es:", y)
else:
#Esto esta dentro del ELSE
print("El menor es:", x)
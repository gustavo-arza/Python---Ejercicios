# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p78-79
#nombre:10.CalcularAreaVolumen.py
print("-------------------------------------------------------")
print("Ejercicio10: CALCULAR �REA Y VOLUMEN DEL CILINDRO.")
print("-------------------------------------------------------")

#Constantes
PI = 3.1416

#Entradas
print("Ingrese Radio y Alto: ")
radio = float( input("Radio: "))
alto = float ( input("Alto: "))

#Proceso
vol = PI * radio**2 * alto
are = 2*PI*radio*(radio + alto)
#Salida

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Volumen:", vol)
print("Area:", are)

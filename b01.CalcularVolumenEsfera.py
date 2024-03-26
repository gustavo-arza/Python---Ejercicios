# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p81
#nombre: b01.CalcularVolumenEsfera.py

print("-------------------------------------------------------")
print("Complemento1: CALCULAR VOLUMEN DE LA ESFERA.")
print("-------------------------------------------------------")

#Constantes
PI = 3.1416

#Entradas
r = float( input("Ingrese Radio: "))

#Proceso
v = 4/3 * PI * r**3

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El volumen de la esfera es:", v)

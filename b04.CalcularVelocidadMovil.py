# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p87
#nombre: b04.CalcularVelocidadMovil.py
print("-------------------------------------------------------")
print("Complemento4: CALCULAR LA VELOCIDAD DE UN MOVIL.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese el tiempo en segundos:")
t = float( input())
print("Ingrese la distancia en metros:")
d = float( input())

#Proceso
v = d/t

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("La velocidad es:", v, "m/s")

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p98
#nombre: b09.RadiantesAOtros.py
print("-------------------------------------------------------")
print("Complemento9: RADIANES a SEXAGESIMALES y CENTESIMALES")
print("-------------------------------------------------------")
#Constantes
PI = 3.1416
#Entradas
print("Ingrese ángulo en radianes:")
x = float( input())
sex = x*180/PI
cen = x*200/PI
#Proceso
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("En sexagesimales es:", sex)
print("En centesimales es:", cen)

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p74-75
#Nombre: 8.Calcular Perimetro y Superficie.py
print("----------------------------------------------------------")
print("Ejercicio8: CALCULAR PERIMETRO Y SUPERFICIE DEL RECTANGULO")
print("----------------------------------------------------------")

#Entradas
print("Ingrese Base y Alto: ")
BASE = float( input("Base: "))
ALTO = float( input("Alto: "))

#Proceso
SUP = BASE*ALTO
PER = 2*(BASE + ALTO)

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Superficie:", SUP)
print("Perimetro:", PER)
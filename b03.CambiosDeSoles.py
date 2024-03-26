# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p85
#nombre: b03.CambiosDeSoles.py
print("-------------------------------------------------------")
print("Complemento3: CAMBIOS DE SOLES a EUROS y DOLARES")
print("-------------------------------------------------------")

#Constantes
EU = 3.84
DO = 2.28

#Entradas
print("Ingrese la cantidad de soles:")
s = float( input())

#Proceso
d = s/DO
e = s/EU

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("En", s, "soles hay ", e, "euros")
print("En", s, "soles hay ", d, "dolares")
# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p89
#nombre: b04.CalcularMontoAPagar.py
print("-------------------------------------------------------")
print("Complemento5: CALCULAR MONTO A PAGAR.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese costo unitario del art�culo:")
c = float( input())
print("Ingrese el n�mero de docenas:")
d = int( input())
#Proceso
p = d*12 * c
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El precio del art�culo es:", p)
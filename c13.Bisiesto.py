# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p117
#nombre: c13.Bisiestor.py
print("-------------------------------------------------------")
print("EjercicioN: VERIFICAR SI EL AÑO ES BISIESTO.")
print("-------------------------------------------------------")
#Entradas
anio = int( input("Ingrese año: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
print("El año es BISIESTO")
else:
print("El año NO es BISIESTO")

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p117
#nombre: c13.Bisiestor.py
print("-------------------------------------------------------")
print("EjercicioN: VERIFICAR SI EL A�O ES BISIESTO.")
print("-------------------------------------------------------")
#Entradas
anio = int( input("Ingrese a�o: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
print("El a�o es BISIESTO")
else:
print("El a�o NO es BISIESTO")

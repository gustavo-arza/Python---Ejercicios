# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p115
#nombre: c12.Sueldo a Percibir.py
print("-------------------------------------------------------")
print("Ejercicio12: SUELDO A PERCIBIR")
print("-------------------------------------------------------")
#Entradas
SUE = float( input("Ingrese Sueldo: "))
#Proceso
if SUE < 1000:
AUM = SUE*0.15
SUE = SUE + AUM
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El sueldo es:", SUE)
# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p192-193
#nombre: d16.C10.Repeticiones.py
print("-------------------------------------------------------")
print('Complemento10: CUANTAS VECES SE REPITE "a".')
print("-------------------------------------------------------")

#Inicializar
ca = 0

#Entradas
numCar = 10
print("Ingrese", numCar, "caracteres: ")

#Proceso
for i in range(0, numCar):
m = input("Ingrese Caracter: ")
if m == "a" :
ca = ca + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("En", numCar, "caracteres hay", ca, "caracteres 'a'")

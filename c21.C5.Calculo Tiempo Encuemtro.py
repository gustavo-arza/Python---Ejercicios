# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p137-138
#nombre: c21.C5.Calculo Tiempo Encuemtro.py
print("-------------------------------------------------------")
print("Complemento5: CALCULAR TIEMPO DE ENCUENTRO.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese las velocidades de ambos vehículos: ")
v1 = float( input("V1: "))
v2 = float( input("V2: "))
print("Ingrese la distancia que los separa: ")
d = float( input("Distancia: "))

#Proceso

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if v1 > 0 and v2 > 0 :
t = d/(v1+v2)
print(t, "segundos")
else:
print("ERROR")
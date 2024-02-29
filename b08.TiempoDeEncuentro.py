# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p95-96
#nombre: b08.TiempoDeEncuentro.py
print("-------------------------------------------------------")
print("Complemento8: TIEMPO DE ENCUENTRO.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese las velocidades:")
va = float( input("Va: "))
vb = float( input("Vb: "))
print("Ingrese la distancia que los separa:")
D = float( input())
#Proceso
te = D/(va+vb)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Los cuerpos se encontraran en:", te, "segundos")

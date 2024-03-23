# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p77
#Nombre: 9.Gasolinera.py
print("-------------------------------------------------------")
print("Ejercicio9: GASOLINERA.")
print("-------------------------------------------------------")

#Constantes
LITXG = 3.785       #litros por Galon
PRECIOXL = 4.50     #Precio por Litro

#Entradas
consu = float( input("Ingresar consumo total: "))

#Proceso
total = consu*LITXG*PRECIOXL

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Consumo total:", total)

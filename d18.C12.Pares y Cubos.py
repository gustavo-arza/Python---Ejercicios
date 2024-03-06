# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p198
#nombre: d18.C12.Pares y Cubos.py
print("-------------------------------------------------------")
print("Complemento12: IMPRIMIR PARES Y SUS CUBOS.")
print("-------------------------------------------------------")

#Entradas

#Inicializar
i = 2

#Proceso
while i <= 20 :
if i%2 == 0 :
p = i**3
print("El cubo de", i, "es:", p)
i = i + 1

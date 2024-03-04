# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p170
#nombre: d08.C2.Pares y Cubos.py
print("-------------------------------------------------------")
print("Complemento2: PARES Y SUS CUBOS.")
print("-------------------------------------------------------")

#Proceso
start = 2
stop = 20
step = 2 #incrementar de 2 en 2
for i in range(start, stop+1, step):
c = i**3
print("El cubo de ", i, "es ", c)
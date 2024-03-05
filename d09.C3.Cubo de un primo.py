# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p173
#nombre: d09.C3.Cubo de un primo.py
print("-------------------------------------------------------")
print("Complemento3: CUBO DE UN NÚMERO PRIMO.")
print("-------------------------------------------------------")

#Inicializar
b = 2

#Proceso
for i in range(1, 29):
co = 0
for a in range(2, b//2):
if b % a == 0 :
co = co + 1
a = b
if co == 0 :
print("El cubo de", b," es: ", b**3)
b = b + 1

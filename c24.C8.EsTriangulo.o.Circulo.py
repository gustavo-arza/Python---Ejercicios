# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p146-147
#nombre: c24.C8.EsTriangulo.o.Circulo.py
print("-------------------------------------------------------")
print("Complemento8: TRI�NGULO O C�RCULO.")
print("-------------------------------------------------------")

#Constantes
PI = 3.1416

#Entradas
print("Ingrese valores del men�:")
print("1: �rea del tri�ngulo:")
print("2: �rea del c�rculo:")
Opc = int( input("Opc: "))

#Proceso
if Opc == 1 :
print("�rea del Tri�ngulo")
print("Ingrese el lado del tri�ngulo")
L = float( input("L: "))
A = ( (3 ** 0.5)/ 4) * L**2
print("\nEl �rea del tri�ngulo es:", A)
elif Opc == 2:
print("�rea del C�rculo")
print("Ingrese el radio del c�rculo")
R = float( input("R: "))
C = PI * R**2
print("\nEl �rea del c�rculo es:", C)
else:
print("\nerror")

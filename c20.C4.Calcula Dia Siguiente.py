# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p135
#nombre: c20.C4.Calcula Dia Siguiente.py
print("-------------------------------------------------------")
print("Complemento4: CALCULA EL D�A SIGUIENTE.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese la fecha: ")
a = int( input("A�o: "))
m = int( input("Mes: "))
d = int( input("D�a: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if d > 0 and d < 30 :
print("Ma�ana es:", d+1, m, a)
else:
if m > 0 and m < 12 :
print("Ma�ana es:", 1, m+1, a)
else:
print("Ma�ana es:", 1, 1, a+1)

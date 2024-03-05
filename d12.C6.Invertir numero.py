# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p180-181
#nombre: d12.C6.Invertir numero.py
print("-------------------------------------------------------")
print("Complemento6: INVERTIR NÚMERO.")
print("-------------------------------------------------------")
#Inicializar
aux = 0
aux2 = 0

#Entradas
print("Ingrese un número: ")
n = int( input())

#Proceso
i = 10
#TODO: REPORTAR COMO ERROR
while i <= n:
aux = n%10
n = n // 10
aux2 = aux2*10 + aux
aux2 = aux2*10 + n

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El número invertido será:", aux2)

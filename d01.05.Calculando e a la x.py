# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p163-164
#nombre: d01.05.Calculando e a la x.py
print("-------------------------------------------------------")
print("Ejercicio5: CALCULANDO e^x.")
print("-------------------------------------------------------")
#Constantes
#Entradas
print("Ingrese el valor de X: ")
x = int( input())

#Inicialización
e = 1
num = 1
den = 1
i = 1

#Sería un caso de Do While
#PERO: Python no tiene implementado la sintaxis Do While
#por lo tanto habrá que ingeniárselas
#DO
num = x**i
den = den*i
i = i + 1
e = e + num/den
#WHILE
while not (num/den < 0.000001):
num = x**i
den = den*i
i = i + 1
e = e + num/den

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("e elevado al", x, "es: ", e)
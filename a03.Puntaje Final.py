# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p59-60
#Nombre: a03.Puntaje Final.py
print("-------------------------------------------------------")
print("Ejercicio3: PUNTAJE FINAL.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese n�mero de respuestas correctas: ")
RC = int( input())
print("Ingrese n�mero de respuestas incorrectas: ")
RI = int( input())
print("Ingrese n�mero de respuestas en blanco: ")
RB = int( input())
#Proceso
PCR = RC*3
PRI = RI*-1
PRB = RB*0
PF = PCR + PRI + PRB
#Salida
print("El puntaje total es:", PF)
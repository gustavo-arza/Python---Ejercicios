# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p62
#nombre: 4.PuntajedePartidos.py
#Puntaje Total de Partidos
print("-------------------------------------------------------")
print("Ejercicio4: PUNTAJE TOTAL DE PARTIDOS.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese numero de partidos ganados")
PG = int( input())
print("Ingrese numero de partidos empatados")
PE = int( input())
print("Ingrese numero de partidos perdidos")
PP = int( input())

#Proceso
PPG = PG*3
PPE = PE*1
PPP = PP*0
PF = PPG + PPE + PPP

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Puntaje Final: ", PF)

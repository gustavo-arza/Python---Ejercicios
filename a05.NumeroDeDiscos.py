# -*- coding: utf-8 -*-
import math #librer�a necesaria para usar funciones Matem�ticas
#en este caso math.ceil(), que redondea un numero al Entero superior
#extraido del libro Algoritmos resueltos con Python | p64
#nombre: a05.NumeroDeDiscos.py
print("-------------------------------------------------------")
print("Ejercicio5: N�MERO DE MICRO DISCOS 3.5 NECESARIOS")
print("-------------------------------------------------------")
#Entradas
print("Ingrese GB: ")
GB = float( input())
#Proceso
MG = GB*1024
MD = MG/1.44
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(MD)
#En caso de Decimal Aproximar al siguiente entero
#Ya que la parte decimal debe ser almacenada en otro DISCO 3.5
print("Numero de Discos necesarios: ", math.ceil(MD))
# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p120
#nombre: c14.Funcion.py
print("-------------------------------------------------------")
print("Ejercicio14: FUNCIÓN.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese valores: ")
NUM = int( input("Tipo de Calculo: "))
V = int( input("Ingrese V: "))
#Proceso
#usando un diccionario
Funcion = {
1 : 100*V,
2 : 100**V,
3 : 100/V
}
#DICCIONARIO.get(ElementoABuscarEnDiccionario, PorDefecto)
#porDefecto: En caso de que el elemnto no se encuentre.
VAL = Funcion.get(NUM, 0)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(VAL)

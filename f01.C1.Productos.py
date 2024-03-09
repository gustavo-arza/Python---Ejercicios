# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p227
#nombre: f01.C1.Productos.py
print("-------------------------------------------------------")
print("Complemento1: PRODUCTO VECTORIAL Y ESCALAR.")
print("-------------------------------------------------------")

#Inicializa
#Para inicializar vectores se puede usar:
#La operación lista por vector
#N*[ALGO] o [ALGO]*N,
#N: Es un escalar
#ALGO: Debe representar un valor por defecto
V1 = 3*[0] #Se crea el sigue vector: [0, 0, 0]
V2 = [0]*3 #Idéntico al anterior: [0, 0, 0]

#Entradas
for i in range(3):
V1[i] = int( input("V1({}): ".format(i+1)))
for i in range(3):
V2[i] = int( input("V2({}): ".format(i+1)))

#Proceso
sum = 0
for i in range(3):
P = V1[i]*V2[i]
sum = sum + P
print("El producto escalar es:", sum)
x = V1[1]* V2[2] - V1[2]* V2[1]
y = -( V1[0]* V2[2] - V1[2]* V2[0] )
z = V1[0]* V2[1] - V1[1]* V2[0]
print("El producto vectorial es: {}i {}j {}k".format(x, y, z))
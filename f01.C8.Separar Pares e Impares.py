# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p247-248
#nombre: f01.C8.Separar Pares e Impares.py
print("-------------------------------------------------------")
print("Complemento8: SEPARAR PARES E IMPARES.")
print("-------------------------------------------------------")

#Inicializar
Vec = []

#Entradas
print ("Ingrese dimensión del vector: ")
tamVec = int( input())
pares = tamVec*[0]
impares = tamVec*[0]
print ( "Ingrese los", tamVec, "valores del vector")
for x in range(tamVec):
elemento = int( input("Elemento {}: ".format(x+1)))
Vec.append(elemento)
vpr = 0
i = 0

for x in range(tamVec):
if Vec[x] % 2 == 0:
pares[vpr] = Vec[x]
vpr = vpr + 1
else:
impares[i] = Vec[x]
i = i + 1
print(pares[0:vpr]) #en [0:vpr], desde el inicio hasta vpr
print ( "El vector de pares tiene" , vpr, "elementos")
print(impares[0:i])
print ( "El vector de impares tiene", i, "elementos")Algoritmos resueltos con Python ISBN: 978-958-53018-2-5 248 / 257
if vpr > i :
print ( "El vector de pares es el más grande")
elif vpr < i:
print ( "El vector de impares es el mas grande")
else:
print ( "Los 2 vectores son iguales en número de elementos")

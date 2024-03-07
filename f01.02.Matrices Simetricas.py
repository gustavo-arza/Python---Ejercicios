# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p220
#nombre: f01.02.Matrices Simetricas.py
print("-------------------------------------------------------")
print("Matriz2: VERIFICAR SI LA MATRIZ ES SIMÉTRICA.")
print("-------------------------------------------------------")

#Inicializar
A = []

#Entradas
print("Ingrese dimensiones del arreglo")
N = int( input())

#Proceso
if 1 <= N and N <= 100:
#Ingresar datos al array
for i in range(N):
A.append( [] ) #Se agrega la fila i
for j in range(N):
elemento = input( "A{}{}: ".format(i, j) )
A[i].append( int(elemento))
BAND = True
i = 0
while i < N and BAND == True:
j = 0
while j < i-1 and BAND == True:
if A[i][j] == A[j][i]:
j = j + 1
else:
BAND = False
i = i + 1
if BAND:
print("SI ES SIMÉTRICA")
else:
print("NO ES SIMÉTRICA")
else:
print("La dimensión de la matriz no es correcta.")
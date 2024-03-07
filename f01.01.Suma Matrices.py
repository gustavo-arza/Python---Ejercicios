# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p217
#nombre: f01.01.Suma Matrices.py
print("-------------------------------------------------------")
print("Matriz1: SUMA DE MATRICES.")
print("-------------------------------------------------------")

#Inicializar
A = []
B = []
C = []

#Entradas
print ("Ingrese dimensi�n de la matriz,m�ximo 100")
S = int( input("N�mero de Filas: "))
R = int( input("N�mero Columnas: "))

#Proceso
for i in range(S):
A.append( [] ) #Agregamos una i fila vac�a en A
B.append( [] ) #Agregamos una i fila vac�a en B
C.append( [] ) #Agregamos una i fila vac�a en C
for j in range(R):
A[i].append( int( input("A{}{}: ".format(i+1,j+1))))
B[i].append( int( input("B{}{}: ".format(i+1,j+1))))
C[i].append( A[i][j] + B[i][j])

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(A)
print(B)
print(C)
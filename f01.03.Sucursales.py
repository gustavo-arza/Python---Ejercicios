# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p224-225
#nombre: f01.03.Sucursales.py
print("-------------------------------------------------------")
print("Matriz3: SUCURSALES DE UNA EMPRESA.")
print("-------------------------------------------------------")

#Inicializar
MONTO = [] #Se crea una lista vac�a

#Entradas
print("Ingrese n�mero de sucursales y a�os: ")
N = int( input("N�mero de Sucursales: "))
M = int( input("N�mero de A�os: "))
for i in range(M):
MONTO.append( [] ) #Se Agrega la fila i
for j in range(N):
print("Ingrese ventas de la sucursal", j+1 , "en el a�o", i+1 )
venta = int( input())
MONTO[i].append(venta)

#Proceso
print("\nSUCURSAL CON M�S VENTAS: ")
print("-------------------------------------------------------")
MAX = 0
for j in range(N):
SUMA = 0
for i in range(M):
SUMA = SUMA + MONTO[i][j]
print ("N�mero de ventas de la Sucursal" , j+1, "es", SUMA)
if SUMA > MAX :
MAX = SUMA
SUC = j + 1 #Se incrementa j, por conteo desde 0
print("Sucursal que m�s vendi�: ", SUC)
print("\nPROMEDIO DE VENTAS DEL A�O: ")
print("-------------------------------------------------------")
MAX = 0
for i in range(M):
SUMA = 0
for j in range(N):
SUMA = SUMA + MONTO[i][j]
PROM = SUMA/N
print ("Promedio de ventas del a�o" , i+1, "es", PROM)
if PROM > MAX :
MAX = PROM
ANIO = i + 1 #Se incrementa i, por conteo desde 0
print("A�o con mayor promedio", ANIO)

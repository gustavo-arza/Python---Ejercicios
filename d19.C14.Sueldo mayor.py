# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p201
#nombre: d18.C14.Sueldo mayor.py
print("-------------------------------------------------------")
print("Complemento14: EMPLEADOS, SUELDO MAYOR.")
print("-------------------------------------------------------")
#Entradas
print ("Ingrese la cantidad de empleados:")
ce = int( input())

#Inicializar
i = 1
smayor = 0.0 #Inicializando Real

#Proceso
print("Ingrese los sueldos: ")
while i <= ce :
sueldo = float( input("Ingrese sueldo {0}: ".format(i)))
if sueldo > smayor :
smayor = sueldo
c = i
i = i + 1

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("El empleado numero ", c, "tiene el mayor sueldo que es:", smayor)

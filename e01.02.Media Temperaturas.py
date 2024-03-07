# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p212
#Nombre del Algoritmo: e01.02.Media Temperaturas.py
print("-------------------------------------------------------")
print("Vector2: MEDIA DE TEMPERATURAS.")
print("-------------------------------------------------------")
#Inicializar
Suma = 0
Media = 0.0
C = 0
Temp = [] #Lista vacía para almacenar temperaturas
#Entradas
print("Ingrese cantidad de Temperaturas: ")
N = int( input())
#Proceso
for i in range(N):
temperatura = float( input("Ingrese Temperatura {0}: ".format(i + 1) ))
Temp.append(temperatura)
Suma = Suma + Temp[i]
#Tambien se puede usar esta línea En lugar de la anterior:
#Suma = Suma + temperatura
Media = Suma / N #División real
#Contar cuantas temperaturas son mayor que la MEDIA
for tempElement in Temp: #La magia del FOR de PYTHON inicia.
if tempElement >= Media:
C = C + 1
print(tempElement)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("La media es ", Media)
print ("Total de temperaturas >= a la media es", C)

# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p160
#nombre: d01.03.Primos entre 1 y 1000.py
print("-------------------------------------------------------")
print("Ejercicio3: N�MEROS PRIMOS ENTRE 1 Y 1000.")
print("-------------------------------------------------------")
#Constantes
primero = 2
limite = 1000
#Inicializando
Cont = 0
#Proceso
for i in range(primero, limite):
primo = True
j = 2
while (i > j) and (primo == True):
if i%j == 0 :
#como no se consider� el N�mero(i) y el 1
#Si otro numero divide a i entonces ya tendr�a
# tres divisores. por lo tanto, no es primo
primo = False
break #Por tal motivo se rompe el ciclo
else:
j = j + 1
if primo == True :
print(i, "es primo.")
Cont = Cont + 1
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Entre", primero, "y" , limite, "hay", Cont, "n� primos")
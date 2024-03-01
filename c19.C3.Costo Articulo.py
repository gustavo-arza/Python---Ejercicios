# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p132
#nombre: c19.C3.Costo Articulo.py
print("-------------------------------------------------------")
print("Complemento3: COSTO DE ARTICULO.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese el Costo del artículo: ")
costo = float( input())
print("Ingrese la marca: ")
#m no necesita conversión ya que la entradas son Texto
m = input()
#Proceso
if costo >= 2000 and m == "NOSY" :
pa = costo*0.90
pt = pa*0.95
elif costo >= 200 and m != "NOSY" :
pt = costo*0.90
elif costo < 2000 and m == "NOSY" :
pa = costo*0.95
pt = pa + pa*0.20
elif costo < 2000 and m != "NOSY" :
pa = costo*1.20
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Usted pagara:", pt, "soles")

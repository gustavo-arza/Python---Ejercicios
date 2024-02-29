# -*- coding: utf-8 -*-
#extraido del libro Algoritmos resueltos con Python | p101-112
#nombre: c03.Condicion Multiple.py
#En Python no existe la selección multiple o SWITCH
#para simular la funcionalidad se usa un Diccionario
switcher = {
1: "Enero",
2: "Febrero",
3: "Marzo",
4: "Abril",
5: "Mayo",
6: "Junio",
7: "Julio",
8: "Agosto",
9: "Septiembre",
10: "Octubre",
11: "Noviembre",
12: "Diciembre"
}
argument = int( input("Ingrese número de mes: "))
#para acceder a los elementos se hace uso de la funcion .get del diccionario
# diccionario.get(AlgunArgumento, mensaje por Defecto)
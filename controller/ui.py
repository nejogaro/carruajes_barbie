__author__ = 'jedi'


import sys
sys.path.insert(0, '../model')
from cocheController import *
from coche import *

while(True):
    print("Bienvenido a la Tienda!")
    print("1 : ")
    print("2 Lista Coches disponibles: ")
    print("3 Lista Coches alquilados en este momento: ")
    print("4 Añade un nuevo coche: ")
    print("5 Conoce los ingresos totales entre 2 fechas: ")
    opcion = int(input("Selecciona una opcion: "))

    cocheController = CocheController()


    if(opcion == 1):
        cocheController.newAlquilerCoche()
    if(opcion == 2):
        cocheController.listCochesDisponibles()
    if(opcion == 3):
        cocheController.listCochesAlquilados()
    if(opcion == 4):
        cocheController.newCoche()



__author__ = 'jedi'

import sys
import os

sys.path.insert(0, '../model')
from coche import *
from dbController import *

import datetime

class CocheController:

    def newCoche(self):
        matricula = input("Matricula: ")
        marca = input("MArca: ")
        modelo = input("Modelo: ")
        preciodia = input("Preciodia: ")
        disponible = input("Disponible: ")
        cocheToInsert = coche(matricula, marca, modelo, preciodia, disponible)
        cocheToInsert.insertToDb();


    def listCochesDisponibles(self):
        print("Mostrando la lista de Coches Disponibles...")
        dbController = DbController()
        cocheList = dbController.getAllCoches()
        #cocheOrderedList = list()
        for cocheString in cocheList:
            matricula, marca, modelo, preciodia, disponible = cocheString.split(";")
            coche = coche(matricula, marca, modelo, preciodia, disponible)
            if coche.getDisponible() == 'SI':
                    cocheToList = coche
                    cocheList.append(cocheToList)
                    print(cocheToList)
            else:
                print("No hay coches disponibles")

    def listCochesAlquilados(self):
        print("Mostrando la lista de Coches Disponibles...")
        dbController = DbController()
        cocheList = dbController.getAllCoches()
        #cocheOrderedList = list()
        for cocheString in cocheList:
            matricula, marca, modelo, preciodia, disponible = cocheString.split(";")
            coche = coche(matricula, marca, modelo, preciodia, disponible)
            if coche.getDisponible() == 'NO':
                    cocheToList = coche
                    cocheList.append(cocheToList)
                    print("Lista de Coches Alquilados")
                    print(cocheToList)
            else:
                print("No hay coches disponibles")

#test = CocheController()
#test.listCochesDisponibles()

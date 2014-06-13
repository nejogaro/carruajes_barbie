__author__ = 'jedi'

import sys
import os
from controller.dbController import *

sys.path.insert(0, '../model')
from model.coche import *


class CocheController:



    def newAlquileresCoches(self):
        print("HOLA")

    def listCochesDisponibles(self):
        print("Mostrando la lista de Coches Disponibles...")
        dbController = DbController()
        cocheList = dbController.getAllCoches()
        #cocheOrderedList = list()
        for cocheString in cocheList:
            matricula, marca, modelo, preciodia, disponible = cocheString.split(";")
            coche = coche(matricula, marca, modelo, preciodia, disponible)
            #if coche.getDisponible() == 'SI':
            cocheToList = coche
            print(cocheToList)
            #else:
            #    print("No hay coches disponibles")

    def listCochesAlquilados(self):
        print("Mostrando la lista de Coches Alquilados...")
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


    def newCoche(self):
        matricula = input("Matricula: ")
        marca = input("MArca: ")
        modelo = input("Modelo: ")
        preciodia = input("Preciodia: ")
        disponible = input("Disponible: ")
        cocheToInsert = Coche(matricula, marca, modelo, preciodia, disponible)
        cocheToInsert.insertToDb();


    def ingresosTotales(self):
        matricula = input("Matricula: ")
        marca = input("MArca: ")
#test = CocheController()
#test.listCochesDisponibles()

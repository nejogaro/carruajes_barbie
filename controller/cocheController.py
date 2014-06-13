__author__ = 'jedi'

import sys
import os

from controller.dbController import *
from model.alquileres import *
from model.coche import *


class CocheController:


    def newAlquileresCoches(self):
        print("")


    def newCoche(self):
        matricula = input("Matricula: ")
        marca = input("MArca: ")
        modelo = input("Modelo: ")
        preciodia = input("Preciodia: ")
        disponible = input("Disponible: ")
        cocheToInsert = Coche(matricula, marca, modelo, preciodia, disponible)
        cocheToInsert.insertToDb();

    def ingresosTotales(self):
        alquileres = Alquileres()
        fechaini = input("Fecha 1: ")
        fechafin = input("Fecha 2: ")
        alquileres.getImporte(fechaini, fechafin)




#test = CocheController()
#test.listCochesDisponibles()
#test.newCoche()

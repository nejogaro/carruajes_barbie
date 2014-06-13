__author__ = 'jedi'

import sys

sys.path.insert(0, '../model')
from coche import *
from cocheController import *

class DbController:
    def __init__(self, pathToDbCoches="../database/coches.txt", pathToDbClientes="../database/coches.txt", pathToDbTransacciones="../database/coches.txt"):
        self.pathToDbCoches = pathToDbCoches
        self.pathToDbClientes = pathToDbClientes
        self.pathToDbTransacciones = pathToDbTransacciones

    def insertLineCoches(self, line):
        with open(self.pathToDbCoches, "a") as f:
            f.write(line + "\n")
            print("Coche añadido!")


    def pathToDbTransacciones(self, line):
        with open(self.pathToDbCoches, "a") as f:
            f.write(line + "\n")
            print("Coche añadido!")

    def getAllCoches(self):
        cochesList = list()
        with open(self.pathToDbCoches, "r") as f:
            for line in f:
                cochesList.append(line)
        print(cochesList)
        #return cochesList


    def getAllCochesAlquilados(self):
        cochesListAlquilados = list()
        with open(self.pathToDbCoches, "r") as f:
            for line in f:
                cochesListAlquilados.append(line)
        return cochesListAlquilados

test = DbController()
test.getAllCoches()
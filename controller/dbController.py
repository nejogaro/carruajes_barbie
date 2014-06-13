__author__ = 'jedi'
from controller.cocheController import *
import sys
import re

sys.path.insert(0, '../model')


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
                #cochesList.append(line)
                cochesList = line.split(';')
                if re.match(cochesList[4], 'SI'):
                    print("Matricula: ", cochesList[0], "Marca: ", cochesList[1])
        #return cochesList


    def getAllCochesAlquilados(self):
        cochesListAlquilados = list()
        with open(self.pathToDbCoches, "r") as f:
            for line in f:
                cochesListAlquilados.append(line)
        return cochesListAlquilados

#test = DbController()
#test.getAllCoches()
__author__ = 'jedi'

import sys
sys.path.insert(0, '../controller')
from dbController import *
from datetime import datetime


class Alquileres:
    def __init__(self, matricula, nif, fechaalquiler, fecharetorno, importe, compleatada):
        self.matricula = matricula
        self.nif = nif
        self.fechaalquiler = fechaalquiler
        self.fecharetorno = fecharetorno
        self.importe = importe
        self.completada = compleatada


    def getMatricula(self):
        return self.matricula
    def getNif(self):
        return self.nif
    def getFechaalquiler(self):
        return self.fechaalquiler
    def getFecharetorno(self):
        return self.fecharetorno
    def getImporte(self):
        return self.importe
    def getCompletada(self):
        return self.completada


    def totalIngresosPerioFechas(self):

        fecha_al = datetime.strptime(self.fechaalquiler, "%m/%d/%Y")
        fecha_re = datetime.strptime(self.fecharetorno, "%m/%d/%Y")
        total_dias = (abs((fecha_al-fecha_re).days))
        totalingresos = float(self.importe) * float(total_dias)
        print("El total de ingresos ha sido de : " + str(totalingresos))


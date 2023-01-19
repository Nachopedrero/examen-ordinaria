from ej1y2 import *

import random
import string


def generarlegion():
    legion = ["FL", "TF", "TK", "CT", "FN", "FO"]
    return random.choice(legion)

def generarnumero():
    numero = random.randint(1000,9999)
    return numero


def generarnombre():
    nombre = ""
    for i in range(0,4):
        nombre += random.choice(string.ascii_uppercase)
    return nombre

def crear_tropa():
    tropa = []
    for i in range(0,2000):
        legion = generarlegion()
        numero = generarnumero()
        nombre = generarnombre()
        rango = legion + str(numero)
        stormtruper = Stormtrooper(rango, nombre)
        tropa.append(stormtruper)
    return tropa





def agruparlegion(tropa):
    legiones = {}
    for i in tropa:
        legion = i[:2]
        if legion in legiones:
            legiones[legion].append(i)
        else:
            legiones[legion] = [i]
    return legiones



def agruparnumero(tropa):
    numeros = {}
    for i in tropa:
        numero = i[2:6]
        if numero in numeros:
            numeros[numero].append(i)
        else:
            numeros[numero] = [i]
    return numeros



def desertor(tropa):
    for i in tropa:
        if i == "FN-2187":
            print("El Stormtrooper FN-2187 está cargado")
            tropa.remove(i)
            print("El Stormtrooper FN-2187 ha sido eliminado")
        else:
            print("El Stormtrooper FN-2187 no está cargado")
    return tropa


def asignar_mision(tropa):
    mision = {}
    for i in tropa:
        if i[-3:] == "781":
            mision["asalto"] = i
        elif i[-3:] == "537":
            mision["exploracion"] = i
    return mision


def asignar_mision2(tropa):
    mision = {}
    for i in tropa:
        if i[:2] == "CT":
            mision["custodia"] = i
        elif i[:2] == "TF":
            mision["exterminacion"] = i
    return mision

# ejecutaria primero el crear y lo guardaria en una lista que luego paso a las siguientes funciones para que echen al desertor, los agrupe y los mande 
# a la mision

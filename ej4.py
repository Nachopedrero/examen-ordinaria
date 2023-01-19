from ej3 import *

def mochila_vacia(mochila):
    if len(mochila) == 0:
        return True  
    else:
        return False

def usarfuerza():
    mochila = Artefactosvaliosos.create_artefactosvaliosos()
    suma = 0
    for i in mochila:
        while i.nombre != "sable de luz" and mochila_vacia(mochila) == False:
            mochila.pop(0)
            suma += 1
        else:
            suma += 1
            print("sable de luz encontrado")
            mochila.pop(0)
            break
            
    print("se sacaron",suma,"objetos")

usarfuerza()

precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100

diccionario = dict(zip(precio, pesos))

def calcular_relacion(diccionario):
    relacion = []
    for precio, peso in diccionario.items():
        relacion.append(precio/peso)
    diccionario_relacion = dict(zip(relacion, diccionario.keys()))
    diccionario_relacion = dict(sorted(diccionario_relacion.items(), reverse=True))
    return diccionario_relacion

def agregar_a_mochila(diccionario_relacion):
    peso = 0
    mochila = []
    for relacion, precio in diccionario_relacion.items():
        if diccionario[precio] + peso <= peso_maximo:
            peso += diccionario[precio]
            mochila.append(precio)
    return mochila

print('¿Cuál es el valor máximo de los artículos que se pueden agregar a la mochila de manera que el peso no exceda el límite de peso W?')
print('El valor máximo es: ', sum(agregar_a_mochila(calcular_relacion(diccionario))))
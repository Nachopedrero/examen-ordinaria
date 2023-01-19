class Artefactosvaliosos(object):

    def __init__(self,nombre,peso,precio,fechacaducidad):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fechacaducidad = fechacaducidad
        print("creado con exito")


    def __str__(self):
        return "Artefactosvaliosos: {} {}".format(self.nombre, self.peso, self.precio, self.fechacaducidad)


    
    def create_artefactosvaliosos():
        mochila = []
        num = int(input("cuantos artefactos quieres crear:"))
        for i in range (1,num+1):
            nombre = input("Nombre del artefacto: ")
            peso = input("Peso del artefacto: ")
            precio = input("Precio del artefacto: ")
            fechacaducidad = input("Fecha de caducidad del artefacto: ")
            artefacto = Artefactosvaliosos(nombre, peso, precio, fechacaducidad)
            mochila.append(artefacto)
        return mochila
    
    def coctel(self):
        mochila = self.create_artefactosvaliosos()
        for i in range(len(mochila) - 1, 0, -1):
            control = False
            for j in range(i, 0, -1):
                if mochila[j].fechacaducidad < mochila[j - 1].fechacaducidad:
                    mochila[j], mochila[j - 1] = mochila[j - 1], mochila[j]
                    control = True
            for j in range(i):
                if mochila[j].fechacaducidad > mochila[j + 1].fechacaducidad:
                    mochila[j], mochila[j + 1] = mochila[j + 1], mochila[j]
                    control = True
            if control == False:
                break
        return mochila

    def modificarvalor(artefacto):
        artefacto.precio = input("Nuevo precio del artefacto: ")
        return artefacto

    def modificarpeso(artefacto):
        artefacto.peso = input("Nuevo peso del artefacto: ")
        return artefacto

    def modificarnombre(artefacto):
        artefacto.nombre = input("Nuevo nombre del artefacto: ")
        return artefacto      

    def modificarpeso(artefacto):
        artefacto.fechacaducidad = input("Nueva fecha de caducidad del artefacto: ")
        return artefacto
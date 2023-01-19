class Stormtrooper:

    def _init_(self, name, rank):
        if len(rank)== 6:
            self.name = name
            self.rank = rank
       
            print("creado con exito")
        else:
            print("error, el rango debe tener 6 caracteres")
            
        
    def __str__(self):
        return "Stormtrooper: {} {}".format(self.name, self.rank)
    

    def calificacion(self):
        codigolegion = self.rank[:2]
        codigocoohorte = self.rank[2]
        codigosiglo = self.rank[3]
        codigoescuadra = self.rank[4]
        numerotrooper = self.rank[5]
        print("codigo legion", codigolegion)
        print("codigo coohorte", codigocoohorte)
        print("codigo siglo", codigosiglo)
        print("codigo escuadra", codigoescuadra)
        print("numero trooper", numerotrooper)

    def create_stormtroopers(self):
        stormtroopers = []
        numero = int(input("Numero de stormtroopers: "))
        for i in range (1,numero+1):
            name = input("Nombre del stormtrooper: ")
            rank = input("Rango del stormtrooper: ")
            stormtrooper = Stormtrooper(name, rank)
            stormtroopers.append(stormtrooper)
        return stormtroopers
        
    def clasificar_stormtroopers(self):
        stormtroopers = self.create_stormtroopers()
        for i in stormtroopers:
            print('\n')
            print(i)
            i.calificacion()
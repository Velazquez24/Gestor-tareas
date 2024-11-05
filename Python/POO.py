#//Metodos y atributos//

class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ':', sep='')    
        print('Fuerza:', self.fuerza)    
        print('Inteligencia', ':', self.inteligencia)    
        print('Defensa', ':', self.defensa)    
        print('Vida', ':', self.vida)  

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, 'Ha muerto')    

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, 'ha realizado', damage, 'hp a', enemigo.nombre)
        if enemigo.esta_vivo():
            print('la vida del enemigo es', enemigo.vida)
        else:
            enemigo.morir()

        
#//Herencias//

class guerrero(personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input('Elija un arma (1)Espada, (2)Arco'))
        if opcion == 1:
            self.espada == 8
        elif opcion == 2:
            self.espada == 5
        else:
            print('Elija bien pendeja')    

    def atributos(self):
        super().atributos()
        print('Espada:', self.espada)

    def damage(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa


class mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print('libro', self.libro)

    def damage(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
        

#//Poliformismo//
    
    
personaje_1 = personaje('Mancer', 50, 40, 30, 100)
personaje_2 = personaje('random', 50, 40, 30, 100)


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print('turno', turno)
        print('>>>Accion de',jugador_1.nombre, ':', sep='')
        jugador_1.atacar(jugador_2)
        print('>>>Accion de',jugador_2.nombre, ':', sep='')
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print('ha ganado', jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print('ha ganado', jugador_2.nombre)
    else:
        print('todos muertos')
combate(personaje_1, personaje_2)

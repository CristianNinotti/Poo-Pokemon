import random

class PokemonSimulacion:
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def vida(self):
        return self._vida

    def atacar1(self):
        cantidad = random.randint(10, 25)
        return cantidad
    
    def atacar2(self):
        cantidad = random.randint(20, 35)
        return cantidad

    def perder_vida(self, ataque):
        self._vida -= ataque

    def __str__(self):
        return f'{self.nombre} (Vida: {self.vida})'

def pausa():
    print("---------------------------------------------------------")
    input("APRETA CUALQUIERA TECLA PARA SEGUIR JUGANDO\n")
    

def batalla():
    pokemon1 = PokemonSimulacion("Charmander", 100)
    pokemon2 = PokemonSimulacion("Pikachu", 100)

    while pokemon1.vida > 0 and pokemon2.vida > 0:
        print("Vida de los Pokemones:\n")
        print(pokemon1)
        print(pokemon2)
        pausa()
        
        option = input("Elige ataque 1 o 2\n")
        if option == "1":
            print(f"Turno de ataque para {pokemon1.nombre}")
            print("Eligió ataque 1\n")
            ataque = pokemon1.atacar1()
            print(f"Valor de ataque: {ataque}\n")
            pokemon2.perder_vida(ataque)
        else:
            print(f"Turno de ataque para {pokemon1.nombre}")
            print("Eligió ataque 2\n")
            ataque = pokemon1.atacar2()
            print(f"Valor de ataque: {ataque}\n")
            pokemon2.perder_vida(ataque)
        
        pausa()
        if pokemon2.vida <= 0:
            print(f"{pokemon2.nombre} ha sido derrotado.\n")
            break
        
        print("Vida de los Pokemones:\n")
        print(pokemon1)
        print(pokemon2)
        pausa()
        
        #Jugador 2
        option = random.choice(["1", "2"])
        if option == "1":
            print(f"Turno de ataque para {pokemon2.nombre}")
            print("Eligió ataque 1\n")
            ataque = pokemon2.atacar1()
            print(f"Valor de ataque: {ataque}\n")
            pokemon1.perder_vida(ataque)
        else:
            print(f"Turno de ataque para {pokemon2.nombre}")
            print("Eligió ataque 2\n")
            ataque = pokemon2.atacar2()
            print(f"Valor de ataque: {ataque}\n")
            pokemon1.perder_vida(ataque)
        
        pausa()
        if pokemon1.vida <= 0:
            print(f"{pokemon1.nombre} ha sido derrotado.\n")
            break

    print("\n\nFIN DEL JUEGO")



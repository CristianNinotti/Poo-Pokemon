from entrenador import *
from mochila import *
from objeto import *
from pokemon import *
from tipopokemon import *
import random

## Tipo(str) - Tipo-Pokemon-Debilidad(str) -Modificador(float)
pokemonAgua = TipoPokemon('Agua', 'Hierba', 0.5)
pokemonFuego = TipoPokemon('Fuego', 'Agua', 0.5)
pokemonHierba = TipoPokemon('Hierba', 'Fuego', 0.5)
pokemonElectrico = TipoPokemon('Electrico', 'Roca', 0.5)
pokemonRoca = TipoPokemon('Roca', 'Agua | Hielo', 0.3)
pokemonBicho = TipoPokemon('Bicho', 'Fuego | Volador', 0.4)
pokemonVolador = TipoPokemon('Volador', 'Electrico | Roca', 0.5)
pokemonHielo = TipoPokemon('Hielo', 'Fuego', 0.5)
pokemonTierra = TipoPokemon('Tierra', 'Bicho | Hierba | Agua', 0.3)
pokemonAcero = TipoPokemon('Acero', 'Electrico | Hielo', 0.5)
pokemonDragon = TipoPokemon('Dragon','Electrico | Hielo', 0.5)
pokemonFantasma = TipoPokemon('Fantasma', 'Psiquico', 0.6)
pokemonPsiquico = TipoPokemon('Psiquico', 'Fantasma', 0.6)
pokemonLucha = TipoPokemon('Lucha', 'Normal', 0.8)
pokemonNormal = TipoPokemon('Normal', 'Psiquico | Fantasma | Acero | Dragon | Tierra | Hielo | Volador | Bicho | Roca | Electrico | Hierba | Fuego | Agua', 1)


## Nombre(str) - Puntos de Salud(int) - Nivel(int) - Nivel minimo de evolucion(int)
Squartle = Pokemon('Squartle', 50, random.randint(5,25), 16, pokemonAgua, "Wartortle")
Charmander = Pokemon('Charmander', 50, random.randint(5,25), 16, pokemonFuego, "Charmeleon")
Bulbasaur = Pokemon('Bulbasaur', 50, random.randint(5,25), 16, pokemonHierba, "Ivysaur")
Pikachu = Pokemon('Pikachu', 80, random.randint(5,25), 16, pokemonElectrico, "Raichu")
Geodude = Pokemon('Geodude', 160, random.randint(5,25), 16, pokemonRoca, "Graveler")
Caterpie = Pokemon('Caterpie', 90, random.randint(3,10), 7, pokemonBicho, "Metapod")
Pidgey = Pokemon('Pidgey', 50, random.randint(8,20), 12, pokemonVolador, "Pidgeotto")
Jynx = Pokemon('Jynx',50, random.randint(5,25), 16, pokemonHielo, "MegaJynx")
Cubone = Pokemon('Cubone', 120, random.randint(5,25), 16, pokemonTierra, "Marowak")
Aerodactyl = Pokemon('Aerodactyl', 225, random.randint(5,25), 16, pokemonAcero, "MegaAerodactyl")
Dratini = Pokemon('Dratini', 100,random.randint(5,25), 16, pokemonDragon, "Dragonair")
Gastly = Pokemon('Gastly', 75, random.randint(5,25), 16, pokemonFantasma, "Haunter")
Abra = Pokemon('Abra', 75, random.randint(5,25), 16, pokemonPsiquico, "Kadabra")
Mankey = Pokemon('Mankey', 210, random.randint(5,25), 16, pokemonLucha, "Prime")
Clefairy = Pokemon('Clefairy', 210, random.randint(5,25), 16, pokemonNormal, "Cleaffe")

piedraEvolutiva = Objeto("Piedra Evolutiva")
mochila = Mochila()

lista_pokemones = [Squartle,Charmander,Bulbasaur,Pikachu,Geodude,Caterpie,Pidgey,Jynx,Cubone,Aerodactyl,Dratini,Gastly,Abra,Mankey,Clefairy]

lista_entrenadores = []

pokemones_aleatorios=[]
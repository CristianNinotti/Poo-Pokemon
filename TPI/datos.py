from entrenador import *
from mochila import *
from objeto import *
from pokemon import *
from tipopokemon import *

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
Squartle = Pokemon('Squartle', 50, 1, 16, pokemonAgua)
Charmander = Pokemon('Charmander', 50, 1, 16, pokemonFuego)
Bulbasaur = Pokemon('Bulbasaur', 50, 1, 16, pokemonHierba)
Pikachu = Pokemon('Pikachu', 80, 1, 16, pokemonElectrico)
Geodude = Pokemon('Geodude', 160, 17, 16, pokemonRoca)
Caterpie = Pokemon('Caterpie', 90, 8, 7, pokemonBicho)
Pidgey = Pokemon('Pidgey', 50, 5, 12, pokemonVolador)
Jynx = Pokemon('Jynx',50, 20, 16, pokemonHielo)
Cubone = Pokemon('Cubone', 120, 6, 16, pokemonTierra)
Aerodactyl = Pokemon('Aerodactyl', 225, 25, 16, pokemonAcero)
Dratini = Pokemon('Dratini', 100, 8, 16, pokemonDragon)
Gastly = Pokemon('Gastly', 75, 3, 16, pokemonFantasma)
Abra = Pokemon('Abra', 75, 3, 16, pokemonPsiquico)
Mankey = Pokemon('Mankey', 210, 21, 16, pokemonLucha)
Clefairy = Pokemon('Clefairy', 210, 21, 16, pokemonNormal)

lista_pokemones = [Squartle,Charmander,Bulbasaur,Pikachu,Geodude,Caterpie,Pidgey,Jynx,Cubone,Aerodactyl,Dratini,Gastly,Abra,Mankey,Clefairy]

## for pokemon in lista_pokemones:
##   print(pokemon) 




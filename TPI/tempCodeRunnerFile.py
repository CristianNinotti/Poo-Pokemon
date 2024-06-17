from entrenador import *
from mochila import *
from objeto import *
from pokemon import *
from tipopokemon import *


## Nombre(str) - Puntos de Salud(int) - Nivel(int) - Nivel minimo de evolucion(int)
pokemonAgua1 = Pokemon('Squartle', 50, 1, 16)
## Tipo(str) - Tipo-Pokemon-Debilidad(str) -Modificador(float)
pokemonAgua1 = TipoPokemon('Agua', 'Hierba', 0.5)
print(pokemonAgua1)



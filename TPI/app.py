from entrenador import Entrenador
from objeto import Objeto
from mochila import Mochila
from datos import lista_pokemones
from pokemon import Pokemon
from tipopokemon import TipoPokemon

def mostrar_menu():
    print("1. Mostrar Pokémon disponibles")
    print("2. Capturar Pokémon")
    print("3. Liberar Pokémon")
    print("4. Evolucionar Pokémon")
    print("5. Ver Detalles del Entrenador")
    print("6. Salir")

def mostrar_pokemon_disponibles():
    print("Pokémon disponibles:")
    for i, pokemon in enumerate(lista_pokemones):
        print(f"{i + 1}. {pokemon.nombre} (Nivel: {pokemon.nivel}, Salud: {pokemon.puntos_salud} Tipo:{TipoPokemon}) ")

def main():
    print("Bienvenido a la aplicación de Pokémon")
    ciudad = input("Ingrese la ciudad del entrenador: ")
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")

    entrenador = Entrenador(ciudad, nombre_entrenador)
    mochila = Mochila()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_pokemon_disponibles()

        elif opcion == "2":
            mostrar_pokemon_disponibles()
            indice = int(input("Seleccione el número del Pokémon que desea capturar: ")) - 1
            if 0 <= indice < len(lista_pokemones):
                pokemon = lista_pokemones[indice]
                entrenador.capturar_pokemon(pokemon)
                print(f"Pokémon {pokemon.nombre} capturado!")
            else:
                print("Selección no válida.")

        elif opcion == "3":
            nombre_pokemon = input("Ingrese el nombre del Pokémon a liberar: ")
            pokemon_a_liberar = next((p for p in entrenador.Entrenador_lista_pokemones if p.nombre == nombre_pokemon), None)
            if pokemon_a_liberar:
                entrenador.liberar_pokemon(pokemon_a_liberar)
                print(f"Pokémon {nombre_pokemon} liberado!")
            else:
                print(f"No se encontró el Pokémon {nombre_pokemon}")

        elif opcion == "4":
            nombre_pokemon = input("Ingrese el nombre del Pokémon a evolucionar: ")
            pokemon_a_evolucionar = next((p for p in entrenador.Entrenador_lista_pokemones if p.nombre == nombre_pokemon), None)
            if pokemon_a_evolucionar:
                objeto = Objeto("Piedra Evolutiva")
                mochila.add_objeto(objeto)
                try:
                    mensaje = pokemon_a_evolucionar.evolucionar(objeto)
                    print(mensaje)
                except Exception as e:
                    print(e)
            else:
                print(f"No se encontró el Pokémon {nombre_pokemon}")

        elif opcion == "5":
            print(entrenador)

        elif opcion == "6":
            print("Saliendo de la aplicación...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if _name_ == "_main_":
    main()
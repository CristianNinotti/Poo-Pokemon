from entrenador import Entrenador
from mochila import Mochila
from datos import *
from simulacion import *

def menu():
    print("\n1. Sección entrenadores")
    print("2. Sección pokemon")
    print("3. Simulación de batalla")
    print("4. Salir del programa")

def sub_menu_entrenadores():
    print("\n1. Crear nuevo entrenador")
    print("2. Mostrar lista de entrenadores")
    print("3. Mostrar pokemones capturados")
    print("4. Cambiar de entrenador")
    print("5. Comprar piedra de evolución")
    print("6. Salir al menú principal")

def sub_menu_pokemones():
    print("\n1. Capturar pokemon")
    print("2. Liberar pokemon")
    print("3. Evolucionar pokemon")
    print("4. Salir al menú principal")

def mostrar_pokemon_disponibles():
    # Seleccionamos 3 pokemones aleatorios de la lista enumerada
    pokemones_aleatorios = random.sample(lista_pokemones, 3)

    print("\nEntre los arbustos puedes divisar algunos Pokemones.. ¡Rápido! ¡Lánzales una pokebola!")
    for indice, pokemon in enumerate(pokemones_aleatorios, 1):
        print(f"""\n{indice} - {pokemon.nombre}
     Nivel: {pokemon.nivel}
     {pokemon.tipo_pokemon}""")
    return pokemones_aleatorios

def mostrar_pokemones_atrapados():
    if len(entrenador_activo.lista_pokemones) == 0:
        print(f"\n¡Parece que {entrenador_activo.nombre} no ha atrapado ningún Pokemon aún!")
    else:
        print("\nLista de pokemones capturados:")
        for i, pokemon in enumerate(entrenador_activo.lista_pokemones, 1):
            print(f"\n{i} - {pokemon}")

def mostrar_lista_entrenadores():
    for i, entrenador in enumerate(lista_entrenadores, 1):
        print(f"\n{i} - {entrenador}")

entrenador_activo = False

print("""
===============================
 BIENVENIDOS AL MUNDO POKEMON!
===============================""")

while True:
    print("\n------- MENU PRINCIPAL -------")
    menu()
    opcion = input("\nSeleccione una opcción: ")

    if opcion == "1":
        print("\n---- SUBMENU ENTRENADORES ----")
        while True:
            sub_menu_entrenadores()
            opcion = input("\nSeleccione una opcción: ")
            if opcion == "1":
                print("\nNUEVO ENTRENADOR:")
                nombre = input("Ingrese el NOMBRE del entrenador: ")
                ciudad = input("Ingrese la CIUDAD del entrenador: ")
                mochila = Mochila()
                entrenador_activo = Entrenador(ciudad.title(), nombre.title(), mochila)
                if str(nombre.title()) == str(entrenador_activo.nombre):
                    lista_entrenadores.append(entrenador_activo)
                    print(f"\n¡{entrenador_activo.nombre} proveniente de {entrenador_activo.ciudad} es ahora un entrenador Pokemon!")
                else:
                    print(entrenador_activo.nombre)

            elif opcion == "2":
                if len(lista_entrenadores) > 0:
                    mostrar_lista_entrenadores()
                else:
                    print("\n¡No existen entrenadores disponibles para realizar esa tarea!")
            
            elif opcion =="3":
                if len(lista_entrenadores) > 0:
                    mostrar_pokemones_atrapados()
                else:
                    print("\n¡No existen entrenadores disponibles para realizar esa tarea!")

            elif opcion == "4":
                if len(lista_entrenadores) > 0:
                    if len(lista_entrenadores) == 1:
                        print(f"\n¡El único entrenador disponible es {entrenador_activo.nombre} por el momento!")
                    else:
                        mostrar_lista_entrenadores()
                        seleccion = int(input("\nIntroduzca el número del entrenador deseado: "))
                        if 0 < seleccion <= len(lista_entrenadores): 
                            entrenador_activo = lista_entrenadores[seleccion-1]
                            print(f"\n¡Ahora recorres el mundo con {entrenador_activo.nombre}!")
                        else:
                            print("\nSelección no válida! Intente nuevamente..")
                else:
                    print("\n¡No existen entrenadores disponibles para realizar esa tarea!")

            elif opcion == "5":
                if len(lista_entrenadores) > 0:
                    if len(entrenador_activo.mochila.lista_objetos) < entrenador_activo.mochila.capacidad:
                        entrenador_activo.mochila.add_objeto(piedraEvolutiva)
                        print("\n¡Piedra de Evolución comprada y añadida a la mochila!")
                    else:
                        print("\n¡Mochila llena, no se pueden comprar más objetos!")
                else:
                    print("\n¡No existen entrenadores disponibles para realizar esa tarea!")                

            elif opcion == "6":
                break
            
            else:
                print("\nSelección no válida! Intente nuevamente..")
    
    elif opcion == "2":
        print("\n----- SUBMENU POKEMONES -----")
        while True:
            if not entrenador_activo:
                print("\n¡Necesitas ser un entrenador Pokemon para ingresar a esta sección!")
                break
            sub_menu_pokemones()
            opcion = input("\nSeleccione una opcción: ")

            if opcion == "1":
                pokemones_aleatorios = mostrar_pokemon_disponibles()
                indice = int(input("\nSelecciona el número de Pokemon que deseas capturar: "))
    
                if 1 <= indice <= len(pokemones_aleatorios):
                    pokemon = pokemones_aleatorios[indice - 1]
                    entrenador_activo.capturar_pokemon(pokemon)
                    #Captura de pokemon
                    print(f"\n¡Pokémon {pokemon.nombre} capturado!")
                else:
                    print("\nSelección no válida! Intente nuevamente..")

            elif opcion == "2":
                mostrar_pokemones_atrapados()
                indice = int(input("\nSeleccione el número del Pokémon que deseas liberar: "))
                if 1 <= indice <= len(entrenador_activo.lista_pokemones):
                    pokemon = entrenador_activo.lista_pokemones[indice - 1]
                    entrenador_activo.liberar_pokemon(pokemon)
                    print(f"\n¡Pokémon {pokemon.nombre} liberado!")
                else:
                    print("\nSelección no válida! Intente nuevamente..")

            elif opcion == "3":
                mostrar_pokemones_atrapados()
                if len(entrenador_activo.lista_pokemones):
                    indice = int(input("\nSeleccione el número del Pokémon que desea evolucionar: "))
                    if 1 <= indice <= len(entrenador_activo.lista_pokemones):
                        pokemon = entrenador_activo.lista_pokemones[indice - 1]
                        pokemon_antes_evol = pokemon.nombre
                        if entrenador_activo.evolucionar_pokemon(pokemon, entrenador_activo.mochila, piedraEvolutiva):
                            print(f"\n{pokemon_antes_evol} ha evolucionado a {pokemon.nombre}!")
                        elif pokemon.nombre == pokemon.nombre_evolucion:
                            print("El pokemón no puede evolucionar porque ya está evolucionado") 
                        else:
                            print(f"\n¡No se cumplen los requisitos para que {pokemon.nombre} evolucione!")
                    else:
                        print("\nSelección no válida! Intente nuevamente..")

            elif opcion == "4":
                break
            
            else:
                print("\nSelección no válida! Intente nuevamente..")

    elif opcion == "3":
        batalla()
    
    elif opcion == "4":
        break
    
    else:
        print("\nSelección no válida! Intente nuevamente..")              
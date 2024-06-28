from mochila import Mochila
from pokemon import Pokemon
from objeto import Objeto

class Entrenador():

    __lista_nombres = []

    def __init__(self,ciudad:str,nombre:str, mochila:Mochila) -> None:
        self.__ciudad = ciudad
        self.__nombre = Entrenador.lista_nombres(nombre)
        self.__lista_pokemones = []
        self.__mochila = mochila

    ## Unique Nombre ##
    @classmethod
    def lista_nombres(cls,nombre)->str:
        if (nombre in cls.__lista_nombres):
            return f"\n¡Ya hay un entrenador llamado {nombre}!"
        cls.__lista_nombres.append(nombre)
        return nombre

    ## Getter Lista de Pokemones ##
    @property
    def lista_pokemones(self):
        return  self.__lista_pokemones

    ## Getter  Nombre{readonly} ##
    @property
    def nombre(self)->list:
        return self.__nombre    

    ## Getter - Ciudad ##
    @property
    def ciudad(self)->str:
        return self.__ciudad
    
    ## Setter - Ciudad ##
    @ciudad.setter
    def ciudad(self,new_ciudad):
        self.__ciudad = new_ciudad

    ## Getter Mochila ##
    @property
    def mochila(self) -> Mochila:
        return self.__mochila    

    ## Método Evolucionar Pokemon ##
    def evolucionar_pokemon(self, pokemon: 'Pokemon', mochila: Mochila, objeto: Objeto=None) -> bool:
        #Validacion para no evolucionar un pokemon ya evolucionado
        if pokemon.puede_evolucionar and pokemon.nombre != pokemon.nombre_evolucion: 
            pokemon.evolucionar()
            return True
         #Validacion para no evolucionar un pokemon ya evolucionado
        elif objeto in mochila.lista_objetos and pokemon.nombre != pokemon.nombre_evolucion:
            pokemon.evolucionar()
            mochila.remove_objeto(objeto)
            return True
        return False
            
    ## Método Capturar Pokemon ## 
    def capturar_pokemon(self,pokemon:Pokemon)->Pokemon:
        self.__lista_pokemones.append(pokemon)

    ## Método Liberar Pokemon ## 
    def liberar_pokemon(self,pokemon:Pokemon)->Pokemon:
        self.__lista_pokemones.remove(pokemon)

    ## Str ## 
    def __str__(self) -> str:
        return f'''Nombre: {self.nombre} 
    Ciudad: {self.ciudad} 
    Pokemones: {" - ".join(str(pokemon.nombre) for pokemon in self.__lista_pokemones)}
    Cantidad de objetos evolutivos: {len(self.mochila.lista_objetos)}'''
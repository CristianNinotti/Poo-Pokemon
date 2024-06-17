from mochila import Mochila
from pokemon import Pokemon

class Entrenador():
    __lista_nombres = []
    def __init__(self,ciudad:str,nombre:str) -> None:
        self.__ciudad = ciudad
        self.__nombre = Entrenador.__lista_nombres(nombre)
        self.__lista_pokemones = []

    ## Unique Nombre ##
    @classmethod
    def __lista_nombres(cls,nombre)->str:
        if (nombre in cls.__lista_nombres):
            raise Exception ("Ese nombre ya existe por otro jugador")
        cls.__lista_nombres.append(nombre)      ## Controlar append sin color
        return nombre
    
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


    ## Add
    def capturar_pokemon(self,pokemon:Pokemon)->Pokemon:
        self.__lista_pokemones.append(pokemon)

    ##Remove
    def liberar_pokemon(self,pokemon:Pokemon)->Pokemon:
        self.__lista_pokemones.remove(pokemon)    

    def evolucionar_pokemon(self,pokemon:Pokemon)->Pokemon:
          pokemon.evolucionar()
          return pokemon                 ### VER ###
     
    def __str__(self) -> str:
        return f'''
        Nombre del entrenador: {self.nombre}
        Ciudad: {self.ciudad}
        Pokemones: {self.__lista_pokemones}'''





from tipopokemon import TipoPokemon

class TipoPokemon():
    def __init__(self, tipo:str, tipo_pokemon_debilidad:TipoPokemon, modificador:float) -> None:
        self.__tipo = tipo
        self.__tipo_pokemon_debilidad = tipo_pokemon_debilidad
        self.__modificador = modificador

    ## Getter Tipo ##
    @property
    def tipo(self)->str:
        return self.__tipo

    ## Setter Tipo ##
    @tipo.setter
    def tipo(self,new_tipo):
        self.__tipo = new_tipo

    ## Getter Tipo_Pokemon_Debilidad ##
    @property
    def tipo_pokemon_debilidad(self)->TipoPokemon:
        return self.__tipo_pokemon_debilidad

    ## Setter Tipo_Pokemon_Debilidad ##
    @tipo_pokemon_debilidad.setter
    def tipo_pokemon_debilidad(self,new_tipo_pokemon_debilidad):
        self.__tipo_pokemon_debilidad = new_tipo_pokemon_debilidad

    ## Get Modificador ##
    @property
    def modificador(self)->float:
        return self.__modificador

    ## Set Modificador ##
    @modificador.setter
    def modificador(self,new_modificador):
        self.__modificador = new_modificador

    ## Str ##
    def __str__(self) -> str:
        return f'{self.tipo}, {self.tipo_pokemon_debilidad}, {self.modificador}'                    

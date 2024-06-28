from tipopokemon import TipoPokemon

class Pokemon():

    __nro_incremental = int(0)

    def __init__(self, nombre:str, puntos_salud:int, nivel:int, nivel_min_evolucion:int, tipo_pokemon:TipoPokemon, nombre_evolucion:str) -> None:
        self.__nombre:str = nombre
        self.__nro:int = Pokemon.nro_incremental()
        self.__puntos_salud:int = puntos_salud
        self.__nivel:int = nivel
        self.__nivel_min_evolucion:int = nivel_min_evolucion
        self.__tipo_pokemon:TipoPokemon = tipo_pokemon
        self.__nombre_evolucion:str = nombre_evolucion

    ## Auto incremental nro ##
    @classmethod
    def nro_incremental(cls)->int:
        cls.__nro_incremental += 1
        return cls.__nro_incremental
    
    ## Getter Tipo_Pokemon ##
    @property
    def tipo_pokemon(self)->TipoPokemon:
        return self.__tipo_pokemon
    
    ## Setter Tipo_Pokemon ##
    @tipo_pokemon.setter
    def tipo_pokemon(self,new_tipo_pokemon):
        self.__tipo_pokemon = new_tipo_pokemon

    ## Getter Nro ##
    @property
    def nro(self)->int:
        return self.__nro
    
    ## Getter Nombre ##
    @property
    def nombre(self)->str:
        return self.__nombre
    
    ## Setter Nombre ##
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

    ## Getter Puntos de salud ##
    @property
    def puntos_salud(self)->int:
        return self.__puntos_salud

    ## Setter Puntos de salud
    @puntos_salud.setter
    def puntos_salud(self,new_puntos_salud):
        self.__puntos_salud = new_puntos_salud

    ## Getter Nivel ##
    @property
    def nivel(self)->int:
        return self.__nivel

    ## Setter Nivel ##
    @nivel.setter
    def nivel(self,new_nivel):
        self.__nivel = new_nivel

    ## Getter Nivel_Min_Evolucion ##
    @property
    def nivel_min_evolucion(self)->int:
        return self.__nivel_min_evolucion

    ## Setter Nivel_Min_Evolucion ##
    @nivel_min_evolucion.setter
    def nivel_min_evolucion(self,new_nivel_min_evolucion):
        self.__nivel_min_evolucion = new_nivel_min_evolucion
        
    ## Getter Nombre de Evolución ##
    @property
    def nombre_evolucion(self):
        return self.__nombre_evolucion

    ## Calculado Getter - Puede Evolucionar ##
    @property
    def puede_evolucionar(self):
        if int(self.nivel) >= int(self.nivel_min_evolucion):
            return True
        return False
    
    ## Método evolucionar ##
    def evolucionar(self):        
        self.nombre = self.nombre_evolucion 
        self.puntos_salud += 5
        self.nivel_min_evolucion += 15
        
    ## Str ##
    def __str__(self) -> str:
        return f"""{self.nombre}:
     Nro: {self.nro}
     Nivel: {self.nivel}
     HP: {self.puntos_salud}
     Nivel mínimo para evolucionar: {self.nivel_min_evolucion}
     {self.tipo_pokemon}"""
    
    
        
        


    

    

   








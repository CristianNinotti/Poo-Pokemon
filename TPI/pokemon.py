from mochila import Mochila
from tipopokemon import TipoPokemon

class Pokemon():
    __nro_incremental = int(0)
    def __init__(self, nombre:str, puntos_salud:int, nivel:int, nivel_min_evolucion:int, tipo_pokemon:TipoPokemon) -> None:
        self.__nombre = nombre
        self.__nro = Pokemon.nro_incremental()
        self.__puntos_salud = puntos_salud
        self.__nivel = nivel
        self.__nivel_min_evolucion = nivel_min_evolucion
        self.__tipo_pokemon = tipo_pokemon

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

    ## Calculado Getter - Puede Evolucionar ##
    @property
    def puede_evolucionar(self)->bool:
        if (self.__nivel >= 16):
           ## f'El pokemon evolucionó'
            return True
        ## f'El pokemon necesita nivel para evolucionar'
        return False
    
    def evolucionar(self, objeto):
        if (objeto not in Mochila.lista_objetos and Pokemon.puede_evolucionar):
            Mochila.remove_objeto(objeto)
            return  f'Evolucionando ....' 
        raise Exception ("No tienes ningun objeto o no cumple con el nivel necesario")
           
    def __str__(self) -> str:
        return f"""
        Nombre Pokemon: {self.nombre}
        Nro: {self.nro}
        HP: {self.puntos_salud}
        Nivel: {self.nivel}
        Puede evolucionar: {self.puede_evolucionar}
        Nivel minimo para evolucionar: {self.nivel_min_evolucion} {self.tipo_pokemon}"""
        
        


    

    

   








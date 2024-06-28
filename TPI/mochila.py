from objeto import Objeto

class Mochila():

    def __init__(self) -> None:
        # Capacidad mochila 3 maximo = Que UML
        self.__capacidad:int = 3                 
        self.__lista_objetos:list = []

    ## Getter Capacidad ##
    @property
    def capacidad(self) -> int:
        return self.__capacidad

    ## Setter Capacidad ##
    @capacidad.setter
    def capacidad(self, new_capacidad):
        self.__capacidad = new_capacidad

    ## Getter Lista de Objetos ##
    @property
    def lista_objetos(self) -> list:
        return self.__lista_objetos    

    # Métdodo Agregar Objeto #
    def add_objeto(self, objeto: Objeto) -> None:
        if len(self.lista_objetos) >= self.capacidad:
            raise Exception("Capacidad máxima de la mochila alcanzada")
        self.__lista_objetos.append(objeto)

    # Métdodo Eliminar Objeto #
    def remove_objeto(self, objeto: Objeto) -> None:
        if objeto in self.lista_objetos:
            self.__lista_objetos.remove(objeto)
        else:
            raise Exception("El objeto no está en la mochila")

    ## Str ##
    def __str__(self) -> str:
        return f'Capacidad de objetos en mochila: {self.capacidad} Objetos: {self.__lista_objetos}'
    
  
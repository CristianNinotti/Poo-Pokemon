from objeto import Objeto

class Mochila():
    def __init__(self) -> None:
        self.__capacidad = 2
        self.__lista_objetos = []

    @property
    def capacidad(self)->int:
        return self.__capacidad

    @capacidad.setter
    def capacidad(self,new_capacidad):
        self.__capacidad = new_capacidad

    @property
    def lista_objetos(self)->list:
        return self.__lista_objetos    

    def add_objeto(self,objeto:Objeto)->Objeto:
        if len(self.lista_objetos) > 2:
            raise Exception ("Limite de objetos en mochila alcanzado")
        self.__lista_objetos.append(objeto)
        return objeto

    def remove_objeto(self,objeto:Objeto)->Objeto:
        if len(self.lista_objetos) == 0:
            raise Exception ("No tiene objetos en la mochila")
        self.__lista_objetos.remove(objeto)    

    def __str__(self) -> str:
        return f'Capacidad de objetos en mochila: {self.capacidad} Objetos: {self.__lista_objetos}' 
    
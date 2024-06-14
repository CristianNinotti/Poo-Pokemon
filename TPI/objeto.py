class Objeto():
    def __init__(self, tipo:str) -> None:
        self.__tipo = tipo

    @property
    def tipo(self)->str:
        return self.__tipo

    @tipo.setter
    def tipo(self,new_tipo):
        self.__tipo = new_tipo

    def dar_objeto(self, objeto)->None:
        return objeto

    def __str__(self) -> str:
        return f'Tipo objeto: {self.tipo}'       
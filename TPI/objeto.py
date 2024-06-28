class Objeto():
    def __init__(self, tipo:str) -> None:
        self.__tipo:str = tipo

    ## Getter Tipo ##
    @property
    def tipo(self) -> str:
        return self.__tipo

    ## Setter Tipo ##
    @tipo.setter
    def tipo(self,new_tipo):
        self.__tipo = new_tipo

    ## Str ##
    def __str__(self) -> str:
        return f'Tipo objeto: {self.tipo}'
    

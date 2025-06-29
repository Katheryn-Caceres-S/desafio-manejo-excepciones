from error import DimensionError




class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self._ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        #si el ancho es mayor a 1  o menor que el maximo 
        if ancho > self.MAX  or ancho < 1:
             raise DimensionError("ancho es menor a 1 o mayor al maximo porfavor revisar",ancho, self.MAX)
        else:
            self.__ancho = ancho
        

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if 1 <= alto <= self.MAX:
            self.alto = alto
        else:
            raise DimensionError("ERROR",alto, self.MAX)
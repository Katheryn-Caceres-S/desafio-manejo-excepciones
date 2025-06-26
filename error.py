

#punto 1
class DimensionError(Exception):
    def __init__(self,mensaje,dimension,maximo):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
# punto 2
    def __str__(self):
        #si no le pasamos la dimension y no le pasamos el maximo retornar str del padre
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return f"{self.mensaje} , {self.dimension} , {self.maximo} "
        
    
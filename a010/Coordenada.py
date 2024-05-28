""" Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  """

from math import sqrt

class Coordenada:
    def __init__(self, coord = (0,0), *args):
        if len(args) > 0:
            raise Exception(f"Numero de argumentos errado: {len(locals()) - 1}")
        elif type(coord) != tuple:
            raise Exception(f"Parâmetro não é uma tupla")
        elif len(coord) > 2:
            raise Exception(f"Numero de coordenadas inválido: {len(coord)}")
        elif not all((isinstance(item, int) or isinstance(item, float) for item in coord)):
            raise Exception(f"Elemento da tupla não é int nem float")
        
        self.x = coord[0]
        self.y = coord[1]

    def distancia(self, destino):
        return sqrt( ( ( self.x - destino.x ) ** 2 ) + ( ( self.y - destino.y ) ** 2 ) )
    
    def toTuple(self, operando = 0):
        if type(operando) == int:
            return (self.x + operando, self.y + operando)
        elif type(operando) == float:
            return (self.x * operando, self.y * operando)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

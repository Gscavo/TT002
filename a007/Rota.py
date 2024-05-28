from Coordenada import Coordenada
from typing import List
from random import shuffle as embaralha
from aco import AntColony

class Rota:
    def __init__(self):
        self.coords: List[Coordenada] = []

    def addCoord(self, coord: Coordenada | List[tuple]):
        if type(coord) == Coordenada:
            self.coords.append(coord)
        elif type(coord) == list:
            for el in coord:
                c = Coordenada(el)
                self.coords.append(c)

    def comprimento(self):
        comp = 0
        final_pos = len(self.coords) - 1
        for c in range(final_pos):
            comp += self.coords[c].distancia(self.coords[c + 1])
        comp +=  self.coords[final_pos].distancia(self.coords[0])
        return comp

    def copy(self):
        copia = __class__()
        for c in self.coords:
            copia.addCoord(c)
        return copia

    def shuffle(self):
        return embaralha(self.coords)

    def __str__(self) -> str:
        msg = ""
        for c in self.coords:
            msg += f"{c}->"
        msg += str(self.coords[0])
        return msg
    
    def listaCoords(self):
        return [(c.x, c.y) for c in self.coords]
    
    def otimiza(self, n_formigas: int = 40, n_iter: int = 100):
        colony = AntColony(self.listaCoords(), ant_count=n_formigas, iterations=n_iter)
        self.coords = []
        self.addCoord(colony.get_path())
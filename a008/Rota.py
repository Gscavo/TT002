""" Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  """

from aco import AntColony
from Coordenada import Coordenada
from copy import deepcopy
from PIL import Image, ImageDraw, ImageFont
from typing import List

import math
import random
import time

class Rota:
    def __init__(self):
        self.coords: List[Coordenada] = []
        self.coordsNormalizadas: List[Coordenada] = []
        self.maxes = (0, 0)
        self.mins = (0, 0)

    def addCoord(self, coord: Coordenada):
        if type(coord) == Coordenada:
            self.coords.append(coord)
            self.coordsNormalizadas.append(coord)

    def comprimento(self):
        comp = 0
        final_pos = len(self.coords) - 1
        for c in range(final_pos):
            comp += self.coords[c].distancia(self.coords[c + 1])
        comp +=  self.coords[final_pos].distancia(self.coords[0])
        return comp

    def copy(self):
        return deepcopy(self)

    def desenha(self, filename: str = 'RotaDev.png'):
        self.maximo()
        self.normaliza()

        size = 800
        margin = 100
        draw_width = 8

        img = Image.new(mode="RGBA", size=(size, size), color=(255, 255, 255, 255))
        
        draw = ImageDraw.Draw(img)

        enquadra_na_imagem = lambda xy: (xy * (size - (margin * 2))) + margin

        # linhas
        linha = lambda coord1, coord2: draw.line(
                    xy=(
                        enquadra_na_imagem(coord1.x), 
                        enquadra_na_imagem(coord1.y),
                        enquadra_na_imagem(coord2.x),
                        enquadra_na_imagem(coord2.y)
                        ),
                    fill=(0, 0, 0, 255), 
                    width=draw_width//2)

        ponto = lambda coord, color: draw.rectangle(
                    xy=(
                        enquadra_na_imagem(coord.x)-(draw_width//2),
                        enquadra_na_imagem(coord.y)-(draw_width//2),
                        enquadra_na_imagem(coord.x)+(draw_width//2),
                        enquadra_na_imagem(coord.y)+(draw_width//2),
                    ),
                    fill=color,
        )
        
        for i in range(1, len(self.coordsNormalizadas)):
            linha(self.coordsNormalizadas[i-1], self.coordsNormalizadas[i])
            ponto(self.coordsNormalizadas[i], (0,85,200,255))
        
        linha(self.coordsNormalizadas[len(self.coordsNormalizadas)-1], self.coordsNormalizadas[0])
        ponto(self.coordsNormalizadas[0], (200,85,50,255))

        draw.text(
            xy=(10, size - 30, size, size), 
            text = f'Comprimento total da Rota: {self.comprimento()}',
            align='center',
            fill=(0,0,0,255),
            font= ImageFont.truetype(font='arial.ttf', size=20)
            )

        img.save(filename)
        return img

    def espera(self, delay: int = 1000):
        tin = int(time.time() * 1000)
        delta = int(time.time() * 1000) - tin
        print(f"Esperando : {delta}ms")
        last_printed = delta
        while delta <= delay:
            if delta - last_printed == 1000:
                print(f"Esperando : {delta}ms")    
                last_printed = delta
            delta = int(time.time() * 1000) - tin

    def listaCoords(self):
        lista = []
        for c in self.coords:
            lista.append((c.x,c.y))
        return lista

    def maximo(self):
        max_x = max(self.coords, key= lambda i: i.x)
        min_x = min(self.coords, key= lambda i: i.x)

        max_y = max(self.coords, key= lambda i: i.y)
        min_y = min(self.coords, key= lambda i: i.y)

        self.maxes = (max_x.x, max_y.y)
        self.mins = (min_x.x, min_y.y)

        return self.maxes

    def normaliza(self):

        self.coordsNormalizadas = []

        delta_x = self.maxes[0]-self.mins[0]
        delta_y = self.maxes[1]-self.mins[1]

        for c in self.coords:
            x = (c.x - self.mins[0]) / delta_x
            y = (c.y - self.mins[1]) / delta_y
            new_coord = Coordenada((x,y)) 
            self.coordsNormalizadas.append(new_coord)
        
    def otimiza(self, n_formigas: int = 30, n_iter: int = 300):
        if (True):
            teste = self.copy()

            colony = AntColony(teste.listaCoords(), start=None, ant_count= n_formigas, iterations= n_iter)
                
            self.coords = []

            for el in colony.get_path():
                self.addCoord(Coordenada((el[0], el[1])))
        else:
            mudou = True
            while(mudou):
                mudou = False
                for i in range(10000):
                    rotaAux = self.copy()
                    rotaAux.shuffle()
                    if rotaAux.comprimento() < self.comprimento():
                        self.coords = rotaAux.coords
                        print(self.comprimento())
                        mudou = True

    
    def randomCoords(self, n: int = 8, max_coord: int = 400):
        self.coords = []
        self.coordsNormalizadas = []
        for i in range(n):
            coord = Coordenada((random.randint(1, max_coord), random.randint(1, max_coord)))
            self.addCoord(coord=coord)

    def shuffle(self):
        return random.shuffle(self.coords)

    def __str__(self) -> str:
        msg = ""
        for c in self.coords:
            msg += f"{c}->"
        msg += str(self.coords[0])
        if False:
            msg += '\n'
            for c in self.coordsNormalizadas:
                msg += f"{c}->"
            msg += str(self.coordsNormalizadas[0])
        return msg

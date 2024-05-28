''' Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  '''

from Linha import Linha as Ln

class Tabela:
    def __init__(self):
        self.cabecalho = Ln()
        self.dados = []

    def add_cabecalho(self, lista: list):
        self.cabecalho.append(lista)
    
    def addLinha(self, dado: Ln):
        if len(dado) is not len(self.cabecalho):
            print("Tamanhos incompatíveis\n")
        else: 
            self.dados.append(dado)

    def ordena_por(self, valor):
        idx = self.cabecalho.dados.index(valor)
        self.dados.sort(key= lambda v: v.dados[idx])


    def __str__(self):
        str_final = f"{self.cabecalho}\n"
        str_final = str_final + "---------------------------------------\n"
        for el in self.dados:
            str_final = str_final + f"{el}\n"
        return str_final
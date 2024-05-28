''' Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  '''

from Linha import Linha as Ln

class Tabela:
    def __init__(self, filename = None):
        self.cabecalho = Ln()
        self.dados = []
        if filename:
            file = open(filename,"r")
            # self.add_cabecalho(file.readline().strip("][\n").replace("'", "").split(','))
            self.add_cabecalho(eval(file.readline()))
            for line in file.readlines():
                # self.addLinha(line.strip("][\n").replace("'", "").split(','))
                self.addLinha(eval(line))
                
    def add_cabecalho(self, lista: list):
        for x in range(len(lista)):
            if type(lista[x]) == str:
                lista[x] = lista[x].strip()
        self.cabecalho.append(lista)
    
    def addLinha(self, dado: Ln | list):
        if type(dado) == list:
            line = Ln()
            line.append(dado)
        elif type(dado) == Ln:
            line = dado
        else:
            return None
        
        if len(line) != len(self.cabecalho):
            print(self.cabecalho, line)
            print("Tamanhos incompatíveis\n")
        else: 
            for i in range(len(line)):
                if type(line.dados[i]) == str:
                    line.dados[i].strip()
            self.dados.append(line)

    def ordena_por(self, valor):
        idx = self.cabecalho.dados.index(valor)
        self.dados.sort(key= lambda v: v.dados[idx])

    def writeFile(self, filename: str):
        file = open(filename, "w")
        file.write(str(self.cabecalho).replace(f"({len(self.cabecalho)})", "\n"))
        for line in self.dados:
            file.write(str(line).replace(f"({len(self.cabecalho)})", "\n"))

    def __str__(self):
        str_final = str(self.cabecalho).replace(f"({len(self.cabecalho)})", "\n")
        str_final = str_final + "---------------------------------------\n"
        for el in self.dados:
            str_final = str_final + str(el).replace(f"({len(self.cabecalho)})", "\n")
        return str_final
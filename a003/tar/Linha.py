''' Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  '''

class Linha:
    def __init__(self):
        self.dados = []
    
    def append(self, dados):
        if type(dados) is list:
            for el in dados:
                self.dados.append(el)
        else:
            self.dados.append(dados)

    def __str__(self):
        return f"{self.dados}({len(self)})"

    def __len__(self):
        return len(self.dados)
        

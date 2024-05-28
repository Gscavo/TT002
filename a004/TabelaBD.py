''' Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691  '''

from Tabela import Tabela

class TabelaBD(Tabela):
    def __init__(self, filename = None):
        super().__init__(filename=filename)

    def conta(self, coluna: str) -> Tabela:
        col_idx = self.cabecalho.dados.index(coluna)
        result = Tabela()
        result.add_cabecalho([coluna, "numero"])
        for linhaBD in self.dados:
            valor = linhaBD.dados[col_idx]
            existe_valor = False
            for linhaConta in result.dados:
                if linhaConta.dados[0] == valor:
                    linhaConta.dados[1] += 1
                    existe_valor = True
                    break
            if not existe_valor:
                result.addLinha([valor, 1])                
        result.ordena_por("numero")
        return result

    def select(self, option, value) -> Tabela:
        col_idx = self.cabecalho.dados.index(option)
        result = Tabela()
        result.add_cabecalho(self.cabecalho.dados)
        for linha in self.dados:
            valor = linha.dados[col_idx]
            if valor == value:
                result.addLinha(linha)
        return result
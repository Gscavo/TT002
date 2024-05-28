"""
    Nome:                               Ra:
    Felipe Costa                        254214
    Guilherme Simões Cavo               254245
    Pedro Augusto Canuto de Oliveira    186691
"""

# Tentativas de plágio serão punidas de maneira exemplar.

# Em grupo de três alunos. Apenas um deve
# submeter o trabalho. O nome e RA dos três
# alunos devem estar junto com o código fonte.

# Nesta tarefa você irá receber um conjunto de assinaturas de funções e terá que implementá-las.
# Primeiramente considere um carro formado por um dicionário da seguinte maneira:
import random

carro = dict()
carro["placa"] = "BBB2B99"
carro["ano"] = 2022
carro["marca"] = "chevrolet"
carro["modelo"] = "onix"
# print(carro)

#Considere também uma variável a seguir:

filename = "carros.txt"

# Daqui para frente não é permitida mais nenhuma variável fora das funções.
# Todas as variáveis devem estar nas funções.


# você está recebendo um projeto com a descrição das funções
# para você implementar. Implemente as funções conforme a descrição.


# Esta função recebe uma variável carro, converte numa
# string e faz um append no arquivo associado a filename.
# Ao final o arquivo deve ser fechado. Deve haver um carro
# por linha.
# Número estimado de linhas: 3 (é o número de linhas gasto pelo
# professor.
def addCarro(carro):
    # seu código vem aqui.
    # print("add:" + str(carro))
    file = open(filename, 'a')
    file.write(str(carro)+"\n")
    file.close()


# Esta função abre o arquivo associado a filename
# e, para cada linha, cria um dicionário carro no
# mesmo padrão mostrado no início deste trabalho.
# Cada carro deve ser adicionado a uma lista, e,
# ao final, esta lista deve ser devolvida pela função.
# O arquivo deve ser fechado após a leitura.
# Número estimado de linhas: 8
def carregaCarros():
    # seu código vem aqui.
    # print("carrega carros")
    file = open(file=filename, mode='r')
    carros = list()
    for line in file.readlines():
        carro = eval(line)
        carros.append(carro)
    file.close()
    return carros


# Esta função verifica se a placa passada como
# parâmetro já existe na base de dados (arquivo salvo
# em filename). Primeiro deve ser feita a leitura de
# todos os carros fazendo uma chamada da função
# carregaCarros. Após isso, deve verificar se
# a placa passada como parâmetro já existe. Neste caso devolve True.
# Caso a placa não exista, devolve False.
# Número estimado de linhas: 6
def contemPlaca(placa):
    # seu código vem aqui.
    # print("contém placa"+placa)
    carros = carregaCarros()
    for carro in carros:
        if carro.get("placa") == placa:
            return True
    return False

# Esta função cria uma placa aleatória no padrão novo,
# LLLNLNN onde L é uma letra e N é um dígito. Deve ser usada
# a função random.choice. A geração da placa aleatória implica
# que todas as placas têm a mesma probabilidade de
# serem geradas. Após gerar uma placa aleatória, deve ser chamada a função
# contemPlaca. Se a placa já existir, o processo deve se repetir até
# que seja gerada uma plana nova (que ainda não pertence ao arquivo de dados)
# Numero estimado de Linhas: 14.
def placaAleatoria():
    # seu código vem aqui.
    # print("placa aleatória")
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    placa = ''
    for c in range(0,7):
        if (c == 3) or (c > 4):
            placa = placa + random.choice(nums)
        else:
            placa = placa + random.choice(letras)
    if contemPlaca(placa=placa):
        return placaAleatoria()
    else:
        return placa

# Esta função cria um carro aleatório. O carro é um dicionario com
# placa, ano, marca e modelo. A placa deve ser gerada pela função
# placaAleatoria() que já foi implementada. A marca é uma escolha
# equiprovavel entre ["chevrolet","volkswagem","fiat"]. Se a marca
# for chevrolet, o carro é uma escolha equiprovável entre
# ["onix","cruze","camaro"]. Se a marca for "volkswagem", o modelo
# é uma escolha equiprovável entre ["polo","jetta","gol"]. Se
# a marca for fiat, o modelo é uma escolha equiprovável entre
# ["pulse","argo","moby"].
# Número estimado de linhas: 21
def carroAleatorio():
    # print("carro aleatório")
    # seu código vem aqui.
    carro = dict()
    placa = placaAleatoria()
    marca = random.choice(["chevrolet", "volkswagem", "fiat"])
    modelo = ''
    ano = random.randint(2000, 2023)
    match marca:
        case 'chevrolet':
            modelo = random.choice(["onix","cruze","camaro"])
        case "volkswagem":
            modelo = random.choice(["polo","jetta","gol"])
        case "fiat":
            modelo = random.choice(["pulse","argo","moby"])
    carro = {
        "placa": placa,
        "ano": ano,
        "marca": marca,
        "modelo": modelo
    }
    return carro


# Esta função deve inicialmente apagar o conteúdo do
# arquivo de dados. Após isso, deve ser gerado um conjunto
# de 200 carros aleatórios. Tais carros devem ser inseridos
# no arquivo de dados, por meio da função addCarro().
# Número estimado de linhas: 4
def populaDados():
    # seu código vem aqui.
    # print("popula dados")
    file = open(file=filename, mode='w')
    for i in range(0,200):
        carro = carroAleatorio()
        addCarro(carro=carro)
    file.close()


# Veja um exemplo de execução.
# Inicialmente o programa chama a função populaDados()
# inserindo 200 carros aleatórios no arquivo de dados. Isso
# é feito fora da função geraEstatistica().
# Após isso, é chamada uma função manualAddCarro() ainda
# fora da função geraEstatistica().
# Suponha que o usuário digitou os dados abaixo
# Digite a placa:BBB1B22
# Digite ano:2000
# Digite marca:Honda
# Digite Modelo:Fit
# Agora foi finalmente chamada a função geraEstatistica().
# Primeiramente ela imprime uma lista de anos, e o número
# de carros por ano, conforme abaixo. Depois uma lista de marcas
# e o número de carros por marca. Finalmente uma lista de
# modelos, e o número de carros por modelo. Note que os valores
# podem diferir, pois a geração é aleatória. Note
# também que os anos/marcas/modelos são impressos em ordem crescente.
# Abaixo a saída da função geraEstatística.
# -- Numero de carros por ano ---
# ano 2000: 1 carro(s)
# ano 2015: 26 carro(s)
# ano 2016: 37 carro(s)
# ano 2017: 42 carro(s)
# ano 2018: 36 carro(s)
# ano 2019: 31 carro(s)
# ano 2020: 28 carro(s)
# -- Numero de carros por marca ---
# marca Honda: 1 carro(s)
# marca chevrolet: 64 carro(s)
# marca fiat: 75 carro(s)
# marca volkswagem: 61 carro(s)
# -- Numero de carros por modelo ---
# modelo Fit: 1 carro(s)
# modelo argo: 29 carro(s)
# modelo camaro: 19 carro(s)
# modelo cruze: 23 carro(s)
# modelo gol: 18 carro(s)
# modelo jetta: 25 carro(s)
# modelo moby: 20 carro(s)
# modelo onix: 22 carro(s)
# modelo polo: 18 carro(s)
# modelo pulse: 26 carro(s).
#
# Número de Linhas Esperado: 3+14, sendo 3 nesta função
# e 14 numa função auxiliar.
def geraEstatistica():
    # seu código vem aqui.
    # print("gera Estatistica")
    printData('ano')
    printData('marca')
    printData('modelo')

def printData(key):
    print(f"-- Numero de carros por {key} ---")
    carros = carregaCarros()
    data = dict()
    for carro in carros:
        if not data.get(carro[key]):
            data[carro.get(key)] = 0
        data[carro.get(key)] += 1
    data = dict(sorted(data.items()))
    for k, v in data.items():
        print(f"{key} {k}: {v} carro(s)")

def manualAddCarro():
    placa = input("Digite a placa:")
    ano = int(input("Digite ano:"))
    marca = input("Digite marca:")
    modelo = input("Digite Modelo:")
    addCarro({"placa": placa, "ano": ano, "marca": marca, "modelo": modelo})


populaDados()
manualAddCarro()
geraEstatistica()
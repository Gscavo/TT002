""" for letra in 'Minha String':
    print(letra)

amigos = ["Joao", "Pedro", "Matheus"]

for amigo in amigos:
    print(amigo) """

# Trocar todas as vogais por g
# Amanda => Gmgndg
def traduz(frase):
    traducao = ''
    for letra in frase:
        if letra in "AEIOUaeiou":
            if letra.isupper():
                traducao = traducao + "G"
            else:
                traducao = traducao + "g"
        else:
            traducao = traducao + letra
    return traducao

print(traduz("Amanda"))

""" file = open("empregados.txt", "r")
file.close()

file = open("empregados2.txt", "w")
file.close()

file = open("empregados3.txt", "a")
file.close()

# file.read() => Lê todo o arquivo
print(file.read())

# file.readline() => Lê linha por linha do arquivo
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# file.readlines() => Lê todas as linhas do arquivo e retorna uma lista
for linha in file.readlines():
    print(linha, end="") """

# Dicionários em python
listaA = ["Luis", "Meira"]
tuplaA = ("Luis", "Meira")
dicionarioA = {"nome": "Luis", "sobrenome": "Meira"}
print(dicionarioA["nome"])
print(dicionarioA["sobrenome"])
dicionarioA["sexo"] = "M"
print(dicionarioA)
del dicionarioA["nome"]
print(dicionarioA)
print(dicionarioA.get("sobrenome"))
print(dicionarioA.get("sla", "chave inválida"))

for key in dicionarioA.keys():
    print(key)

for value in dicionarioA.values():
    print(value)

for chave, valor in dicionarioA.items():
    print(f"chave_{chave}: {valor}")

filme = {
    "titulo": "Star Wars",
    "ano": 1977,
    "diretor": "George Lucas"
}

for chave, valor in filme.items():
    print(f"O {chave} é {valor}")

locadora = []

locadora.append(filme)

locadora.append({ "titulo": "Vingadores", 
                "ano": 2012,
                "diretor": "Jose Whedon"
                })

locadora.append({ "titulo": "Matrix", 
                "ano": 1999,
                "diretor": "Wachowsky"
                })

print(locadora)

brasil = list()
estado = dict()

for c in range(0,3):
    # Conserto 1
    # estado = dict()
    estado['uf'] = str(input("UF: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado)
    # Conserto 2
    # brasil.append(estado.copy)

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} é {v}.")
print(brasil)
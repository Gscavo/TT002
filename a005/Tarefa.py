""" Nome:                               Ra:
Felipe Costa                        254214
Guilherme Simões Cavo               254245
Pedro Augusto Canuto de Oliveira    186691 """

import geopy.distance

# Você recebeu um aquivo chamado coordenadas.txt.
# Você deve fazer a leitura deste aquivo.
file = open("coordenadas.txt", "r")

# Cada linha do arquivo é um registro com 5 campos, separados por ponto e vírgula (;).
# Veja um exemplo:
# Campinas;Sao Paulo;SP;-22.9;-47.0833333
#
# Outro exemplo:
# Agua Azul;Parana;PR;-25.8;-50.2
#
# O primeiro campo é a localidade, que pode ser uma cidade, um distrito,
# etc. O segundo é o estado. O terceiro é a sigla do estado.
# O quarto é a latitude e o quinto é a longitude.
linhas = file.readlines()
coordenadas = []
for linha in linhas:
    coordenadas.append(linha.strip("\n").split(";"))

# Após a leitura, você vai pedir para o usuário digitar uma latitude e uma longitude:
#
# Digite a latitude: -25.43
# Digite a longitude: -49.27

lat = float(input("Digite a latitude: "))
long = float(input("Digite a longitude: "))

# Após isso, você vai buscar qual a localidade mais próxima da coordenada digitada:
#
# A coordenada mais próxima de (-25.43, -49.27) é:
# Curitiba;Parana;PR;-25.4166667;-49.25
# Distância:2.4959858427746413km

input_coordenada = (lat, long)

mais_perto = {
    "dados": coordenadas[0], 
    "dist": geopy.distance.geodesic(input_coordenada, (coordenadas[0][3], coordenadas[0][4])).km
}

for linha in coordenadas:
    linha_coord = (linha[3], linha[4])
    if geopy.distance.geodesic(input_coordenada, linha_coord).km < mais_perto["dist"]:
        mais_perto["dados"] = linha
        mais_perto["dist"] = geopy.distance.geodesic(input_coordenada, linha_coord).km

print(f"A coordenada mais próxima de ({lat:.2f}, {long:.2f}) é:")
print(mais_perto["dados"])
print(f'Distância:{mais_perto["dist"]}Km')
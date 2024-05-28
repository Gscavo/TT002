import geopy.distance

# O seguinte código abre o arquivo de coordenadas e o transforma
# em uma lista.

file = open("coordenadas.txt", "r")  # read
dados = file.readlines()

# for linha in dados:
#    print(linha)

# O código abaixo calcula a distância entre duas coordeandas:

lat1 = -22.9
lo1 = -47.0833333
campinas = (lat1, lo1)

lat1 = -22.9
lo1 = -47.0833333
campinas = (lat1, lo1)

lat2 = -22.5616667
lo2 = -47.4027778
limeira = (lat2, lo2)

dist = geopy.distance.geodesic(campinas, limeira).km

print(f"A distância entre Limeira e Campinas em linha reta é {dist}Km")

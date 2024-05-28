"""     Nome:                               Ra:
        Felipe Costa                        254214
        Guilherme Simões Cavo               254245
        Pedro Augusto Canuto de Oliveira    186691      """

# Tarefa em grupo de 3 pessoas. Apenas um submete, porém com o nome
# dos três integrantes.

# Neste projeto, você deve inicialmente abrir o arquivo de coordenadas.
# Em seguida, você deve fazer a varredura nas coordenadas.
#
# Depois disso, você deve criar uma imagem em branco, 1001x1001.
# Cada coordenada do arquivo deve ser desenhada na imagem que foi
# criada.
#
# Você deve fazer um processo de normalização de modo que a menor latitude
# esteja associada à posição zero e a maior latitude esteja associada à posição
# 1000. Uma latitude intermediaria vai estar em um ponto intemediario entre
# 0 e 1000. Este é um processo chamado normalização.
# O mesmo deve ser feito para longitude.
# Após desenhar as coordenadas na imagem, deve rotacioná-la de maneira
# que o norte esteja para cima e o leste para a direita.
#
# Uma melhoria que deve ser feita é a seguinte: Cada estado
# deve ser pintado com uma cor entre (preto, azul, amarelo, cinza).
# Além disso, estados que possuem fronteira maior que zero
# devem ter cores diferentes.
#
# Ao final, você deve salvar o resulado em Brasil.png
#
# Você deve submeter o arquivo Brasil.png e o arquivo python com o programa.

from PIL import Image

def le_arquivo(filename):
    lista = []
    with open(filename, 'r') as file:
        lista_dados = file.readlines()
        for dado in lista_dados:
            coord_dict = dict()
            dado = dado.split(";")
            coord_dict["estado"] = dado[2]
            coord_dict["latitude"] = float(dado[3])
            coord_dict["longitude"] = float(dado[4])
            lista.append(coord_dict)
    return lista

def desenha_imagem(img: Image, list: list, lat_data: dict, long_data: dict):
    cores = load_cores_estados()
    for linha in list:
        xPixel = ((linha["longitude"] - long_data["min"]) / (long_data["max"] - long_data["min"])) * 1000
        yPixel = (-(linha["latitude"] - lat_data["min"]) / (lat_data["max"] - lat_data["min"])) * 1000
        
        img.putpixel((int(xPixel), int(yPixel)), cores[linha["estado"]])
    img.rotate(90)

def load_cores_estados():
    amarelo = (255, 255, 0)
    azul = (0, 0, 255)
    cinza = (150, 150, 150)
    preto = (0, 0, 0)
    cores_data = {
        "AC": cinza,
        "AL": azul,
        "AM": azul,
        "AP": cinza,
        "BA": amarelo,
        "CE": amarelo,
        "DF": preto,
        "ES": cinza,
        "GO": cinza,
        "MA": preto,
        "MG": azul,
        "MS": amarelo,
        "MT": preto,
        "PA": amarelo,
        "PB": cinza,
        "PE": preto,
        "PI": cinza,
        "PR": cinza,
        "RJ": amarelo,
        "RN": azul,
        "RO": amarelo,
        "RR": preto,
        "RS": amarelo,
        "SC": azul,
        "SE": cinza,
        "SP": preto,
        "TO": azul,
    }
    return cores_data

if __name__ == "__main__":
    filename = 'coordenadas.txt'
    lista_coords = le_arquivo(filename)
    imagem_brasil = Image.new("RGBA", (1001,1001), (255,255,255, 0))
    lista_ordenada = sorted(lista_coords, key = lambda k: k["latitude"])

    latitude_data = {
        "min": lista_ordenada[0]["latitude"],
        "max": lista_ordenada[len(lista_ordenada) - 1]["latitude"]
    }

    lista_ordenada = sorted(lista_coords, key = lambda k: k["longitude"])
    
    longitude_data = {
        "min": lista_ordenada[0]["longitude"],
        "max": lista_ordenada[len(lista_ordenada) - 1]["longitude"]
    }

    del lista_ordenada

    desenha_imagem(imagem_brasil, lista_coords, latitude_data, longitude_data)

    imagem_brasil.show()
    imagem_brasil.save("Brasil.png")
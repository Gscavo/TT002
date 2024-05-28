from matplotlib import pyplot as plt
#Idade do programador
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# Dados fictícios abaixo
#Salário médio do programador, em função da idade.
dev_y = [2000, 2100, 2500, 2300, 4000, 4500,
         4000, 4700, 5000, 5500, 6000]
#O mesmo que o anterior, porém para progrmaador javaScript
js_dev_y = [2000, 2100, 2100, 2500, 4000, 4500,
            4500, 4700, 4000, 4500, 4000]
#O mesmo que o anterior, porém para programador Python.
py_dev_y = [2100, 2200, 2300, 2700, 4100, 4800,
            5000, 5700, 6000, 6500, 7000]

#Estílos de gráficos.
print(plt.style.available)

#Troque o estilo abaixo e veja o resultado.

#plt.style.use('Solarize_Light2')
#plt.style.use('dark_background')
plt.style.use('fivethirtyeight')


#[Marcador][line][color]
#Exemplo "o--b" (bolinha,tracejado,blue)
#plt.plot(dev_x, dev_y,"o--b",label="Todos")
#plt.xkcd()
plt.plot(dev_x, dev_y,"o--",color='b',label="Todos")
# Para outros marcadores, veja https://matplotlib.org/stable/api/markers_api.html
# Para outros estilos de linha, veja https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
plt.plot(dev_x, js_dev_y,color='g',label='JavaScript')
plt.plot(dev_x, py_dev_y,color='k',label='Python',linewidth=3)
plt.xlabel("Idades")
plt.ylabel("Salarios (R$)")
plt.title("Salário Médio por Idades")
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('Salarios.png')
plt.show()

# Para maiores informações sobre o matplotlib, consulte
# o link abaixo:
# https://matplotlib.org/3.8.0/index.html#learn








#salario programadores js

# salario programadores py

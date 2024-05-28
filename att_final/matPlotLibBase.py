from matplotlib import pyplot as plt
import numpy as np


# Exemplo 1
eixo_x = ['JavaScript', 'HTML', 'SQL', 'Python', 'Java',
          'Bash', 'C#', 'PHP', 'C++', 'TypeScript', 'C']
eixo_y = [60000, 50000, 45000, 38000, 37000,
          30000, 25000, 22000, 19000, 18000, 17500]

eixo_x.reverse()
eixo_y.reverse()

plt.barh(eixo_x,eixo_y)
plt.title("Linguagens Mais Populares")
plt.xlabel("Numero de Pessoas que usa")
plt.tight_layout()
plt.savefig("Grafico1.png")
plt.show()
#exit(0)

# Exemplo 2
idades = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,40]
# Salários programadores por idade.
dev_y = [2000, 2100, 2500, 2300, 4000, 4500, 4000, 4700, 5000, 5500, 6000,8000]
# Programadores Python.
py_dev_y = [2100, 2200, 2300, 2700, 4100, 4800, 5000, 5700, 6000, 6500, 7000,8500]
# Java Script.
js_dev_y = [2000, 2100, 2100, 2500, 4000, 4500, 4500, 4700, 4000, 4500, 4000,6000]


plt.xlabel("Idades")
plt.ylabel("Salários (R$)")
plt.title("Salário Médio de Progradores por Idade")
plt.bar(idades, dev_y, label="Todos")
plt.plot(idades, py_dev_y, label="Python")
plt.plot(idades, js_dev_y, label="JavaScrip")
plt.legend()
plt.savefig("Grafico1.png")

plt.show()

#exit(0)

#Exemplo 3

eixo_x = ['Aleatorio', 'SingleSwap', 'Grupo1']
custos_y = [2000, 2100, 2500]
erros = [200, 101, 50]

largura = 0.2

plt.xlabel("Algoritmos")
plt.ylabel("Custos")
plt.title("Custo Por Algortimo")

plt.bar(eixo_x, custos_y, width=largura, label="todos",yerr=erros,capsize=5)
plt.savefig("Grafico1.png")

plt.show()


#exit(0)


#Exemplo 4


x_indexes = np.arange(len(idades))
print(x_indexes)
largura = 0.25

plt.xlabel("Idades")
plt.ylabel("Salários (R$)")
plt.title("Salário Médio de Progradores por Idade")
plt.bar(x_indexes-largura, dev_y, label="Todos", width=largura)
plt.bar(x_indexes, py_dev_y, label="Python", width = largura)
plt.bar(x_indexes+largura, js_dev_y, label="JavaScrip", width = largura)
plt.legend()
plt.xticks(ticks=x_indexes, labels = idades)
plt.savefig("Grafico1.png")
plt.show()


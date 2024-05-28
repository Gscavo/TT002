class Empregado:
    numero_empregados = 0 # Variaveis compartilhadas entre todos os objetos (estatica)
    taxa_aumento = 1.04
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + "." + sobrenome + "@empresa.com"
        Empregado.numero_empregados += 1

    def nomeCompleto(self):
        return self.nome + " " + self.sobrenome
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome} {self.salario}"
    
    def aplicaAumento(self):
        self.salario *= Empregado.taxa_aumento

    @classmethod
    def atualizaTaxaAumento(cls, novaTaxa):
        cls.taxa_aumento = novaTaxa

    @classmethod
    def from_string(cls, emp_str):
        nome, sobrenome, salario = str_empregado.split("-")
        return cls(nome, sobrenome, int(salario))

# pass: classe vazia

empr_1 = Empregado("Pedro", "Silva", 2000)
empr_2 = Empregado("Laryssa", "Linux", 5000)

print(empr_2.__dict__)
print(empr_1)

print(empr_1.numero_empregados)
print(empr_2.numero_empregados)

empr_1.aplicaAumento()
print(empr_1)

Empregado.atualizaTaxaAumento(1.1)
empr_2.aplicaAumento()
print(empr_2)

str_empregado = "Linux-Cavo-100000"

empr_3 = Empregado.from_string(str_empregado)
print(empr_3)

class Desenvolvedor(Empregado):
    def __init__(self, nome, sobrenome, salario, linguagem):
        super().__init__(nome, sobrenome, salario)
        self.linguagem = linguagem

dev_1 = Desenvolvedor("Maria", "Vitoria", 7500, "Python")

print(dev_1.linguagem)

class Gerente(Empregado):
    def __init__(self, nome, sobrenome, salario, empregados = None):
        super().__init__(nome, sobrenome, salario)
        if empregados is None:
            self.empregados = []
        else:
            self.empregados = empregados

    def add_empr(self, empr):
        if empr not in self.empregados:
            self.empregados.append(empr)

    def remove_empr(self, empr):
        if empr in self.empregados:
            self.empregados.remove(empr)

    def imprimeEmpr(self):
        for emp in self.empregados:
            print("--->"+emp.nomeCompleto())
            
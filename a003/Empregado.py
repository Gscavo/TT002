class Empregado:
    taxa_aumento = 1.04
    numero_empregados = 0

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + "." + sobrenome + "@empresa.com"
        Empregado.numero_empregados += 1

    def nomeCompleto(self):
        return self.nome + " " + self.sobrenome

    def __str__(self):
        return f"Nome {self.nome} {self.sobrenome} sal:{self.salario}"

    def aplicaAumento(self):
        self.salario = int(self.salario * self.taxa_aumento)

    @classmethod
    def atualizaTaxaAumento(cls, taxa):
        cls.taxa_aumento = taxa

    @classmethod
    def from_string(cls, emp_str):
        nome, sobrenome, salario = emp_str.split("-")
        return cls(nome, sobrenome, int(salario))


# Instancias da classe
emp_1 = Empregado("Pedro", "Silva", 2000)
emp_2 = Empregado("Ana", "Braga", 3000)

print(emp_1.salario)
emp_1.aplicaAumento()
print(emp_1.salario)
Empregado.taxa_aumento = 1.08
print(emp_1.taxa_aumento)
print(emp_2.taxa_aumento)

print(emp_1.__dict__)
print(Empregado.__dict__)



# emp_1.taxa_aumento = 1.06
print(emp_1.__dict__)

print(Empregado.numero_empregados)

Empregado.atualizaTaxaAumento(1.04)
print(emp_1.taxa_aumento)
print(emp_2.taxa_aumento)

# print(emp_2)
# print(emp_1.nomeCompleto())

emp1_str = "Pedro-Silva-2000"
emp2_str = "Ana-Braga-2000"

nome, sobrenome, salario = emp1_str.split("-")
emp_1 = Empregado(nome, sobrenome, int(salario))
print(emp_1)

emp_2 = Empregado.from_string(emp2_str)
print(emp_2)


class Desenvolvedor(Empregado):
    taxa_aumento = 1.1

    def __init__(self, nome, sobrenome, salario, linguagens):
        super().__init__(nome, sobrenome, salario)
        self.linguagens = linguagens



dev_1 = Desenvolvedor("Pedro", "Silva", 2000, "Java")
dev_2 = Desenvolvedor("Marina", "Pereira", 2000, "Python")

print(help(Desenvolvedor))

print(dev_1.salario)
dev_1.aplicaAumento()
print(dev_1.salario)

print(dev_1.nomeCompleto())
print(dev_1.linguagens)


class Gerente(Empregado):
    def __init__(self, nome, sobrenome, salario, empregados=None):
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

    def print_emp(self):
        for emp in self.empregados:
            print("-->"+emp.nomeCompleto())


gerente_1 = Gerente("Susy", "Vieira", 3000, [dev_1])

gerente_1.add_empr(dev_2)

print(gerente_1.email)
gerente_1.print_emp()
#gerente_1.remove_empr(dev_2)
#print(gerente_1.print_emp())


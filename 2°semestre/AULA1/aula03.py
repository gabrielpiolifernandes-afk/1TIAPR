class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
   
    def display_info(self):
        return f"animal: {self.nome}, raça: {self.cpf}, idade: {self.idade}"

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade,cargo,salario,tempoEmpresa):
        super().__init__(nome, cpf, idade)
        self.caro =cargo
        self.salario = salario
        self.tempoEmpresa = tempoEmpresa

class Dependente (Pessoa):
    def __init__(self, nome, cpf, idade,escola,serie,responsavel):
        super().__init__(nome, cpf, idade)
        self.escola = escola
        self.serie = serie
        self.responsavel =responsavel

        
class Conta:
    def __init__(self,titular,agencia,conta,saldo):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
class ContaCorrente(Conta):
    def __init__(self,titular,agencia,conta,saldo,limite):
        super().__init__(titular,agencia,conta,saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <=0:
            print("Valor menor ou igual a zero nao pode ser sacado")
        if valor > (self.saldo + self.limite):
            print("Valor maior que o saldo + limite, tente outro!")

        self.saldo -= valor
        print(f"Valor: {valor} sacodo com sucesso, seu saldo atual é: {self.saldo}")

class ContaPoupaca(Conta):
    def __init__(self,titular,agencia,conta,saldo,juros):
        super().__init__(titular,agencia,conta,saldo)
        self.juros = juros
    
    def render(self):
        self.saldo += self.saldo * (self.juros/100)

poupaca = ContaPoupaca ( "Leo",1,1234,1000,10)
poupaca.render()

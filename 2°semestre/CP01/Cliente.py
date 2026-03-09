import json
import os

arquivo = "clientes.json"

class Cliente:
    def __init__(self, id, nome, cpf, telefone, cep, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cep = cep
        self.senha = senha

def leitura_de_dados():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def cadastro():
    #DADOS
    while True:
        try:
            while True:
                try:
                    id = int(input("ID: "))
                    clientes_existentes = leitura_de_dados()
                    ids_existentes = [c['id'] for c in clientes_existentes]

                    if id in ids_existentes:
                        print("ID já cadastrado! Digite um ID diferente.")
                    else:
                        break
                except ValueError:
                    print("Digite um número válido para o ID.")

            nome = input("Nome: ")

            while True:
                cpf = input("CPF (11 dígitos): ")
                if cpf.isdigit() and len(cpf) == 11:
                    cpf = int(cpf)
                    break
                print("CPF inválido! Deve ter 11 dígitos.")

            while True:
                telefone = input("Telefone (10 ou 11 dígitos): ")
                if telefone.isdigit() and 10 <= len(telefone) <= 11:
                    telefone = int(telefone)
                    break
                print("Telefone inválido!")

            while True:
                cep = input("CEP (8 dígitos): ")
                if cep.isdigit() and len(cep) == 8:
                    cep = int(cep)
                    break
                print("CEP inválido!")
            
            senha = input("Senha: ")

            confirmar_senha = input("Confirme a senha: ")
            if senha != confirmar_senha:
                print("As senhas não coincidem! Tente novamente.")
                continue
            
            #CONFIRMAÇÃO
            while True:
                print("\n--- Resumo do Cadastro ---")
                print(f"ID: {id}")
                print(f"Nome: {nome}")
                print(f"CPF: {cpf}")
                print(f"Telefone: {telefone}")
                print(f"CEP: {cep}")
                print(f"Senha: {senha}")

                confirma = input("Deseja alterar algum dado? (S/N): ").strip().upper()
                #CONF
                if confirma == "N":
                    return Cliente(id=id, nome=nome, cpf=cpf, telefone=telefone, cep=cep, senha=senha)
                
                #TROCA DE DADOS
                elif confirma == "S":
                    print("\nQual dado deseja alterar?")
                    print("1 - ID")
                    print("2 - Nome")
                    print("3 - CPF")
                    print("4 - Telefone")
                    print("5 - CEP")
                    print("6 - Senha")
                    
                    campo = input("Digite o número do campo que deseja alterar: ").strip()

                    if campo == "1":
                        while True:
                            try:
                                novo_id = int(input("Novo ID: "))
                                ids_existentes = [c['id'] for c in leitura_de_dados()]
                                if novo_id in ids_existentes:
                                    print("ID já cadastrado! Digite outro.")
                                else:
                                    id = novo_id
                                    break
                            except ValueError:
                                print("Digite um número válido para o ID.")
                    
                    elif campo == "2":
                        nome = input("Novo Nome: ")
                   
                    elif campo == "3":
                        while True:
                            cpf_input = input("Novo CPF (11 dígitos): ")
                            if cpf_input.isdigit() and len(cpf_input) == 11:
                                cpf = int(cpf_input)
                                break
                            print("CPF inválido!")
                    
                    elif campo == "4":
                        while True:
                            tel_input = input("Novo Telefone (10 ou 11 dígitos): ")
                            if tel_input.isdigit() and 10 <= len(tel_input) <= 11:
                                telefone = int(tel_input)
                                break
                            print("Telefone inválido!")
                    
                    elif campo == "5":
                        while True:
                            cep_input = input("Novo CEP (8 dígitos): ")
                            if cep_input.isdigit() and len(cep_input) == 8:
                                cep = int(cep_input)

                                break
                            print("CEP inválido!")
                    
                    elif campo == "6":
                        while True:
                            nova_senha = input("Nova Senha: ")
                            confirmar_senha = input("Confirme a senha: ")
                            if nova_senha == confirmar_senha:
                                senha = nova_senha
                                break
                            print("As senhas não coincidem! Tente novamente.")
                    else:
                        print("Opção inválida. Digite um número de 1 a 5.")
                else:
                    print("Digite S para sim ou N para não.")

        except ValueError:
            print("Erro: digite valores válidos.")
    
#while not cpf.isdigit() or len(cpf) != 11:
#.strip() para remover espaços em branco
#.upper() para converter para maiúsculas
#isdigit() para verificar se a string contém apenas dígitos

def salvar_dados(cliente):
    # Se o arquivo não existir, criamos uma lista vazia
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []

    # Adiciona o cliente recém-criado
    dados.append(cliente.__dict__)

    # Salva de volta no JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

#os.path.exists() para verificar se o arquivo existe
#dict() para converter o objeto Cliente em um dicionário antes de salvar no JSON

def listar_clientes():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                print("\nLISTA DE CLIENTES\n")
                for cliente in dados:
                    print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | CPF: {cliente['cpf']} | Telefone: {cliente['telefone']} | CEP: {cliente['cep']} | Senha: {cliente['senha']}")
            except json.JSONDecodeError:
                print("Nenhum cliente cadastrado.")
    else:
        print("Nenhum cliente cadastrado.")
    
def excluir_cliente():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                id_excluir = int(input("Digite o ID do cliente que deseja excluir: "))
                dados = [cliente for cliente in dados if cliente['id'] != id_excluir]
                with open(arquivo, "w", encoding="utf-8") as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                print("Cliente excluído com sucesso!")
            except json.JSONDecodeError:
                print("Nenhum cliente cadastrado.")
    else:
        print("Nenhum cliente cadastrado.")

# Menu principal no terminal

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = cadastro()
        salvar_dados(cliente)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        listar_clientes()
    
    elif opcao == "3":
        excluir_cliente()

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")

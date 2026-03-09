from Cadastro_de_produtos import ProdutoEletronico
from Cliente import cadastro, salvar_dados, leitura_de_dados
import json

while True:
    print("\n===MENU PRINCIPAL===")
    print("1. Tela de cadastro")
    print("2. - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = cadastro()
        print("Cliente cadastrado com sucesso!")
    
    elif opcao == "2":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
    
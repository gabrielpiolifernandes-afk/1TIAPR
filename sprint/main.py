# main.py
from funcoes import cadastrar_informacao, listar_informacoes, pesquisar_por_tipo

def menu():
    while True:
        print("\n TOTEM FLEXMEDIA")
        print("1 - Cadastrar informação")
        print("2 - Listar informações cadastradas")
        print("3 - Pesquisar informações por tipo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_informacao()
        elif opcao == "2":
            listar_informacoes()
        elif opcao == "3":
            pesquisar_por_tipo()
        elif opcao == "0":
            print("Encerrando o programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
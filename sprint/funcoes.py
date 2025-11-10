# funcoes.py

# Lista global para armazenar as informações
informacoes = []

def cadastrar_informacao():
    print("\n=== Cadastro de Informação ===")
    
    titulo = input("Digite o título da informação: ")
    while titulo == "":
        print("O título não pode estar vazio!")
        titulo = input("Digite o título da informação: ")

    tipo = input("Digite o tipo (educativo / cultural / lazer): ").lower()
    while tipo != "educativo" and tipo != "cultural" and tipo != "lazer":
        print("Tipo inválido! Digite apenas: educativo, cultural ou lazer.")
        tipo = input("Digite o tipo novamente: ").lower()

    descricao = input("Digite a descrição: ")

    informacao = {
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    }

    informacoes.append(informacao)
    print("Informação cadastrada com sucesso!")


def listar_informacoes():
    print("\n Lista de Informações Cadastradas")
    if len(informacoes) == 0:
        print("Nenhuma informação cadastrada ainda.")
    else:
        for i in range(len(informacoes)):
            info = informacoes[i]
            print("\nInformação", i + 1)
            print("Título:", info["titulo"])
            print("Tipo:", info["tipo"])
            print("Descrição:", info["descricao"])


def pesquisar_por_tipo():
    print("\n=== Pesquisa de Informações por Tipo ===")
    tipo = input("Digite o tipo para pesquisa (educativo / cultural / lazer): ").lower()

    while tipo != "educativo" and tipo != "cultural" and tipo != "lazer":
        print("Tipo inválido! Digite apenas: educativo, cultural ou lazer.")
        tipo = input("Digite o tipo novamente: ").lower()

    encontrados = []
    for info in informacoes:
        if info["tipo"] == tipo:
            encontrados.append(info)

    if len(encontrados) == 0:
        print("Nenhuma informação do tipo", tipo, "foi encontrada.")
    else:
        print("\nInformações do tipo", tipo + ":")
        for info in encontrados:
            print("- " + info["titulo"] + ": " + info["descricao"])

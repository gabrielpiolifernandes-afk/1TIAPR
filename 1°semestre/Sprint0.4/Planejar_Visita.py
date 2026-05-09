import json
import re

arquivo = "artes.json"

# -----------------------------------
# FUNÇÕES AUXILIARES
# -----------------------------------

def extrair_tempo_minutos(texto):
    # Pega o primeiro número da string e retorna como inteiro
    match = re.search(r'\d+', texto)
    if match:
        return int(match.group())
    return 0

def leitor_de_obras():
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo de obras não encontrado")
        return []

# -----------------------------------
# FUNÇÕES DE INTERAÇÃO
# -----------------------------------

def tempo():
    while True:
        print("PLANEJAMENTO DE PASSEIO")
        print("Quanto tempo você tem disponível?\n")
        print("1 - 30 minutos")
        print("2 - 1 hora")
        print("3 - 1 hora e 30 minutos")
        print("4 - 2 horas")
        print("5 - 3 horas")

        escolha = input("Digite o número correspondente à sua escolha: ")

        opcoes_tempo = {
            "1": "30 minutos",
            "2": "1 hora",
            "3": "1 hora e 30 minutos",
            "4": "2 horas",
            "5": "3 horas"
        }

        if escolha in opcoes_tempo:
            return opcoes_tempo[escolha]

        print("Opção inválida. Tente novamente.")

def companhia():
    print("COMPANHIA PARA O PASSEIO")
    print("Com quem você vai visitar o museu?\n")
    print("1 - Sozinho")
    print("2 - Amigos")
    print("3 - Família")
    print("4 - Casal")

    escolha = input("Digite o número correspondente à sua escolha: ")

    mapa_companhia = {
        "1": "sozinho",
        "2": "amigos",
        "3": "família",
        "4": "casal"
    }

    return mapa_companhia.get(escolha, "Opção inválida")

def qual_arte_deseja():
    print("QUAL ARTE DESEJA VISITAR?\n")
    print("1 - Arte Moderna")
    print("2 - Arte Contemporânea")
    print("3 - Arte Europeia")
    print("4 - História do Brasil")
    print("5 - Identidade e Cultura")
    print("6 - Arte Indígena")

    escolha = input("Digite o número correspondente à sua escolha: ")

    mapa_arte = {
        "1": "Arte Moderna",
        "2": "Arte Contemporânea",
        "3": "Arte Europeia",
        "4": "História do Brasil",
        "5": "Identidade e Cultura",
        "6": "Arte Indígena"
    }

    return mapa_arte.get(escolha, "Opção inválida")

# -----------------------------------
# FUNÇÃO PRINCIPAL DE SUGESTÃO DE OBRAS
# -----------------------------------

def obras_por_tempo(tempo_usuario, tema_escolhido):
    tempo_map = {
        "30 minutos": 30,
        "1 hora": 60,
        "1 hora e 30 minutos": 90,
        "2 horas": 120,
        "3 horas": 180
    }
    tempo_total = tempo_map.get(tempo_usuario, 0)

    obras = leitor_de_obras()
    obras_filtradas = [o for o in obras if o["tema"].lower() == tema_escolhido.lower()]

    # Ordenar por tempo da obra (menor primeiro)
    obras_filtradas.sort(key=lambda x: extrair_tempo_minutos(x["tempo"]))

    selecionadas = []
    tempo_acumulado = 0

    for obra in obras_filtradas:
        tempo_obra = extrair_tempo_minutos(obra["tempo"])
        if tempo_acumulado + tempo_obra <= tempo_total:
            selecionadas.append(obra)
            tempo_acumulado += tempo_obra
        if tempo_acumulado == tempo_total:
            break  # não ultrapassar o tempo disponível

    return selecionadas

# -----------------------------------
# FUNÇÃO PRINCIPAL
# -----------------------------------

def main_Planejar_Visita():
    tempo_escolhido = tempo()
    companhia_escolhida = companhia()
    arte_escolhida = qual_arte_deseja()

    print("\nRESUMO DO PASSEIO")
    print(f"Tempo disponível: {tempo_escolhido}")
    print(f"Companhia: {companhia_escolhida}")
    print(f"Arte escolhida: {arte_escolhida}")

    obras_sugeridas = obras_por_tempo(tempo_escolhido, arte_escolhida)
    if obras_sugeridas:
        print("\nObras sugeridas dentro do tempo disponível:")
        for obra in obras_sugeridas:
            print(f"{obra['titulo']} - {obra['tempo']}")
    else:
        print("\nNenhuma obra cabe no tempo selecionado.")

    print("\nObrigado por usar o planejamento de passeio!")

# -----------------------------------
# EXECUÇÃO
# -----------------------------------

if __name__ == "__main__":
    main_Planejar_Visita()
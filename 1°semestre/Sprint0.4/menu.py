import random
import Planejar_Visita  # nome do arquivo com a função main_Planejar_Visita

# =========================================
# MENU PRINCIPAL DO SISTEMA
# =========================================

MENU = [
    {
        "id": 1,
        "titulo": "Planejar Visita",
        "descricao": "Roteiro personalizado em segundos",
        "tipo": "lazer"
    },
    {
        "id": 2,
        "titulo": "Assistente IA",
        "descricao": "Converse sobre arte",
        "tipo": "cultural"
    },
    {
        "id": 3,
        "titulo": "Mapa Interativo",
        "descricao": "Explore cada andar",
        "tipo": "lazer"
    },
    {
        "id": 4,
        "titulo": "Minha Coleção",
        "descricao": "Salve obras favoritas",
        "tipo": "cultural"
    },
    {
        "id": 5,
        "titulo": "Quiz Educativo",
        "descricao": "Quiz nas exposições",
        "tipo": "educativo"
    },
    {
        "id": 6,
        "titulo": "Informações",
        "descricao": "Saiba tudo sobre o MASP",
        "tipo": "educativo"
    },
    {
        "id": 7,
        "titulo": "Dados de Uso",
        "descricao": "Transparência dos seus dados",
        "tipo": "educativo"
    }
]

# =========================================
# MODO VISITANTE
# =========================================

class ModoVisitante:

    def __init__(self, menu):
        self.menu = menu

    # -------------------------------------
    # Mostrar categorias disponíveis
    # -------------------------------------
    def mostrar_interesses(self):
        return [
            "planejar visita",
            "educativo",
            "cultural",
            "lazer"
        ]

    # -------------------------------------
    # Filtrar conteúdos
    # -------------------------------------
    def filtrar_por_tipo(self, tipo):
        resultados = []
        for item in self.menu:
            if item["tipo"] == tipo:
                resultados.append(item)
        return resultados

    # -------------------------------------
    # Recomendação aleatória
    # -------------------------------------
    def recomendar_aleatorio(self, tipo):
        resultados = self.filtrar_por_tipo(tipo)
        if not resultados:
            return None
        return random.choice(resultados)

    # -------------------------------------
    # Primeiro item encontrado
    # -------------------------------------
    def recomendar_primeiro(self, tipo):
        resultados = self.filtrar_por_tipo(tipo)
        if not resultados:
            return None
        return resultados[0]

    # -------------------------------------
    # Fluxo principal do visitante
    # -------------------------------------
    def iniciar(self):
        print("\n================================")
        print(" BEM-VINDO AO GUIA DO MASP ")
        print("================================\n")

        print("Escolha seu interesse:\n")

        interesses = self.mostrar_interesses()
        for i, interesse in enumerate(interesses, start=1):
            print(f"{i} - {interesse.capitalize()}")

        opcao = input("\nDigite uma opção: ")

        # Se a opção for Planejar Visita, chama diretamente a função
        if opcao == "1":
            print("\nRedirecionando para Planejar Visita...\n")
            Planejar_Visita.main_Planejar_Visita()
            return

        # Para outras opções, mantém fluxo normal
        mapa = {
            "2": "cultural",
            "3": "lazer",
            "4": "cultural",
            "5": "educativo",
            "6": "educativo",
            "7": "educativo"
        }

        tipo_escolhido = mapa.get(opcao)
        if not tipo_escolhido:
            print("\nOpção inválida.")
            return

        print(f"\nCategoria escolhida: {tipo_escolhido}\n")

        conteudos = self.filtrar_por_tipo(tipo_escolhido)
        if not conteudos:
            print("Nenhum conteúdo encontrado.")
            return

        print("Conteúdos disponíveis:\n")
        for item in conteudos:
            print(f"[{item['id']}] {item['titulo']}")
            print(f"Descrição: {item['descricao']}\n")

        # ---------------------------------
        # RECOMENDAÇÃO
        # ---------------------------------
        recomendacao = self.recomendar_aleatorio(tipo_escolhido)

        print("================================")
        print(" RECOMENDAÇÃO PARA VOCÊ ")
        print("================================\n")
        print(f"Título: {recomendacao['titulo']}")
        print(f"Descrição: {recomendacao['descricao']}")
        print(f"Categoria: {recomendacao['tipo']}")


# =========================================
# EXECUÇÃO
# =========================================

if __name__ == "__main__":
    sistema = ModoVisitante(MENU)
    sistema.iniciar()
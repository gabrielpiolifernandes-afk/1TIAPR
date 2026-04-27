import random

def monty_hall():
    portas = [1, 2, 3]
    premio = random.choice(portas)

    print("Portas: 1, 2, 3")
    escolha = int(input("Escolha uma porta: "))

    portas_restantes = [p for p in portas if p != escolha and p != premio]
    porta_aberta = random.choice(portas_restantes)

    print(f"O apresentador abriu a porta {porta_aberta} (não tem prêmio).")

    trocar = input("Você quer trocar de porta? (s/n): ").lower()

    if trocar == 's':
        escolha_final = [p for p in portas if p != escolha and p != porta_aberta][0]
    else:
        escolha_final = escolha

    print(f"Sua escolha final: porta {escolha_final}")

    if escolha_final == premio:
        print("Você ganhou O CARRO!")
    else:
        print(f"Você perdeu! O prêmio estava na porta {premio}")


monty_hall()
# Receba a nota de um aluno (0 a 10) e diga se ele foi aprovado (nota ≥ 6) ou reprovado.

lista_de_nota=[4,8,3,10,5,5,8,9,10,1,0]

for notas in lista_de_nota:
    if notas > 6:
        print(f"Voce Passou com {notas} (=")
    elif notas == 6:
        print(f"ficou na risca com {notas}!")
    elif notas == 0:
        print(f"{notas} Talvez estudar não seja pra você")
    else:
        print(f"Você não passou com {notas}, tem que estudar mais!")

#Eu sei que seria mais facil com int(input) mas eu quis tentar usar a lista e for, na minha cabeça eu tinha que puxar as informações da lista pra notas armazenar nas aspas
# e depois passar no if e else mas não consegui ai fui pesquisar e mudei um pouquinho


# lista_de_nota=[4,8,3,10,5,5,8,9,10,1,0]

# for notas in lista_de_nota:
#     notas=()
# if notas > 6:
#     print("Voce Passou (=")
# elif notas == 6:
#     print("Na risca em!")
# elif notas == 0:
#     print("Talvez estudar não seja pra você")
# else:
# print("Você não passou, tem que estudar mais!")
matriz=[
    [1,2],
    [3,4]
]

escalar = 3
resultado=[]

for linha in range(len(matriz)):
    linha_do_resuldato = []
    for coluna in range(len(matriz[linha])):
        linha_do_resuldato.append(matriz[linha][coluna]*escalar)
    resultado.append(linha_do_resuldato)

print(resultado)
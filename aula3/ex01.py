lista=[
    [1,2],
    [3,4]
]

escalar = 3
lista_resultado=[]

for linha in range(len(lista)):
    linha_montar = []
    for coluna in range(len(lista[linha])):
        linha_montar.append(lista[linha][coluna]*escalar)
    lista_resultado.append(linha_montar)

print(lista_resultado)
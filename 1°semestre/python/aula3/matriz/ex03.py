matriz =[
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

validador = True
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if linha == coluna and matriz[linha][coluna] !=1:
            validador= False
            break
        elif linha != coluna and matriz [linha][coluna] !=0:
            validador = False
            break
    if not validador:
        break

if validador:
    print("É identidade")
else:
    print("não é identidade")

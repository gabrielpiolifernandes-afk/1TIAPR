lista = [5,9,7,8,8,0,4]

def media(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma / len(lista)

resultado = media(lista)
print(resultado)
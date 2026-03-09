a=int(input("digite um numero: "))
b=int(input("digite um numero: "))
def soma (a, b):
    return a + b
def subtração (a,b):
    return a-b
def multiplicação (a,b):
    return a*b
def divizão (a,b):
    if b ==0:
        return "erro: divisão por zero"
    else:
        return a/b

resultado = divizão(a,b)
print(resultado)
print("hello word!")
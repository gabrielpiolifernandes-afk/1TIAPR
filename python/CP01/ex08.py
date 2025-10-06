# Solicite um número inteiro e verifique:
# Se ele é par, escreva “Par”.
# Senão, se for múltiplo de 5, escreva “Múltiplo de 5”.
# Caso contrário, escreva “Outro número”.

numero=int(input("Escolha um numero: "))

if numero % 2 == 0:
    print("este numero é par!")
elif numero % 5 == 0:
    print("este numero é múltiplo de 5")
else:
    print("Outro número")


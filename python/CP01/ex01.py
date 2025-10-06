#Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

numero=int(input("escolha um numero:"))

if numero > 0:
    print("O numero é positivo.")
elif numero < 0:
    print("O numero é negativo.")
else:
    print("O numero é zero")
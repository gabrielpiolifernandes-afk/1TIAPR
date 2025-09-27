#Peça dois números inteiros e informe qual deles é maior ou se são iguais.

numero1=int(input("Digite o numero um: "))

numero2=int(input("Digite o numero dois: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior")
elif numero1 == numero2:
    print("Os numeros são iguais")
else:
    print(f"O numero {numero2} é maior")

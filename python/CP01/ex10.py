# Receba dois números inteiros e uma operação (+, -, *, /) digitada pelo usuário. Use if-else para calcular e mostrar o resultado.

# Escolha de numeros
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Escolha se vai ser soma/subtração/vezes/dividido
operacao = input("Digite a operação (+, -, *, /): ")

while operacao not in ["+", "-", "*", "/"]:
    operacao = input("COLOCA CERTO!: ")

# conta
if operacao == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: divisão por zero!")
# Peça ao usuário uma temperatura em graus Celsius e mostre se está:
# Abaixo de 0 → “Congelante”
# Entre 0 e 30 → “Agradável”
# # Acima de 30 → “Quente”

temperatura=float(input("Qual é a temperatura atual em °C?: "))

if temperatura < 0:
    print("congelante")
elif temperatura <= 30:
    print("Agradavel")
else:
    print("Quente")

#professor por algum motivo quando coloco um numero quebrado da erro mesmo colocando float
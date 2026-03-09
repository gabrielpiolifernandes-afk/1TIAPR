import random

lancamentos = 1000
cara = 0
coroa = 0

for i in range(lancamentos):
    resultado = random.randint(0,1)

    if resultado == 0:
        cara += 1
    else:
        coroa += 1

print("Total de lançamentos:", lancamentos)
print("Cara:", cara)
print("Coroa:", coroa)

valores = [cara, coroa]
labels = ["Cara", "Coroa"]

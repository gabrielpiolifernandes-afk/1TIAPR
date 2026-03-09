#Receba o valor de um produto e mostre o preço final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.

valor_do_produto = float(input("Fale o valor do produto: R$ "))

if valor_do_produto > 100:
    desconto = valor_do_produto * 0.10
    valor_final = valor_do_produto - desconto
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Preço final com 10% de desconto: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Preço final: R$ {valor_do_produto:.2f}")
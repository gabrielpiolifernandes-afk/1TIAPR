lista=["maça","banana","laranja", "uva", "pera","abacaxi", "manga","morango"]

with open("frutas.txt","w",encoding="UTF-8")as arquivo:
    for fruta in lista:
        arquivo.write(fruta +"\n")

print("lista salva em frutas.txt")
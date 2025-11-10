#Abre o arquivo no modo de leitura('r')
with open('frutas.txt','r') as file:
    #le todo conteudo do arquivo
    conteudo = file.read()
    print(conteudo)

#Abre o arquivo no modo de leitura ('r')
with open ('frutas.txt', 'r') as file:
    # le a primeira linha do arquivo
    linha1 = file.readline()
    #le a segunda
    linha2 = file.readline()

    linha3 = file.readline()
    print(linha1) 
    print(linha2) 
    print(linha3) 
    
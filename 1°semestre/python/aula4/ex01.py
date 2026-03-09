with open('meuarquivo.txt', 'w', encoding='utf-8') as file:
    file.write('ola mundo!')

with open('meuarquivo.txt', 'r+', encoding= 'utf-8') as file:
    conteudo = file.read()
    file.write('\nEste é um arquivo de texto.')

with open ('meuarquivo.txt', 'a', encoding= 'utf-8') as file:
    file.write('\nCriado por cleitin distruido de nucleo fundido')
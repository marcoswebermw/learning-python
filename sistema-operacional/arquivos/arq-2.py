# Lendo um arquivo e salvando suas linhas em uma lista.
arquivo = open('arquivo.txt', 'r')
# Lista, onde cada elemento representa uma linha do arquivo.
linhas = arquivo.readlines()

for l in linhas:
    print(l)

arquivo.close()
# Lendo um arquivo com 'open'.
# E salvando suas linhas em uma lista.
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for l in linhas:
        print(l)


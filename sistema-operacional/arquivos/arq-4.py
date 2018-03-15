# Abrindo um arquivo com 'open' sem passar o modo de acesso.
# Lendo o arquivo inteiro de uma vez com 'read()'.
# Depois usa o 'split(\n)' para dividir a string em uma lista.
with open('arquivo.txt') as arquivo:
    linhas = arquivo.read().split('\n')
    for l in linhas:
        print(l)
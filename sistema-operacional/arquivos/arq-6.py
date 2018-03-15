# Gravando um fluxo de dados de uma vez com 'writelines()'.
# Os dados sao guardados em sequencia.
with open('times.txt', 'w') as arquivo:
    linhas = ['Spurs\n', 'Warriors\n', 'Cavs\n', 'Rockets']
    arquivo.writelines(linhas)

# Imprimindo o arquivo.
with open('times.txt', 'r') as arquivo:
    for l in arquivo:
        print(l)
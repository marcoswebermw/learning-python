# *-* encoding: utf-8 *-*
# O 'read()' sem parametros le todo o arquivo. Mas pode ler somente
# a quantidade de caracteres ou bytes determinados.
# O 'tell()' indica a posição atual do manipulador de arquivos.
# Lendo apenas 5 caracteres do arquivo.
with open('arquivo.txt', 'r') as arquivo_caractere:
    linha = arquivo_caractere.read(7)
    print('Imprimindo até a posição: {}'.format(arquivo_caractere.tell()))
    print(linha) # Chicago
    print('\n')

# Lendo apenas 5 bytes do arquivo.
with open('arquivo.txt', 'rb') as arquivo_byte:
    linha = arquivo_byte.read(13)
    print('Imprimindo até a posição: {}'.format(arquivo_byte.tell()))
    print(linha) # Chicago Bulls
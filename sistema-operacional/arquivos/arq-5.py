# *-* encoding: utf-8 *-*
# Lendo linha por linha de um arquivo.
# É mais seguro quando o arquivo é muito grande.
# O 'strip()' é usado por segurança para remover espaços no 
# começo e fim da string, além de garantir a remoção do caracter
# de quebra de linha '\n'.
with open('arquivo.txt', 'r') as arquivo:
    linhas = []
    for l in arquivo:
        linhas.append(l.strip())
        print(l)
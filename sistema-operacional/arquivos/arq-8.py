# Para posicionar o manipulador do arquivo em determinada posicao,
# use o 'seek()'. No exemplo abaixo o 'Chicago Bulls' nao sera exibido.
with open('arquivo.txt', 'r') as arquivo:
    arquivo.seek(14)
    for l in arquivo:
        print(l)
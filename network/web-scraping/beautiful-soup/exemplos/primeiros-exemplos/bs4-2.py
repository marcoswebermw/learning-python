from bs4 import BeautifulSoup

with open("index.html","r") as arquivo:
    objeto_arquivo = BeautifulSoup(arquivo)

print(objeto_arquivo)
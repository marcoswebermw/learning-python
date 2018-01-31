from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")  

primeira_ocorrencia = soup.find(text='Stephen Curry')
print(primeira_ocorrencia)
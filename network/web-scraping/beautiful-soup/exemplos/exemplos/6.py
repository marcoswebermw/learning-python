from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")  

primeira_ocorrencia = soup.find('div', attrs={'data-conquistas':'16'})
print(primeira_ocorrencia) # Los Angeles Lakers
from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")  

primeira_ocorrencia = soup.find("ul")
print(primeira_ocorrencia.li.div.string) # San Antonio Spurs
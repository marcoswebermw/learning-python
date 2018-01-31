from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")  

primeira_ocorrencia = soup.find(id="jogadores")
print(primeira_ocorrencia.li.div.string) # Kawai Leonard

primeira_ocorrencia = soup.find(attrs={'data-conquistas':'16'})
print(primeira_ocorrencia) # Los Angeles Lakers

primeira_ocorrencia = soup.find(attrs = {'class':'lista-treinadores'})
print(primeira_ocorrencia.div.string) # Greg Popovich

primeira_ocorrencia = soup.find(class_ = 'lista-times')
print(primeira_ocorrencia.div.string) # San Antonio Spurs
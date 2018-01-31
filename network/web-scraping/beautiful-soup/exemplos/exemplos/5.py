from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")  

def e_o_treinador(tag):
  return tag.has_attr('id') and tag.get('id') == 'treinadores'

primeira_ocorrencia = soup.find(e_o_treinador)
print(primeira_ocorrencia.li.div.string) # Greg Popovich
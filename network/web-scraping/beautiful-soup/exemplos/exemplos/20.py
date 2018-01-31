from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.netflix.com/br/originals"
pagina = urlopen(url)
soup = BeautifulSoup(pagina, "lxml")
pagina.close()

empacotadorTitulos = soup.find("div", class_="originals")
titulos = empacotadorTitulos.find_all("div", class_="original-title")

i = 1

for t in titulos:
    print('{} - Título: {}'.format(i, t.string))
    i += 1



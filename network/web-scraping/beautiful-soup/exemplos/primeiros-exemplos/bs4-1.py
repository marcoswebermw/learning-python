from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.netflix.com/br/originals"
pagina = urlopen(url)
objeto_netflix = BeautifulSoup(pagina)

print(objeto_netflix)
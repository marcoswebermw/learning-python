import re
from bs4 import BeautifulSoup

texto = 'Texto só de teste.'
soup = BeautifulSoup(texto, 'lxml')
minha_regex = re.compile('\w+')
primeira_ocorrencia = soup.find(text=minha_regex)
print(primeira_ocorrencia)
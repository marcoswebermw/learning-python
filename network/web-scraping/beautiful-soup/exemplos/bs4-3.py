from bs4 import BeautifulSoup

minha_string = "<p>Meu XML</p>"
soup = BeautifulSoup(minha_string, 'xml')
print(soup)
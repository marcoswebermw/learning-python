from bs4 import BeautifulSoup

with open('nba.html', 'r') as arq:
    soup = BeautifulSoup(arq, 'lxml')
    resultado = soup.find_all(['ul','li'], recursive=True)
    
    print(resultado)
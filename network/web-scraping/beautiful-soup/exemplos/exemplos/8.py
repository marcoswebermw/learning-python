from bs4 import BeautifulSoup

with open('nba.html', 'r') as arq:
    soup = BeautifulSoup(arq, 'lxml')
    treinadores = soup.find_all(attrs={'class':'lista-treinadores'}, limit=2)
    
    for t in treinadores:
        print(t.div.string, end='\n\n',)

        # VAI IMPRIMIR:
        # Greg Popovich
        # Steve Ker
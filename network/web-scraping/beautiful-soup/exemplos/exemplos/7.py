from bs4 import BeautifulSoup

with open('nba.html', 'r') as arq:
    soup = BeautifulSoup(arq, 'lxml')
    times = soup.find_all(attrs={'class':'lista-times'})

    for t in times:
        print(t.div.string)
        # SERÁ IMPRESSO:
        # San Antonio Spurs
        # Boston Celtics
        # Los Angeles Lakers
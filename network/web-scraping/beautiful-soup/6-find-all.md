## Buscando tudo
  
O `find_all()` é um método que busca todas as ocorrências de um dado valor.  
  
Assim como o `find()` e todos os outros métodos de busca do BeautifulSoup, ele aceita **todos os filtros** que o `find()` aceita.  
  
Ele também aceita o argumento(filtro) `limit` que limita a quantidade de itens buscados. o método `find()` é um `find_all()` com `limit` igual a 1.  
  
> Tanto `find()` quanto `find_all()` podem receber como parâmetro o valor `True`. Nesse caso o `find()` irá retornar a primeira tag do objeto `soup` e o `find_all()`irá retornar todas as tags do objeto `soup`.  
  
```py
from bs4 import BeautifulSoup

with open('nba.html', 'r') as arq:
    soup = BeautifulSoup(arq, 'lxml')
    treinadores = soup.find_all(attrs={'class':'lista-treinadores'}, limit=2)
    
    for t in treinadores:
        print(t.div.string, end='\n\n',)

        # VAI IMPRIMIR:
        # Greg Popovich
        # Steve Ker
```  

### Encontrando todos os ul e li
  
```py
from bs4 import BeautifulSoup

with open('nba.html', 'r') as arq:
    soup = BeautifulSoup(arq, 'lxml')
    resultado = soup.find_all(['ul','li'], recursive=True)
    
    print(resultado)
```  
  
> O `recursive=True` é o padrão(não precisa colocar), e indica que serão pesquisadas na árvore das tags pelas tags filhas, e depois as filhas das filhas, etc.  

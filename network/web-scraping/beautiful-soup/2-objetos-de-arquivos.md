## Objetos Beautiful Soup através de arquivos
  
Arquivos podem ser usados para serem transformados em objetos do Beautiful Soup e assim serem trabalhadas por ele. Este é o método mais comum de se usar o módulo Beautiful Soup.  

Podemos trabalhar com arquivos remotos através de suas urls ou com arquivos locais.  

### Usando Urls  
   
Aqui será usado o módulo `urllib` que é um cliente http para trabalharmos com documentos obtidos através de urls no exemplo. O Beautiful Soup não trabalha diretamente com urls por isso precisamos dos documentos gerados pela `urllib`.   

```py
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.netflix.com/br/originals"
pagina = urlopen(url)
objeto_netflix = BeautifulSoup(pagina)

print(objeto_netflix)
```
  
### Usando arquivos locais
  
Será aberto o arquivo local `index.html` como um objeto do Beautiful Soup e depois será impresso.  
  
```py
from bs4 import BeautifulSoup

with open("index.html","r") as arquivo:
    objeto_arquivo = BeautifulSoup(arquivo)

print(objeto_arquivo)
```
## Search
  
Com a BeatifulSoup é possível buscar algo no documento através de tags, atributos e valores desses atributos em tags ou textos dentro do documento.  
  
Os métodos disponibilizados para tal são:
  
* find()
* find_previous()
* find_next()
* find_all()
* find_all_next()
* find_all_previous()
* find_parent()
* find_parents()
* find_next_sibling()
* find_next_siblings()
* find_previous_sibling()
* find_previous_siblings()
  
### find()
  
O método `find()` busca pela `primeira` ocorrência dentro de um objeto do BeautifilSoup.  
  
```py
from bs4 import BeautifulSoup

with open("nba.html", "r") as arquivo_nba:
    soup = BeautifulSoup(arquivo_nba, "lxml")

primeira_ocorrencia = soup.find("ul")
print(primeira_ocorrencia.li.div.string)
```
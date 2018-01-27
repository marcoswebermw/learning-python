## Find - Encontrando os elementos pais
  
### Encontrando a tag pai com `find_parent()`
  
É possível encontrar, à partir de um elemento, o seu elemento pai e toda estrutura abaixo dele(inclusive esse filho que foi usado para encontrá-lo).  
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>
    <p>
      <a>Link</a>
    </p>
  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_a = soup.find(name='a')
pai = tag_a.find_parent()
# Ou pode ser usado como no comentário abaixo:
# pai = tag_a.find_parent('p')

print(pai)

```
  
```py
## RESULTADO
<p>
  <a>Link</a>
</p>
```
  
### Encontrando as tags pais com `find_parents()`
  
É possível encontrar, à partir de um elemento, o seu elemento pai e os pais dos pais, e assim por diante, até a tag raiz da estrutura.  

O resultado é mostrado de forma recursiva, mostrando do item mais simples(pais imediatos), até toda a estrutura dos pais.   
  
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>
    <p>
      <a>Link</a>
    </p>
  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_a = soup.find(name='a')
pais = tag_a.find_parents()

for tags in pais:
    print(tags, end="\n\n")

```
  
```py
## RESULTADO
<p>
  <a>Link</a>
</p>

<div>
  <p>
    <a>Link</a>
  </p>
</div>

<body>
  <div>
    <p>
      <a>Link</a>
    </p>
  </div>
</body>

<html>
  <body>
    <div>
      <p>
        <a>Link</a>
      </p>
    </div>
  </body>
</html>

<html>
  <body>
    <div>
      <p>
        <a>Link</a>
      </p>
    </div>
  </body>
</html>

```
## Find - Encontrando os elementos irmãos
  
Elementos são considerados irmãos quando estão no mesmo nível na estrutura de árvore.  
  
### find_next_sibling()
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>

    <p id='irmao-1'>
      <a>Link 1</a>
    </p>

    <p id='irmao-2'>
      <a>Link 2</a>
    </p>

    <p id='irmao-3'>
      <a>Link 3</a>
    </p>        

  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.find(name='p')
proximo_irmao = tag_p.find_next_sibling()
print(proximo_irmao)
```
  
```py
## RESULTADO

<p id="irmao-2">
  <a>Link 2</a>
</p>
```
  
### find_next_siblings()
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>

    <p id='irmao-1'>
      <a>Link 1</a>
    </p>

    <p id='irmao-2'>
      <a>Link 2</a>
    </p>

    <p id='irmao-3'>
      <a>Link 3</a>
    </p>        

  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.find(name='p')
irmaos = tag_p.find_next_siblings()

for i in irmaos:
    print(i, end="\n\n")
```
  
```py
## RESULTADO

<p id="irmao-2">
  <a>Link 2</a>
</p>

<p id="irmao-3">
  <a>Link 3</a>
</p>

```  
    
### find_previous_sibling()
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>

    <p id='irmao-1'>
      <a>Link 1</a>
    </p>

    <p id='irmao-2'>
      <a>Link 2</a>
    </p>

    <p id='irmao-3'>
      <a>Link 3</a>
    </p>        

  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.find(id='irmao-2')

irmao_anterior = tag_p.find_previous_sibling()
print(irmao_anterior)
```
  
```py
## RESULTADO

<p id="irmao-1">
  <a>Link 1</a>
</p>
```  
    
### find_previous_siblings()
  
```py
from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>

    <p id='irmao-1'>
      <a>Link 1</a>
    </p>

    <p id='irmao-2'>
      <a>Link 2</a>
    </p>

    <p id='irmao-3'>
      <a>Link 3</a>
    </p>        

  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.find(id='irmao-3')
irmaos = tag_p.find_previous_siblings()

for i in irmaos:
    print(i, end="\n\n")
```  
  
```py
## RESULTADO

<p id="irmao-2">
  <a>Link 2</a>
</p>

<p id="irmao-1">
  <a>Link 1</a>
</p>

```
## Find next and previous
  
BeatifulSoup permite que encontremos o elemento imediatamente anterior, todos os elementos anteriores, somente o elemento posterior, ou todos os elementos posteriores ao elemento selecionado.  
  

### find_next()
  
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
proximo_elemento = tag_p.find_next()
print(proximo_elemento) # <a>Link 1</a>
  

```
    
### find_all_next()
  
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
tag_p = soup.find(id='irmao-1')
proximos_elementos = tag_p.find_all_next()

for p in proximos_elementos:
    print(p)
```  
  
```py
## RESULTADO:

  <a>Link 1</a>

<p id="irmao-2">
  <a>Link 2</a>
</p>

  <a>Link 2</a>

<p id="irmao-3">
  <a>Link 3</a>
</p>

  <a>Link 3</a>
```
  
### find_previous()
  
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
elemento_anterior = tag_p.find_previous()
print(elemento_anterior)
```
  
```py
## RESULTADO: elemento DIV
<div>
  <p id="irmao-1">
    <a>Link 1</a>
  </p>
  <p id="irmao-2">
    <a>Link 2</a>
  </p>
  <p id="irmao-3">
   <a>Link 3</a>
  </p>
</div>

```
      
### find_all_previous()
  
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
tag_p = soup.find(id='irmao-1')
elementos_anteriores = tag_p.find_all_previous()

for a in elementos_anteriores:
    print(a)
```
  
```py
<div>
  <p id="irmao-1">
    <a>Link 1</a>
  </p>
  <p id="irmao-2">
    <a>Link 2</a>
  </p>
  <p id="irmao-3">
    <a>Link 3</a>
  </p>
</div>

<body>
  <div>
    <p id="irmao-1">
      <a>Link 1</a>
    </p>
    <p id="irmao-2">
      <a>Link 2</a>
    </p>
    <p id="irmao-3">
      <a>Link 3</a>
    </p>
  </div>
</body>

<html>
  <body>
    <div>
      <p id="irmao-1">
        <a>Link 1</a>
      </p>
      <p id="irmao-2">
        <a>Link 2</a>
      </p>
      <p id="irmao-3">
        <a>Link 3</a>
      </p>
    </div>
  </body>
</html>
```
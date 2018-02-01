## Formatando a saída
  
O BeautifulSoup permite várias formas de formatar a saída dos documentos por ele trabalhados.  
  
Novamente, para ter uma saída bem formatada e identada, usamos o método `prettify()`.  
  
Para saída não formatada e em texto simples do python, podemos usar o método `str()`, ou o método `encode()` para deixarmos o documento com determinado encoding. E para remover o encoding colocado no documento usamos o `decode()`.  
  

```py
from bs4 import BeautifulSoup

html = "<html><body><div>Olá Mundo!</div><p>&copy;</p></body></html>"

soup = BeautifulSoup(html, "lxml")

# Mostrando formatação simples
print("\nFormatação simples com str():\n")
print(str(soup))
print("\n")

# Mostrando formatação identada com prettify()
print("\nFormatação com prettify:\n")
print(soup.prettify())
print("\n")

# Usando encoding no documento
print("\nEncodando o documento com encode('utf-8'):\n")
print(soup.encode("utf-8"))
print("\n")

# Decodificando o documento
print("\nDecodificando o documento com decode():\n")
print(soup.decode())
print("\n")
  
```
  

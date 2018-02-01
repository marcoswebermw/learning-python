## Encoding no BeautifulSoup
  
O BeautifulSoup usa a biblioteca `UnicodeDammit` para tentar adivinhar automaticamente o encoding da página. Mas é muito comum a detecção errada do mesmo pela biblioteca.  
  
Se soubermos o encoding correto podemos passá-lo para o construtor do BeautifulSoup através do parâmetro `from_encoding`.  
  
Podemos usar para formatação do documento o método `prettify()` e passar o encoding que quisermos para ele se necessário.  
  
Além do `prettify()` existe o método `encode()` que também transforma um documento ou partes dele em um determinado encode que passarmos.  
  
  
```py
from bs4 import BeautifulSoup

# Este texto já foi reconhecido como utf-8. Por isso os erros.
html = """<html>
<head>
 <meta content="text/html;charset=utf-8" http-equiv="Content-
Type"/>
 </head>
<body>
 <div>Olá Mundo</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html5lib", from_encoding="utf-8")

# Mostrando o encoding
print(soup.original_encoding)

# Imprimindo com prettify()
print(soup.prettify())
print("\n")

# Codificando com prettify() com codificação passada.
print(soup.prettify("utf-8"))
print("\n")

# Codificando com encode() com codificação passada.
print(soup.div.encode("utf-8"))
print("\n")
```
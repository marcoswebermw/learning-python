## Tags e NavigableString Object
  
### Tags 
  
Um outro objeto fornecido pela biblioteca é o `Tag`. Ele representa as tags html e xml dos sites em nosso código. Com ele é possível acessar, obter e até modificar valores, atributos e propriedades das tags dos sites.  
  
Essas tags são criadas automaticamente quando invocamos o construtor da biblioteca. Nós só precisamos usar os atributos criados.  
  
As tags são as equivalentes ao html e xml. Os atributos são dicionários e podem ser acessados por suas chaves.  
  
Todos os atributos modificados de uma tag podem ser acessados pela propriedade `attrs`.  
  

### NavigableString Object
  
Ele mantém o texto de dentro de uma tag que pode ser acessado como por exemplo: `minha_tag.string`.  
  
Ele também serve para navegação por tags à partir do texto da tag atual.  
  


### Exemplo
  
```py
from bs4 import BeautifulSoup

meu_html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exemplo</title>
</head>
<body>
    <p>Exemplo do Beautiful Soup</p>
    <a href="#">Meu Link 1</a>
    <a href="#">Meu Link 2</a>
</body>
</html>
"""
soup = BeautifulSoup(meu_html, 'lxml')

tag_paragrafo = soup.p
tag_link_1 = soup.a
tag_link_1['href'] = "http://google.com"

print('Parágrafo <p>: {}'.format(tag_paragrafo))
print('Link 1 <a>: {}'.format(tag_link_1))

print('\n')
print('Atributos modificados de <a>:  {}'.format(tag_link_1.attrs))
print('Texto dentro do parágrafo:  {}'.format(tag_paragrafo.string))
```  
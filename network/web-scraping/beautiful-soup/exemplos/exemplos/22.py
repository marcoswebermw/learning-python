from bs4 import BeautifulSoup

html = """
<html>
 <body>
  <div>
   <ul>
    <li>A</li>
    <li>B</li>
    <li>C</li>
   </ul>
  </div>
 </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")
conteudo = soup.find("ul")

# Imprimindo os filhos
for c in conteudo.contents:
    print(c)

# Imprimindo o tipo dos filhos
print('Tipo de conteúdo: {}'.format(type(conteudo.contents))) # É do tipo 'list'.

# Imprimindo a quantidade de filhos
filhos = []

for f in conteudo.contents:
    if (f == '\n'):  # Removendo caractere '\n'.
        continue
    else:
        filhos.append(f)

print('Quantdidade de filhos: {} filhos'.format(len(filhos))) # div tem 3 filhos.

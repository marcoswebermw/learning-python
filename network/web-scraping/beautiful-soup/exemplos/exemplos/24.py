from bs4 import BeautifulSoup, NavigableString

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
conteudo = soup.find("div")

# Imprimindo o tipo dos filhos
print('Tipo de conteúdo: {}'.format(type(conteudo.descendants))) # É do tipo 'generator'.

# Imprimindo os filhos
i = 1
for c in conteudo.descendants:
    if c != '\n':
        # Verifica se é uma tag ou um valor
        if isinstance(c, NavigableString):
            print('\n{} - É um valor: {}'.format(i,c))
        else:
            print('\n{} - É uma tag: {}'.format(i, c.name))
        i += 1



# Imprimindo a quantidade de filhos
filhos = []

for f in conteudo.descendants:
    if (f == '\n'):  # Removendo caractere '\n'.
        continue
    else:
        filhos.append(f)

print('\nQuantdidade de filhos: {} filhos'.format(len(filhos))) # div tem 7 filhos.
print('\n')

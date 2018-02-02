from bs4 import BeautifulSoup

html = "<html><body><div><p>Parágrafo.<p></div><div><a>Link 1</a><a>Link 2</a></div></body></html>"

soup = BeautifulSoup(html, "lxml")
tag_p = soup.p
tag_a = soup.a

# Removendo uma tag com decompose().
tag_p.decompose()

# Excluindo conteúdo de uma string com extract().
# Também é possível pegar o conteúdo que foi excluído.
conteudo_excluido = tag_a.string.extract()
print(conteudo_excluido)

# Excluindo uma tag com extract().
tag_a.extract()

# Excluindo a tag 'a' dentro da segunda 'div' e também os filhos e conteúdo dela.
# Depois a própria div é removida com o decompose().
soup.find_all("div")[1].clear()
soup.find_all("div")[1].decompose()

# Imprimindo
print('Antes: \n\n {}'.format(html) )
print('\n\nDepois: \n\n {} \n'.format(soup.prettify()) )

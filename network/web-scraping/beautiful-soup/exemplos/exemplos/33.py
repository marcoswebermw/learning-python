from bs4 import BeautifulSoup

html = "<html><body><div></div></body></html>"

soup = BeautifulSoup(html, "lxml")
nova_tag_p = soup.new_tag("p")

# Inserindo o conteúdo de uma tag.
nova_tag_p.string = "Conteúdo do parágrafo."

# Anexando mais conteúdo ao final do conteúdo existente.
nova_tag_p.append("Conteúdo final do parágrafo.")

# Inserindo mais conteúdo no meio do conteúdo existente.
# Além disso será criada uma nova string de forma um pouco diferente.
novo_conteudo = soup.new_string("Conteúdo do meio do parágrafo.")
nova_tag_p.insert(1, novo_conteudo)

# Inserindo a nova tag no documento.
soup.div.insert(0, nova_tag_p)

# Imprimindo
print('Antes: \n\n {}'.format(html) )
print('\n\nDepois: \n\n {} \n'.format(soup.prettify()) )


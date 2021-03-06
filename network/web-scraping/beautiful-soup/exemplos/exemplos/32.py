from bs4 import BeautifulSoup

html = "<html><body><div></div></body></html>"

soup = BeautifulSoup(html, "lxml")

# Adicionando nova tag 'p' através do método 'new_tag()'.
# O único parâmetro obrigatório é o nome da tag, os outros são opcionais.
nova_tag_p = soup.new_tag("p")

# Adicionando atributos posteriormente.
nova_tag_p.attrs={'id':'id_do_p'}

# Adicionando nova tag 'a' já com algumas propriedades.
nova_tag_a = soup.new_tag("a", href="site.com", id="id_de_a")

# Anexando novas tags no documento
soup.div.append(nova_tag_p)
soup.p.append(nova_tag_a)

# Criando nova tag e inserindo em determinada posição.
nova_tag_div = soup.new_tag("div", id="nova_div")
soup.body.insert(1, nova_tag_div)

# Imprimindo
print('Antes: \n\n {}'.format(html) )
print('\n\nDepois: \n\n {} \n'.format(soup.prettify()) )


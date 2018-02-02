from bs4 import BeautifulSoup

html = "<html><body><div>Div do meio</div></body></html>"

soup = BeautifulSoup(html, "lxml")

# insert_before
tag_p = soup.new_tag("p")
tag_p['id'] = "antes-da-div"
tag_p.append("Meu Parágrafo")
tag_div = soup.find("div")
tag_div.insert_before(tag_p)

# insert_after
tag_a =soup.new_tag("a")
tag_a["id"] = "depois-da-div"
tag_a.append("Meu Link")
tag_div.insert_after(tag_a)

# replace_with
tag_a.string.replace_with("Texto Alterado com replace_with. Poderia ser uma tag alterada.")

# wrap
nova_tag_div = soup.new_tag("div")
tag_p.wrap(nova_tag_div)

# unwrap
tag_div.unwrap()

#

# Imprimindo
print('Antes: \n\n {}'.format(html) )
print('\n\nDepois: \n\n {} \n'.format(soup.prettify()) )

from bs4 import BeautifulSoup

html = """
<html>
<body>
<div class="velha" data-info="Alguma Informacao">
<p>Estou dentro da div</p>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html5lib")
div_tag = soup.div

# Alterando a propriedade classe.
div_tag["class"] = "nova_classe"

# Criando a propriedade id.
div_tag["id"] = "id_da_div"

# Deletando a propriedade data-info da div.
# As propriedades são armazenadas em dicionários e no python,
# elementos de dicionários podem ser removidos com o 'del'.
del div_tag["data-info"]

# Exibindo de forma mais organizada como html.
print(div_tag.prettify())
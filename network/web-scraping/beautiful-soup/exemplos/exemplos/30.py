from bs4 import BeautifulSoup

html = """
<html>
<body>
<p>
<li>A</li>
<li>B</li>
<li>C</li>
</p>
</body>
</html>
"""

soup = BeautifulSoup(html, "lxml")
p_tag = soup.p

# Alterando o nome da tag.
p_tag.name = "ul"

# Exibindo de forma mais organizada como html.
print(p_tag.prettify())
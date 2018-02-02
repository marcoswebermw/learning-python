from bs4 import BeautifulSoup

# Este texto já foi reconhecido como utf-8. Por isso os erros.
html = """<html><head><meta content="text/html;charset=utf-8" http-equiv="Content-
Type"/></head><body><div>Olá Mundo</div></body></html>"""

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
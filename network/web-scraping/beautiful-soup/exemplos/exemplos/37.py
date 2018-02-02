from bs4 import BeautifulSoup

# Este texto já foi reconhecido como utf-8. Por isso os erros.
html = "<html><body><div>Olá Mundo</div></body></html>"

soup = BeautifulSoup(html, "html5lib")

# Mostrando o encoding
print(soup.original_encoding)

# Imprimindo com prettify()
print(soup.prettify())
print("\n")

# Imprimindo com prettify() com codificação passada.
print(soup.prettify("utf-8"))
print("\n")

# Imprimindo com encode() com codificação passada.
print(soup.div.encode("utf-8"))
print("\n")
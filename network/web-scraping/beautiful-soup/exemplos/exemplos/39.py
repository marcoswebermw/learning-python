from bs4 import BeautifulSoup

html = "<html><body><div>Olá Mundo!</div><p>&copy;</p></body></html>"

soup = BeautifulSoup(html, "lxml")

# Usando o formatador minimal.
print("\nUsando o formatador minimal:\n")
print(soup.prettify(formatter="minimal"))
print("\n")

# Usando o formatador html.
print("\nUsando o formatador html:\n")
print(soup.prettify(formatter="html"))
print("\n")

# Usando o formatador None.
print("\nUsando o formatador None:\n")
print(soup.prettify(formatter=None))
print("\n")

# Usando uma função.
def caixa_alta(texto):
    return texto.upper()

print("\nUsando o formatador função:\n")
print(soup.prettify(formatter=caixa_alta))
print("\n")

# Removendo o texto do documento.
print("\nRemovendo o texto do documento:\n")
texto = soup.get_text()
print(texto)
print("\n")
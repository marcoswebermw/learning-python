from bs4 import BeautifulSoup

meu_html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Exemplo</title>
</head>
<body>
    <p>Exemplo do Beautiful Soup</p>
    <a href="#">Meu Link 1</a>
    <a href="#">Meu Link 2</a>
</body>
</html>
"""
soup = BeautifulSoup(meu_html, 'lxml')

tag_paragrafo = soup.p
tag_link_1 = soup.a
tag_link_1['href'] = "http://google.com"

print('Parágrafo <p>: {}'.format(tag_paragrafo))
print('Link 1 <a>: {}'.format(tag_link_1))

print('\n')
print('Atributos modificados de <a>:  {}'.format(tag_link_1.attrs))
print('Texto dentro do parágrafo:  {}'.format(tag_paragrafo.string))

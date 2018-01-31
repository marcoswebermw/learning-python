from bs4 import BeautifulSoup

html = """
<html>
 <body>
  <div>
   <ul>
    <li>A</li>
    <li>B</li>
    <li>C</li>
   </ul>
  </div>
 </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")
conteudo = soup.find("ul")

print(conteudo.li.string)
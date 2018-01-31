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

# Removendo caracter '\n' para evitar problemas.
html = html.strip().split()
html = ''.join(html)

soup = BeautifulSoup(html, "lxml")

body = soup.find("body") 

print(body.name)                           # body

print(body.next_element.name)              # div
print(body.next_element.next_element.name) # ul
print(body.next_element.next_element.next_element.name) # li
print(body.next_element.next_element.next_element.next_element) # A

print(body.previous_element.name)  # html
print(body.previous_element.previous_element)  # None

from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>
    <p>
      <a>Link</a>
    </p>
  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_a = soup.find(name='a')
pai = tag_a.find_parent()
# Ou pode ser usado como abaixo
# pai = tag_a.find_parent('p')

print(pai)

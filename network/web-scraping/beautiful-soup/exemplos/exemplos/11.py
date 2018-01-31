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
pais = tag_a.find_parents()

for tags in pais:
    print(tags, end="\n\n")

from bs4 import BeautifulSoup

html = """ 
<html>
<body>
  <div>

    <p id='irmao-1'>
      <a>Link 1</a>
    </p>

    <p id='irmao-2'>
      <a>Link 2</a>
    </p>

    <p id='irmao-3'>
      <a>Link 3</a>
    </p>        

  </div>
</body>
</html>
"""
  
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.find(name='p')
irmaos = tag_p.find_next_siblings()

for i in irmaos:
    print(i, end="\n\n")
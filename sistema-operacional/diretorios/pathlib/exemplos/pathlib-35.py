# Casa o caminho com o padrão dado.
# Retornando 'True' se o padrão corresponder.
# Se o padrão for relativo, o caminho pode ser,
# relativo ou absoluto, e a correspondência é feita
# à partir da direita.
from pathlib import Path

diretorio = Path('.')
print(diretorio.match('*.py')) # False

diretorio = Path('/etc/teste.py')
print(diretorio.match('*.py')) # True

diretorio = Path('etc/teste.py')
print(diretorio.match('*/*.py')) # True

diretorio = Path('etc/teste.py')
print(diretorio.match('/*.py')) # False - Caminho tinha que ser relativo.
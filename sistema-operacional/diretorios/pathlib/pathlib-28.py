# O caminho final do nome do componente, sem o drive ou root.
from pathlib import Path

arquivo = Path('/usr/bin/teste.tar.gz')
print(arquivo.name) # teste.tar.gz
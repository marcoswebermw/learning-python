# Retorna o caminho final("tronco") 
# de um componente sem o sufixo(extensão).
from pathlib import Path

arquivo = Path('/usr/bin/teste.tar.gz')
print(arquivo.stem) # teste.tar

arquivo = Path('/usr/bin/teste.tar')
print(arquivo.stem) # teste
# Junta mais de um componente para formar um caminho.
from pathlib import Path

diretorio = Path('/usr').joinpath('bin')
print(diretorio) # /usr/bin

diretorio = Path('/usr').joinpath('bin', 'teste.tar.gz')
print(diretorio) # /usr/bin/teste.tar.gz
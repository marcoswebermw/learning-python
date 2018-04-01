# Retorna uma versão relativa do caminho dado de acordo com 
# outro caminho passado.
# Se não for possível, 'ValueError' será lançada.
from pathlib import Path

try:
    diretorio = Path('/usr/bin/teste.tar.gz')
    print(diretorio.relative_to('/')) # usr/bin/teste.tar.gz
    print(diretorio.relative_to('/usr')) # bin/teste.tar.gz
    print(diretorio.relative_to('/bin')) # Exceção lançada.
except ValueError as erro:
    print('Não foi possível determinar o caminho relativo.')
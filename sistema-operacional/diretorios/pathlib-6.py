# Retorna o GID(ID do grupo) dono do arquivo.
# 'KeyError' será lançada, se o GID não for encontrado.
from pathlib import Path

diretorio = Path('/etc')

try:
    [print(x.group()) for x in diretorio.iterdir()]
except KeyError as erro:
    print('GID do arquivo não encontrado no sistema.')
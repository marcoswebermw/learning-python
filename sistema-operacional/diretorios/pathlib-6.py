# Retorna o GID(ID do grupo) dono do arquivo.
# 'KeyError' será lançada, se o GID não for encontrado.
from pathlib import Path

diretorio = Path('/etc')

try:
    print("GRUPO ------------->")
    [print(x.group()) for x in diretorio.iterdir()]
except KeyError as erro:
    print('GID do arquivo não encontrado no sistema.')


# Retorna o UID(ID do usuário) dono do arquivo.
# 'KeyError' será lançada, se o UID não for encontrado.
from pathlib import Path

diretorio = Path('/etc')

try:
    print("DONO ------------->")
    [print(x.owner()) for x in diretorio.iterdir()]
except KeyError as erro:
    print('UID do arquivo não encontrado no sistema.')
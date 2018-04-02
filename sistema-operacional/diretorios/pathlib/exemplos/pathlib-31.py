# Retorna uma string de um caminho no estilo posix.
# Ou seja, com a barra "/" para direita.
from pathlib import PureWindowsPath, Path

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.as_posix()) # c:/Documentos/Recentes

# Retorna um caminho como a URI de um arquivo.
# Se o caminho não for absoluto, será lançada 'ValueError'.
try:
    arquivo = Path('/usr/bin/teste.tar.gz')
    print(arquivo.as_uri()) # file:///usr/bin/teste.tar.gz

    arquivo = Path('.')
    print(arquivo.as_uri()) # Exceção lançada.
except ValueError as erro:
    print('O caminho não é absoluto.')
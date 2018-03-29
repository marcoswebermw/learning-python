# Retorna o nome ou letra do drive.
# Em Unix não deve retornar nada.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin')
print(diretorio.drive) # sem retorno

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.drive) # c:
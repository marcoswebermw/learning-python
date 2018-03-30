#  O nó anterior do caminho.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin/test')
print(diretorio.parent) # /usr/bin

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.parent) # c:\Documentos
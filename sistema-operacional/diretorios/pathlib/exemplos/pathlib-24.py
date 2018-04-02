# Retorna o diretório root.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin')
print(diretorio.root) # /

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.root) # \
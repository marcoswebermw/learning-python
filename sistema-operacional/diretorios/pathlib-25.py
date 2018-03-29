# Concatenação do drive e o root.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin')
print(diretorio.anchor) # /

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.anchor) # c:\
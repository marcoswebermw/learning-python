# Uma sequência imultável com todos os nós de um caminho.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin/test')
print(diretorio.parents[0]) # /usr/bin
print(diretorio.parents[1]) # /usr

diretorio = PureWindowsPath('c:\Documentos\Recentes')
print(diretorio.parents[0]) # c:\Documentos
print(diretorio.parents[1]) # c:\
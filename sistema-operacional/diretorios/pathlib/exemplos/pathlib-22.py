# Mostra cada parte que forma o caminho do diretório ou arquivo.
# 'parts()' retorna uma tupla.
# PurePaths podem ser usados idependentes de sistema.
from pathlib import Path, PureWindowsPath

diretorio = Path('/usr/bin')
print(diretorio.parts)

diretorio = PureWindowsPath('c:\program files\gimp')
print(diretorio.parts)
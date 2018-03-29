# Variações do PurePath.
from pathlib import PurePath, Path 
from pathlib import PurePosixPath, PureWindowsPath
from pathlib import WindowsPath, PosixPath

diretorio = Path('/usr/bin')
print(diretorio.parts)

diretorio = PurePath('/usr/bin')
print(diretorio.parts)

diretorio = PurePosixPath('/usr/bin')
print(diretorio.parts)

diretorio = PureWindowsPath('/usr/bin')
print(diretorio.parts)

try:
    diretorio = PosixPath('/usr/bin')
    print(diretorio.parts)
except NotImplementedError as erro:
    print('PoxisPath,não implementado nesse sistema.')


try:
    diretorio = WindowsPath('/usr/bin')
    print(diretorio.parts)
except NotImplementedError as erro:
    print('WindowsPath,não implementado nesse sistema.')
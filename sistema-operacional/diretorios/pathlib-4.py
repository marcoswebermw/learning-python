# Listando só os arquivos de um diretório.
from pathlib import Path

diretorio = Path('.')

[print(x) for x in diretorio.iterdir() if x.is_file()]
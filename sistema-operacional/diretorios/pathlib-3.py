# Outra forma de listar somente subdiretórios.
from pathlib import Path

diretorio = Path('/')

[print(x) for x in diretorio.iterdir() if x.is_dir()]
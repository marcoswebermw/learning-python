# Verificando se é um diretório
from pathlib import Path

diretorio = Path('/')

print('Diretórios e Subdiretórios:\n')
for x in diretorio.iterdir():
    if x.is_dir():
        print(x)
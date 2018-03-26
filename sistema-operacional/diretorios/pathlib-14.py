# Abrindo um arquivo com 'Path.open()'.
# Funciona como a função padrão 'open()' do python.
from pathlib import Path

try:
    arquivo = Path('arquivo.txt')
    with arquivo.open() as a:
        print(a.readline())
except FileNotFoundError as erro:
    print('Arquivo não encontrado.')


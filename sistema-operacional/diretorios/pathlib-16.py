# Renomeia um arquivo.
from pathlib import Path

try:
    arquivo = Path('arquivo.txt')
    arquivo.replace('novo_arquivo.txt')
except FileNotFoundError as erro:
    print('Arquivo ou diretório não encontrado.')
# Listar subdiretórios.
from pathlib import Path

caminho_atual = Path('.')

for subdiretorio in caminho_atual.iterdir():
    print(subdiretorio)
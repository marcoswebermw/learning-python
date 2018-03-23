# Removendo arquivo ou link simbólico.
from pathlib import Path

try:
    # Tentando remover um único arquivo.
    arquivo = Path('arquivo_1.txt')
    arquivo.unlink()

    # Tentando remover vários arquivos de um diretório de uma vez.
    diretorio = Path('.')
    [x.unlink() for x in diretorio.glob('arquivo_?.txt')]
except FileNotFoundError as erro:
    print('Arquivo a ser deletado não existe.')


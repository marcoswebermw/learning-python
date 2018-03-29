# O 'rmdir()' remove diretorios, que somente serao removidos,
# se estiverem vazios.
from pathlib import Path

try:
    diretorio = Path('meu_diretorio')
    diretorio.rmdir()
except FileNotFoundError as error:
    print('Diretório não encontrado')
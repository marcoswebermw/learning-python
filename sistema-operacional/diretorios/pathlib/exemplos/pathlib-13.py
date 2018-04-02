# O 'mkdir' cria novos diretorios.
# Pode ser passado um modo para criacao do diretorio(umask).
# Com 'exist_ok=False' se um arquivo existir será lançada a
# exceção 'FileExistsError'.
# Se o parametro parents for falso(padrão), se houver a criacao,
# em um diretorio pai, e esse diretorio pai nao existir, vai
# ser lancada a excecao FileNotFoundError.
# O umask não está funcionando do jeito que imaginei.
# Depois tenho quer verificar isso.

from pathlib import Path

try:
    diretorio = Path('meu_diretorio')
    diretorio.mkdir()
    diretorio.rmdir()

    diretorio = Path('meu_diretorio/novo_diretorio')
    diretorio.mkdir(mode=111, parents=True, exist_ok=False)

except FileExistsError as erro:
    print('O arquivo {} já existe.'.format(str(diretorio)))
except FileNotFoundError as erro2:
    print('Diretório não encontrado.')
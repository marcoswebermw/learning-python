from pathlib import Path

# Cria arquivo com permissão padrão.
diretorio = Path('arquivo_1.txt')
diretorio.touch()

# Cria arquivo com 'umask' no modo 220.
# Com 'exist_ok=False' se um arquivo existir será lançada a
# exceção 'FileExistsError'.
# O umask não está funcionando do jeito que imaginei.
# Depois tenho quer verificar isso.
try:
    diretorio = Path('arquivo_2.txt')
    diretorio.touch(220, exist_ok=False)
except FileExistsError as error:
    print('O arquivo {} já existe.'.format(str(diretorio)))
# O 'symlink_to' cria um link simbolico para um arquivo ou diretorio.
# Ele recebe um parametro opcional chamado 'target_is_directory=False'.
# Que é ignorado em sistemas unix, mas em sistemas Windows, quando
# se tratar de diretorios deve ter seu valor mudado para 'True'.
from pathlib import Path

try:
    arquivo = Path('meu_arquivo.txt')
    arquivo.touch()
    arquivo.write_text('Arquivo de testes.')

    link_simbolico = Path('meu_link')
    link_simbolico.symlink_to('meu_arquivo.txt')
except FileExistsError as error:
    print('O arquivo já existe.')
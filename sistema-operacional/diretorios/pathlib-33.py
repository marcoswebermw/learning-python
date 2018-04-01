# Retorna um novo caminho com o nome mudado. 
# Se o caminho original não tem um nome 'ValueError' é lançada.
# Aparentemente só retorna um valor, não faz nenhuma alteração.
from pathlib import Path

try:
    arquivo = Path('arquivo')
    print(arquivo.with_name('meu_arquivo')) # meu_arquivo
except ValueError as erro:
    print('Não tem um nome definido.')

# Retorna um novo caminho com o sufixo mudado. 
# Se o caminho original não tem um sufixo, ele será anexado.
# Aparentemente só retorna um valor, não faz nenhuma alteração.
arquivo = Path('./arquivo')
print(arquivo.with_suffix('.txt')) # arquivo.txt
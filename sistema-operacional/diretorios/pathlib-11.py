# 'samefile' indica se um caminho dado aponta para outro.
# O objeto passado como argumento pode ser um objeto 'Path' ou uma string.
# A excecao 'OSError' pode ser lancada se o arquivo nao puder
# ser acessado por qualquer motivo.
from pathlib import Path

caminho = Path('arquivo.txt')
caminho.touch()
resultado = caminho.samefile('arquivo.txt')

print(resultado) # True.


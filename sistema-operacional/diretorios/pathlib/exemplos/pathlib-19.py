# O 'exists()' indica se um arquivo ou diretório existe.
# Se um for um link simbólico, então, indicará se o link
# aponta para um arquivo ou diretório existente.
from pathlib import Path

caminho = Path('/etc')
print(caminho.exists()) # True

caminho = Path('/caminho-falso')
print(caminho.exists()) # False
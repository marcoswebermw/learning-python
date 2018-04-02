# O 'Path.resolve()' transforma um path em um path absoluto.
# Ele resolve qualquer link simbólico, '.', '..', etc. 
# Recebe, opcionalmente, um parâmetro chamado 'strict=False'. 
# Se 'strict' for 'True' e o caminho não existir será lançada
# uma exceção 'FileNotFoundError'.
from pathlib import Path

arquivo = Path('/etc/init.d/..') # /etc
print(arquivo.resolve())

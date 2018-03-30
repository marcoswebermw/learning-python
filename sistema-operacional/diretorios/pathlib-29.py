# O sufixo final do componente.
from pathlib import Path

arquivo = Path('/usr/bin/teste.tar.gz')
print(arquivo.suffix) # .gz

# Lista dos sufixos finais do componente.
arquivo = Path('/usr/bin/teste.tar.gz')
print(arquivo.suffixes) # ['.tar', '.gz']
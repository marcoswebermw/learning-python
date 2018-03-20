# Procurando todos os elementos(incluindo diretórios),
# que correspondem ao padrão dado.
# O '**' representa uma recursão nos subdiretórios.
from pathlib import Path

diretorio = Path('.')

# Procurando arquivos python no diretório.
[print(x) for x in diretorio.glob('*.py')]
print('\n--------------\n')

# Procurando arquivos python incluindo subdiretórios.
[print(x) for x in diretorio.glob('**/*.py')]
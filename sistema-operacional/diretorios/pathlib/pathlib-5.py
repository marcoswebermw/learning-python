# Procurando todos os elementos(incluindo diretórios),
# que correspondem ao padrão dado.
# O '**' representa uma recursão nos subdiretórios.
from pathlib import Path

diretorio = Path('.')

# Procurando arquivos python no diretório.
[print('glob - {}'.format(x)) for x in diretorio.glob('*.py')]
print('\n--------------\n')

# Procurando arquivos python incluindo subdiretórios.
[print('glob recursivo - {}'.format(x)) for x in diretorio.glob('**/*.py')]
print('\n--------------\n')

# O 'rglob' é parecido com o 'glob', com o '**' por padrão.
# Ou seja, o 'rglob' procura arquivos e diretórios 'casando' 
# um padrão, de forma recursiva.

[print('rglob - {}'.format(x)) for x in diretorio.rglob('*.py')]
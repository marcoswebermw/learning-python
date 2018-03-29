# O 'expanduser()' transforma o '~' e o '~user' em sua
# forma absoluta.
from pathlib import Path

diretorio = Path('~/.local/bin/')
expandido = diretorio.expanduser()
print(expandido) # /home/meu-usuario/.local/bin
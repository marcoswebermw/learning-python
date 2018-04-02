# O 'cwd()' retorna o diretório corrente.
# Equivalente ao 'pwd' do sistemas Unix.
from pathlib import Path

diretorio = Path('.')
print(diretorio.cwd())

# O 'home()' retorna o diretório home do usuário.
print(diretorio.home())

# O 'stat()' retorna várias informações sobre o arquivo ou diretório.
# É possível especificar somente a informação requerida.
print(diretorio.stat())
print(diretorio.stat().st_uid)
print(diretorio.stat().st_size)

# O 'chmod()' muda o modo e as permissões do arquivo.
arquivo = Path('arquivo_1.txt')
print(arquivo.stat().st_mode)
arquivo.chmod(0o444)
print(arquivo.stat().st_mode)
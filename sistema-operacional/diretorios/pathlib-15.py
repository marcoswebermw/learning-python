# Renomeia um arquivo ou diretório de forma garantida em Unix-likes. 
# Pode ser uma string ou Path Object.
# Em Unix, as permissoes serao analizadas.
# Talvez, seja melhor usar o 'replace()' para cross-plataforma.
from pathlib import Path

try:
    arquivo = Path('arquivo.txt')
    arquivo.rename('novo_arquivo.txt')
except FileNotFoundError as erro:
    print('Arquivo não encontrado.')
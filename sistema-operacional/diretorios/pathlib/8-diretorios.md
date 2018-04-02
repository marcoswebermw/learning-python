# Trabalhando com Diretórios
  
É possível criar um objeto que represente o caminho com:
  
```py
d = Path('meu_diretorio')
q = d / 'subdiretorio' / 'mais_subdiretorio'
```
  
> A barra '/' funciona como `os.path.join()`. Ou seja, uma espécie de concatenação.
  
- `cwd()` - Retorna o diretório corrente.
  
- `home()` - Retorna o diretório home do usuário.
  
- `mkdir()` - Cria um novo diretório.
  
- `rmdir()` - Remove diretórios vázios.
  
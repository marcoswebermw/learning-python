# Métodos
  
Alguns métodos relacionados aos arquivos e diretórios.
  
- `as_posix()` - Retorna uma string de um caminho no estilo posix.
  
- `as_uri()` - Retorna um caminho como a URI de um arquivo.
  
- `exists()` - Indica se um arquivo ou diretório existe.
  
- `expanduser()` - Transforma o '~' e o '~user' em sua forma  com caminho absoluto.
  
- `iterdir()` - Retorna um iterável(lista) contendo todos os arquivos e subdiretórios do diretório passado.
  
- `joinpath()` - Junta mais de um componente para formar um caminho.
  
- `samefile('caminho')` - Indica se um caminho dado, aponta para outro.
  
- `symlink_to()` - Cria um link simbólico para um diretório ou arquivo.
  
- `relative_to()` - Retorna uma versão relativa do caminho dado de acordo com outro caminho passado.
  
- `rename()` - Renomeia um arquivo ou diretório.
  
- `replace()` - Renomeia um arquivo ou diretório.
  
- `resolve()` - Transforma um path em um path absoluto.
  
- `unlink()` - Remover um arquivo ou link simbólico.
  
- `with_name()` - Retorna um novo caminho com o nome mudado. Se o caminho original não tem um nome 'ValueError' é lançada.
  
- `with_suffix()` - Retorna um novo caminho com o sufixo mudado. Se o caminho original não tem um sufixo, ele será anexado.
  
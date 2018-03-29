## Pathlib
  
O `pathlib` é um módulo que oferece classes que representam um determinado caminho no sistema de arquivos e, que conseguem trabalhar de forma semântica e orientada a objetos de acordo com o sistema operacional usado.
  
Para usar o módulo, que faz parte da biblioteca padrão do Python à partir da versão 3.4, basta importar o módulo desta forma: `import pathlib`.
  
É mais comum importar a classe `Path` do `pathlib` e passar  no construtor, o diretório base para se trabalhar. Ex.: `from pathlib import Path` e depois `diretorio = Path('meu_diretorio')`.
  
### Principais métodos
  
* `iterdir()` - Retorna um iterável(lista) contendo todos os arquivos e subdiretórios do diretório passado.
  
* `is_dir()` - Indica se o elemento passado é um diretório.
  
* `is_file()` - Indica se o elemento passado é um arquivo.
  
* `glob('pattern')` - Procura os elementos que casam com o padrão dado.
  
* `group()` - Retorna o GID(ID do grupo) dono do arquivo.
  
* `touch()` - Cria um arquivo.
  
* `open()` - Abre um arquivo.
  
* `unlink()` - Remover um arquivo ou link simbólico.
  
* `symlink_to()` - Cria um link simbólico para um diretório ou arquivo.
  
* `mkdir()` - Cria um novo diretório.
  
* `rmdir()` - Remove diretórios vázios.
  
* `rename()` - Renomeia um arquivo ou diretório.
  
* `replace()` - Renomeia um arquivo ou diretório.
  
* `resolve()` - Transforma um path em um path absoluto.

* `chmod()` - Muda o modo e as permissões de um arquivo ou diretório.
  
* `stat()` - Retorna várias informações sobre o arquivo ou diretório.
  
* `home()` - Retorna o diretório home do usuário.
  
* `cwd()` - Retorna o diretório corrente.
  
* `exists` - Indica se um arquivo ou diretório existe.
  
* `expanduser()` - Transforma o '~' e o '~user' em sua forma  com caminho absoluto.
  

### Verificando elementos
  
Assim como o `is_dir()` e o `is_file()` que verificam se um elemento é um diretório ou arquivo respectivamente, existem outros métodos para outros elementos.
  
Métodos com função semelhante:
  
- `is_absolute` - Se o caminho é absoluto.  
- `is_block_device` - Se o caminho é um dispositivo de bloco.  
- `is_char_device` - Se o caminho é um dispositivo de caractere.  
- `is_fifo` - Se o caminho é um dispositivo FIFO.  
- `is_reserved` - Se o caminho é um nome reservado pelo sistema.  
- `is_socket` - Se o caminho é um socket.  
- `is_symlink` - Se o caminho é um link simbólico.
  
### Arquivos de texto e binário
  
Também é possível criar e ler arquivos de texto e binário com a `pathlib`.
  
- `write_byte('texto')` - Cria um arquivo em bytes.
- `write_text('texto')` - Cria um arquivo de texto.
- `read_text()` - Lê um arquivo de texto.
- `read_byte()` - Lê um arquivo em bytes.
  
### Referências
  
* [Python Docs](https://docs.python.org/3/library/pathlib.html)  

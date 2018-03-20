## Pathlib
  
O `pathlib` é um módulo que oferece classes que representam um determinado caminho no sistema de arquivos e, que conseguem trabalhar de forma semântica de acordo com o sistema operacional usado.
  
Para usar o módulo, que vem com o python à partir da versão 3.4, basta importar o módulo desta forma: `import pathlib`.
  
É mais comum importar a classe `Path` do `pathlib` e passar  no construtor, o diretório base para se trabalhar. Ex.: `from pathlib import Path` e depois `diretorio = Path('meu_diretorio')`.
  
### Principais métodos
  
* `iterdir()` - Retorna um iterável(lista) contendo todos os arquivos e subdiretórios do diretório passado.
  
* `is_dir()` - Indica se o elemento passado é um diretório.
  
* `is_file()` - Indica se o elemento passado é um arquivo.
  
* `glob('pattern')` - Procura os elementos que casam com o padrão dado.
  
* `group()` - Retorna o GID(ID do grupo) dono do arquivo.
  
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
  

### Referências
  
* [Python Docs](https://docs.python.org/3/library/pathlib.html)  

## Pathlib
  
O `pathlib` é um módulo que oferece classes que representam um determinado caminho(arquivo ou diretório) no sistema de arquivos e, que conseguem trabalhar de forma semântica e orientada a objetos de acordo com o sistema operacional usado.
  
Este módulo é muito parecido com o módulo `os`, porém, com uma implementação bem mais simples, tornando-se bem mais intuitivo de se usar.
  
Para usar o módulo, que faz parte da biblioteca padrão do Python à partir da versão 3.4, basta importar o módulo desta forma: `import pathlib`.
  
É mais comum importar a classe `Path` do `pathlib` e passar  no construtor, o diretório base para se trabalhar. Ex.: `from pathlib import Path` e depois `diretorio = Path('meu_diretorio')`.
  
### PurePaths
  
`PurePaths` são objetos que permitem operações sobre arquivos e diretórios mas que na realidade não acessam o sistema de arquivos diretamente.
  
São úteis quando não queremos que o código tenha acesso ao sistema operacional, ou quando queremos trabalhar com caminhos Unix no Windows ou vice-versa.
  
Podem ser de 3 tipos:
  
* `PurePath('.')` - A classe mais genérica, que se instanciada em Unix será uma `PurePoxisPath('.')` e no Windows uma `PureWindowsPath`.
  
* `PurePoxisPath('.')` - Representa um sistema não-Windows.
  
* `PureWindowsPath('.')` - Representa um sistema Windows.
  
> Essas classes podem ser usadas não importa o sistema operacional porque não fazem chamadas de sistema.
  
Um objeto path é compatível e pode ser usado onde for aceito o `os.PathLike`.
  
### Paths concretos
  
Paths concretos são objetos que permitem operações sobre arquivos e diretórios e acessam o sistema de arquivos diretamente. Fazem uso de system calls.
  
O código terá acesso ao sistema operacional e, só podem trabalhar com seu determinado sistema.
  
Podem ser de 3 tipos: `Path`, `PosixPath` e `WindowsPath`.
  
### Principais propriedades
  
- `parts` - Retorna uma tupla com cada parte que forma o caminho para um arquivo ou diretório.  
- `drive` - Em sistemas Windows retorna o nome ou letra do drive.  
- `root` - Exibe o diretório root.  
- `anchor` - Concatenação do drive e o root.  
- `parents` - Uma sequência imultável com todos os nós de um caminho.  
- `parent` - O nó anterior do caminho.  
- `name` - O caminho final do nome do componente, sem o drive ou root.  
- `suffix` - O sufixo final do componente.  
- `suffixes` - Uma lista dos sufixos do componente.  
- `stem` - Retorna a parte final do caminho(nome) de um componente sem seu sufixo(extensão).  
  
### Principais métodos
  
- `iterdir()` - Retorna um iterável(lista) contendo todos os arquivos e subdiretórios do diretório passado.
  
- `is_dir()` - Indica se o elemento passado é um diretório.
  
- `is_file()` - Indica se o elemento passado é um arquivo.
  
- `glob('pattern')` - Procura os elementos que casam com o padrão dado.
  
- `group()` - Retorna o GID(ID do grupo) dono do arquivo.
  
- `touch()` - Cria um arquivo.
  
- `open()` - Abre um arquivo.
  
- `unlink()` - Remover um arquivo ou link simbólico.
  
- `symlink_to()` - Cria um link simbólico para um diretório ou arquivo.
  
- `mkdir()` - Cria um novo diretório.
  
- `rmdir()` - Remove diretórios vázios.
  
- `rename()` - Renomeia um arquivo ou diretório.
  
- `replace()` - Renomeia um arquivo ou diretório.
  
- `resolve()` - Transforma um path em um path absoluto.

- `chmod()` - Muda o modo e as permissões de um arquivo ou diretório.
  
- `lchmod()` - O mesmo que o `chmod()`, mas se for um link simbólico, ele apontará para o objteto original.
  
- `stat()` - Retorna várias informações sobre o arquivo ou diretório.
  
- `lstat()` - O mesmo que o `stat`, mas se for um link simbólico, ele apontará para o objeto original.
  
- `exists` - Indica se um arquivo ou diretório existe.
  
- `expanduser()` - Transforma o '~' e o '~user' em sua forma  com caminho absoluto.
  
- `as_posix()` - Retorna uma string de um caminho no estilo posix.
  
- `as_uri()` - Retorna um caminho como a URI de um arquivo.
  
- `joinpath()` - Junta mais de um componente para formar um caminho.
  
- `with_name()` - Retorna um novo caminho com o nome mudado. Se o caminho original não tem um nome 'ValueError' é lançada.
  
- `with_suffix()` - Retorna um novo caminho com o sufixo mudado. Se o caminho original não tem um sufixo, ele será anexado.
  
- `relative_to()` - Retorna uma versão relativa do caminho dado de acordo com outro caminho passado.
  
- `match()` - Casa o caminho com o padrão dado.

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
  
### Navegando pelos diretórios
  
É possível criar um objeto que represente o caminho com:
  
```py
d = Path('meu_diretorio')
q = d / 'subdiretorio' / 'mais_subdiretorio'
```
  
> A barra '/' funciona como `os.path.join()`.
  
- `home()` - Retorna o diretório home do usuário.
  
- `cwd()` - Retorna o diretório corrente.

### Referências
  
* [Python Docs](https://docs.python.org/3/library/pathlib.html)  

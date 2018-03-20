## Pathlib
  
O `pathlib` é um módulo que oferece classes que representam um determinado caminho no sistema de arquivos e, que conseguem trabalhar de forma semântica de acordo com o sistema operacional usado.
  
Para usar o módulo, que vem com o python à partir da versão 3.4, basta importar o módulo desta forma: `import pathlib`.
  
É mais comum importar a classe `Path` do `pathlib` e passar  no construtor, o diretório base para se trabalhar. Ex.: `from pathlib import Path` e depois `diretorio = Path('meu_diretorio')`.
  
### Principais métodos
  
* `iterdir()` - Retorna um iterável(lista) contendo todos os arquivos e subdiretórios do diretório passado.
  
* `is_dir()` - Indica se o elemento passado é um diretório.
  

### Referências
  
* [Python Docs](https://docs.python.org/3/library/pathlib.html)  

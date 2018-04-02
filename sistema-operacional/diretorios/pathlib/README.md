# Pathlib
  
O `pathlib` é um módulo que oferece classes que representam um determinado caminho(arquivo ou diretório) no sistema de arquivos e, que conseguem trabalhar de forma semântica e orientada a objetos de acordo com o sistema operacional usado.
  
Este módulo é muito parecido com o módulo `os`, porém, com uma implementação bem mais simples, tornando-se bem mais intuitivo de se usar.
  
Para usar o módulo, que faz parte da biblioteca padrão do Python à partir da versão 3.4, basta importar o módulo desta forma: `import pathlib`.
  
É mais comum importar a classe `Path` do `pathlib` e passar  no construtor, o diretório base para se trabalhar. Ex.: `from pathlib import Path` e depois `diretorio = Path('meu_diretorio')`.
  
### Referências
  
* [Python Docs](https://docs.python.org/3/library/pathlib.html) 

# PurePaths
  
`PurePaths` são objetos que permitem operações sobre arquivos e diretórios mas que na realidade `não acessam` o sistema de arquivos diretamente.
  
São úteis quando não queremos que o código tenha acesso ao sistema operacional, ou quando queremos trabalhar com caminhos Unix no Windows ou vice-versa.
  
Podem ser de 3 tipos:
  
* `PurePath('.')` - A classe mais genérica, que se instanciada em Unix será uma `PurePoxisPath('.')` e no Windows uma `PureWindowsPath`.
  
* `PurePoxisPath('.')` - Representa um sistema não-Windows.
  
* `PureWindowsPath('.')` - Representa um sistema Windows.
  
> Essas classes podem ser usadas não importa o sistema operacional porque não fazem chamadas de sistema.
  
Um objeto path é compatível e pode ser usado onde for aceito o `os.PathLike`.
  
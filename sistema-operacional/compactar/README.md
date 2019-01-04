# Módulo ZipFile  

O módulo `zipfile` comprime e extrai arquivos de forma individual ou vários arquivos de uma vez.  

## Compactando Arquivo  

O `ZIP_DEFLATED` é o método mais seguro e compatível de compressão. Também existe os modos mais novos `BZIP2` e `LZMA`.  

O `path` do arquivo ou diretório tem que ser escrito de acordo com o sistema operacional.  

```py
import zipfile

# Nome do arquivo compactado a ser criado, e modo de escrita.
arq_compactado = zipfile.ZipFile('compactado.zip','w')
arq_compactado_bzip2 = zipfile.ZipFile('compactado_bzip2.zip','w')
arq_compactado_lzma = zipfile.ZipFile('compactado_lzma.zip','w')

# Gravando arquivos.
arq_compactado.write('arq.txt', compress_type=zipfile.ZIP_DEFLATED)
arq_compactado_bzip2.write('arq.txt', compress_type=zipfile.ZIP_BZIP2)
arq_compactado_lzma.write('arq.txt', compress_type=zipfile.ZIP_LZMA)

# Fechando recurso.
arq_compactado.close()
arq_compactado_bzip2.close()
arq_compactado_lzma.close()
```  

## Referências  

[code.tutsplus.com](https://code.tutsplus.com/pt/tutorials/compressing-and-extracting-files-in-python--cms-26816)  
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

# Fechando recursos.
arq_compactado.close()
arq_compactado_bzip2.close()
arq_compactado_lzma.close()
```  

## Extraindo Arquivo  

```py
import zipfile

# Nome do arquivo zipado.
zipado = 'compactado.zip'
# Nome do arquivo que será extraído.
extrair = 'arq.txt'
# Nome do diretório de destino do conteúdo extraído.
destino = '/tmp/extraido/'


# Definindo o arquivo zip a ser trabalhado(ou criado).
arq_compactado = zipfile.ZipFile(zipado)

# Extraindo arquivo.
arq_compactado.extract(extrair, destino)

# Fechando recursos.
arq_compactado.close()
```  

## Empacotando vários arquivos  

```py
import zipfile

# Será usado para renomear o 'arq3.txt'.
novo_nome = 'arq3_renomeado.txt'

arq_compactado = zipfile.ZipFile('compactando_varios.zip', 'w')

arq_compactado.write('arq.txt', compress_type=zipfile.ZIP_DEFLATED)
arq_compactado.write('arq2.txt', compress_type=zipfile.ZIP_DEFLATED)
# O segundo parâmetro é opcional. Serve para renomear o arquivo dentro do pacote.
arq_compactado.write('arq3.txt', novo_nome,compress_type=zipfile.ZIP_DEFLATED)

arq_compactado.close()
```  

## Extraindo vários arquivos de um pacote  

```py
# Extraindo no diretório atual
import zipfile

arq_compactado = zipfile.ZipFile('compactando_varios.zip')
arq_compactado.extractall()
arq_compactado.close()
```  

```py
# Extraindo em um diretório selecionado.
import zipfile

arq_compactado = zipfile.ZipFile('compactando_varios.zip')
arq_compactado.extractall('/tmp/varios_arquivos_extraidos/')
arq_compactado.close()
```  

## Referências  

[code.tutsplus.com](https://code.tutsplus.com/pt/tutorials/compressing-and-extracting-files-in-python--cms-26816)  
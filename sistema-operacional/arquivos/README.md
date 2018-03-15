## Arquivos em Python
  
Arquivos podem ser trabalhados de forma simples em Python com o método `open`.
  
Sempre feche um arquivo para liberar recursos do sistema.
  
Use o `read` somente em arquivos pequenos. Pois o arquivo será carregado inteiramente na memória. Arquivos muito grande consumiram muitos recursos da máquina com o uso do `read`. Se o arquivo for grande carregue linha por linha ou por pedaços e, vá processando as partes aos poucos.
  
### Modos de acesso aos arquivos
  
Arquivos podem ser acessados de algumas formas.
  
* r  - Leitura de caracteres;  
* rb - Leitura de Bytes;  
* r+ - Leitura e escrita;  
* w  - Escrita ou sobrescrita;  
* a  - Anexar ao final.  
  
> Se não for informado o modo, será adotado por padrão o modo `r`.
  
### Algumas funções para trabalhar com arquivos
  
* read() - Lê todo o arquivo dentro de uma string.  
* write() - Escreve dados no arquivo;  
* readlines() - Retorna uma lista com todas as linhas do arquivo;  
* writelines() - Escreve um fluxo de uma vez(como uma lista);  
* tell() - Informa a posição do manipulador de arquivos no arquivo;  
* seek() - Posiciona o manipulador de arquivos em determinada posição;  
  
Use o método `split()` em conjunto com o `read()` para conseguir obter uma lista, onde com cada elemento dela é uma linha do arquivo. Funcionaria de forma semelhante ao `readlines()`;
  
Ao carregar um arquivo aos poucos(linha por linha), geralmente, o caracter de quebra de linha é removido automaticamente. Mas, por segurança sempre use o método `strip()`.
  


### Escrevendo em um arquivo
  
```py
arquivo = open('arquivo.txt', 'w')
arquivo.write('Chicago Bulls\nBoston Celtics\nLos Angeles Lakers')
arquivo.close()
```
  
### Abrindo um arquivo
  
Um arquivo sempre tem que ser fechado depois de aberto.
  
```py
arquivo = open('arquivo.txt', 'r')
# Lista, onde cada elemento representa uma linha do arquivo.
linhas = arquivo.readlines()

for l in linhas:
    print(l)

arquivo.close()
```
  
### Abrindo um arquivo com `with`
  
Uma forma mais elegante de abrir um arquivo é usar o gerenciador de contexto `with`. Com ele fica mais fácil manipular um arquivo e, depois que o bloco dele for finalizado, o arquivo é fechado automaticamente.
  
```py
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for l in linhas:
        print(l)
```
  
### Lendo um arquivo grande linha por linha
  
```py
with open('arquivo.txt', 'r') as arquivo:
    linhas = []
    for l in arquivo:
        linhas.append(l.strip())
        print(l)
```
  
### Escrevendo um fluxo de dados de uma vez
  
```py
with open('times.txt', 'w') as arquivo:
    linhas = ['Spurs\n', 'Warriors\n', 'Cavs\n', 'Rockets']
    arquivo.writelines(linhas)

# Imprimindo o arquivo.
with open('times.txt', 'r') as arquivo:
    for l in arquivo:
        print(l)
```
  
### Lendo determinada quantidade de caracteres ou bytes
  
O `read()` sem parâmetros lê todo o arquivo. Mas pode ler somente a quantidade de caracteres ou bytes, determinados pelo valor do parâmetro passado a ele.
  
O `tell()` indica a posição atual do manipulador de arquivos.
  
### Lendo apenas 5 caracteres do arquivo.
  
```py
with open('arquivo.txt', 'r') as arquivo_caractere:
    linha = arquivo_caractere.read(7)
    print('Imprimindo até a posição: {}'.format(arquivo_caractere.tell()))
    print(linha) # Chicago
    print('\n')

# Lendo apenas 5 bytes do arquivo.
with open('arquivo.txt', 'rb') as arquivo_byte:
    linha = arquivo_byte.read(13)
    print('Imprimindo até a posição: {}'.format(arquivo_byte.tell()))
    print(linha) # Chicago Bulls
```
  
### Posicionando o começo de leitura
  
Para posicionar o manipulador do arquivo em determinada posicão, use o `seek()`. No exemplo abaixo o 'Chicago Bulls' não será exibido.
  
```py
with open('arquivo.txt', 'r') as arquivo:
    arquivo.seek(14)
    for l in arquivo:
        print(l) 
        # Boston Celtics
        # Los Angeles Lakers
```
# SQLITE
  
Não é um SGBD. É uma biblioteca escrita em C que implementa um banco de dados SQL embutido. Ela mesma faz o papel de servidor. Muito usada em pequenas aplicações, dispositivos embarcados testes etc.

O Sqlite, à partir do python3, já vem com o python, e é usado através do módulo `sqlite3`.  

Existe a opção de usar o sqlite em memória, ao invés de arquivo, o que facilita em testes. Isso pode ser feito com o parâmetro `:memory:` como em: `sqlite3.connect(':memory:')`.  

## Criando nova conexão
  
Cria uma conexão, e cria o arquivo do banco caso não exista.  

```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
print('Conexão Criada')
```
  
## Criando tabelas
  
```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = "CREATE TABLE time (jogador text, numero int)"
cursor.execute(sql)
conexao.close()
```
  
## Inserindo dados
  
```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()

# Inserindo de forma simples.
cursor.execute("INSERT INTO time VALUES('{}',{})".format(
             'Stephen Curry', 30))

# Inserindo vários elementos.
sql = "INSERT INTO time VALUES(?,?)"
jogadores = [('Lebrom James', 23), 
             ('Russel Westbrook', 0),
             ('Kevin Durant', 35)]
cursor.executemany(sql, jogadores)

# Commitando os dados no banco             
conexao.commit() 
conexao.close()
```
  
## Visualizando os dados
  
```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = "SELECT nome, numero FROM jogador"
cursor.execute(sql)

for c in cursor:
    print('Jogador: {}, Camisa Nº: {}'.format(c[0], c[1]))

conexao.close()
```
  
## Atualizando dados
  
```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = """UPDATE jogador 
         SET nome = 'Michael Jordan' 
         WHERE numero = 23"""
cursor.execute(sql)
conexao.commit()
conexao.close()
```
  
## Removendo dados
  
```py
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = """DELETE FROM jogador 
         WHERE nome = '{}'""".format('Kevin Durant')
cursor.execute(sql)
conexao.commit()
conexao.close()
```
  
## Referências
  
* [Sqlite.org](https://www.sqlite.org/index.html)  
* [Python Tips](https://pythontips.com/2013/08/01/connecting-to-sqlite-databases/)  
* [Wikipédia](https://pt.wikipedia.org/wiki/SQLite)  
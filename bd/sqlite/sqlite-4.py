# Inserindo dados
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()

# Inserindo de forma simples.
cursor.execute("INSERT INTO jogador VALUES('{}',{})".format(
             'Stephen Curry', 30))

# Inserindo vários elementos.
# E também evitando SQL Injection.
sql = "INSERT INTO jogador VALUES(?,?)"
jogadores = [('Lebron James', 23), 
             ('Russel Westbrook', 0),
             ('Kevin Durant', 35)]
cursor.executemany(sql, jogadores)

# Commitando os dados no banco             
conexao.commit() 
conexao.close()
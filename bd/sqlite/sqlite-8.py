# Executando o exemplo completo com o banco em memória(sem arquivo).
import sqlite3
conexao = sqlite3.connect(':memory:')
cursor = conexao.cursor()

# Cria tabela.
sql = "CREATE TABLE jogador (nome text, numero int)"
cursor.execute(sql)

# Inserindo vários elementos.
# E também evitando SQL Injection.
sql = "INSERT INTO jogador VALUES(?,?)"
jogadores = [('Lebron James', 23), 
             ('Russel Westbrook', 0),
             ('Kevin Durant', 35),
             ('Stephen Curry', 30)]
cursor.executemany(sql, jogadores)
# Commitando os dados no banco.
conexao.commit() 

# Alterando dados.
sql = """UPDATE jogador 
         SET nome = '{}' 
         WHERE numero = 23""".format('Michael Jordan')
cursor.execute(sql)
conexao.commit()

# Removendo dados.
sql = """DELETE FROM jogador 
         WHERE nome = '{}'""".format('Kevin Durant')
cursor.execute(sql)
conexao.commit()

# Consultando dados.
sql = "SELECT nome, numero FROM jogador"
cursor.execute(sql)

for c in cursor:
    print('Jogador: {}, Camisa Nº: {}'.format(c[0], c[1]))


# Fechando conexão.
conexao.close()
# Atualizando dados
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = """UPDATE jogador 
         SET nome = '{}' 
         WHERE numero = 23""".format('Michael Jordan')
cursor.execute(sql)
conexao.commit()
conexao.close()
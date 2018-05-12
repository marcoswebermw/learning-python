# Removendo dados
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = """DELETE FROM jogador 
         WHERE nome = '{}'""".format('Kevin Durant')
cursor.execute(sql)
conexao.commit()
conexao.close()
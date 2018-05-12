# Criando tabelas
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = "CREATE TABLE jogador (nome text, numero int)"
cursor.execute(sql)

conexao.close()

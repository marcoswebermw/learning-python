# Criando tabelas de forma alternativa.
import sqlite3
with (sqlite3.connect('meu_bd.db')) as conexao:
    sql = "CREATE TABLE jogador (nome text, numero int)"
    cursor = conexao.cursor()
    cursor.execute(sql)
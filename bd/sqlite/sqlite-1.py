# Conexão
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
print('Conexão Criada')
conexao.close()
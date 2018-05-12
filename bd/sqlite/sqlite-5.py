# Visualizando os dados
import sqlite3
conexao = sqlite3.connect('meu_bd.db')
cursor = conexao.cursor()
sql = "SELECT nome, numero FROM jogador"
cursor.execute(sql)

for c in cursor:
    print('Jogador: {}, Camisa Nº: {}'.format(c[0], c[1]))

conexao.close()
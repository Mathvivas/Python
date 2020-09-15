import sqlite3

dados = [
        ('João',    '8901-0109'),
        ('André',   '8902-8900'),
        ('Maria',   '7891-3321')
        ]

conexão = sqlite3.connect('Agenda.pdf')
cursor = conexão.cursor()

cursor.execute('create table agenda(Nome text, Telefone text)')

cursor.executemany('''insert into agenda(Nome, Telefone) values(?, ?)''', dados)

conexão.commit()
cursor.close()
conexão.close()

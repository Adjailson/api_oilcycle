import sqlite3 as db
# Configurando o banco de dados SQLite
DATABASE = "oilcycle.db"

class Database:

    def __init__(self):
        self.conn = db.connect("models/database/"+DATABASE)
        #self.criarTabelas()#Depois do banco criado podemos comentar essa linha

    def conectar(self):
        return db.connect("models/database/"+DATABASE)

    #Criar todas as tabelas necessárias
    def criarTabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS serie (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ano INTEGER NOT NULL,
                versao FLOAT NOT NULL,
                modelo VARCHAR(5) NOT NULL
            )
        ''')
        
        #Outras tabelas:

        # Ao terminar:
        self.conn.commit()
        self.conn.close()

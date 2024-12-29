import sqlite3 as db
# Configurando o banco de dados SQLite
DATABASE = "oilcycle.db"

class Database:

    def __init__(self):
        self.conn = db.connect("models/database/"+DATABASE)
        self.criarTabelas()#Depois do banco criado podemos comentar essa linha

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
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS maquina (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo VARCHAR(10) NOT NULL,
                on_off INTEGER(1) NOT NULL,
                nivel_oleo INTEGER(3) NOT NULL,
                temperatura_oleo INTEGER(3) NOT NULL,
                nivel_agua INTEGER(3) NOT NULL,
                nivel_detegente INTEGER(3) NOT NULL,
                contem_soda INTEGER(1) NOT NULL,
                status_motor INTEGER(1) NOT NULL,
                temporizador INTEGER(3) NOT NULL
            )
        ''')
        # Ao terminar:
        self.conn.commit()

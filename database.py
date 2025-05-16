import sqlite3

def criar_tabela():
    conn = sqlite3.connect('fake_db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudantes (
            matricula TEXT PRIMARY KEY,
            pontos INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Executar só uma vez para criar o banco
if __name__ == '__main__':
    criar_tabela()

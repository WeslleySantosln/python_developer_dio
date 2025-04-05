import mysql.connector
from config import DB_CONFIG

class DatabaseHandler:

    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.valor_chave = 10

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `keys` (  -- Usando backticks ao redor de 'keys'
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                key_value VARCHAR(255) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
        

    def insert_key(self, user_id, key_value):

        try:

            self.cursor.execute("SELECT key_value FROM `keys` WHERE key_value = %s", (key_value,))
            if self.cursor.fetchone():
                return False, "Chave já existe"
            
            self.cursor.execute("INSERT INTO `keys` (user_id, key_value) VALUES (%s, %s)", (user_id, key_value))

            self.conn.commit()

            return True, "Chave inserida com sucesso"
        
        except mysql.connector.Error as e:

            return False, f"Erro ao inserir chave: {e}"

    def get_keys(self, user_id):

        
        self.cursor.execute("SELECT key_value, created_at, %s FROM `keys` WHERE user_id = %s", (self.valor_chave, user_id))
        return self.cursor.fetchall()

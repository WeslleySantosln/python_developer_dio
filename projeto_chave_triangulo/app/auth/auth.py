import mysql.connector
import hashlib
from app.database.database import DatabaseHandler

class Auth:
    def __init__(self):
        self.db = DatabaseHandler()

    def hash_password(self, password):
        """Cria um hash SHA-256 para a senha"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Registra um novo usuário no banco de dados"""
        hashed_password = self.hash_password(password)
        
        # Verificar se o nome de usuário já existe
        self.db.cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if self.db.cursor.fetchone():
            return False, "Nome de usuário já existe."
        
        try:
            self.db.cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            self.db.conn.commit()
            return True, "Usuário cadastrado com sucesso!"
        except mysql.connector.Error as err:
            return False, f"Erro ao cadastrar usuário: {err}"

    def login(self, username, password):

        """Verifica as credenciais do usuário"""
        hashed_password = self.hash_password(password)
        self.db.cursor.execute(
            "SELECT id FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        user = self.db.cursor.fetchone()
        
        if user:
            return True, "Login realizado com sucesso!", user[0]
        return False, "Usuário ou senha incorretos", None

    def __del__(self):
        """Garante que a conexão com o banco de dados seja fechada ao final"""
        self.db.close()

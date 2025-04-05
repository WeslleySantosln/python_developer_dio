import unittest
from app.auth.auth import Auth
from app.database.database import DatabaseHandler

class TestAuth(unittest.TestCase):

    def setUp(self):
        """Configuração antes de cada teste"""
        self.auth = Auth()
        self.db = DatabaseHandler()

    def tearDown(self):
        """Limpeza após cada teste"""
        self.db.cursor.execute("DELETE FROM users")  # Limpar dados após cada teste
        self.db.conn.commit()

    def test_register_user(self):
        """Testa o registro de um novo usuário"""
        result, message = self.auth.register_user('testuser', 'testpassword')
        self.assertTrue(result)
        self.assertEqual(message, "Usuário cadastrado com sucesso!")

    def test_register_user_duplicate(self):
        """Testa a tentativa de registrar um usuário com nome duplicado"""
        self.auth.register_user('testuser', 'testpassword')
        result, message = self.auth.register_user('testuser', 'newpassword')
        self.assertFalse(result)
        self.assertEqual(message, "Nome de usuário já existe.")

    def test_login_success(self):
        """Testa o login com credenciais corretas"""
        self.auth.register_user('testuser', 'testpassword')
        result, message, user_id = self.auth.login('testuser', 'testpassword')
        self.assertTrue(result)
        self.assertEqual(message, "Login realizado com sucesso!")
        self.assertIsNotNone(user_id)

    def test_login_failure(self):
        """Testa o login com credenciais incorretas"""
        self.auth.register_user('testuser', 'testpassword')
        result, message, user_id = self.auth.login('testuser', 'wrongpassword')
        self.assertFalse(result)
        self.assertEqual(message, "Usuário ou senha incorretos")
        self.assertIsNone(user_id)

    def test_invalid_username(self):
        """Testa o login com um nome de usuário inválido"""
        self.auth.register_user('testuser', 'testpassword')
        result, message, user_id = self.auth.login('invaliduser', 'testpassword')
        self.assertFalse(result)
        self.assertEqual(message, "Usuário ou senha incorretos")
        self.assertIsNone(user_id)

if __name__ == '__main__':
    unittest.main()

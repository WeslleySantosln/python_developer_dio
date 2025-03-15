import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost',
}

db_name = 'triangle_db'


def create_database():
    cursor = None  # Inicializa o cursor fora do bloco try para evitar o erro UnboundLocalError
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()  # Corrigido para cursor() e não curso()
        
        # Tente criar o banco de dados
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f'Banco de dados {db_name} criado com sucesso!')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"O banco de dados '{db_name}' já existe.")
        else:
            print(f"Erro ao criar o banco de dados: {err}")
    finally:
        if cursor:
            cursor.close()  # Verifique se o cursor foi realmente criado
        if connection:
            connection.close()  # Verifique se a conexão foi estabelecida


def create_table_one():
    cursor = None  # Inicializa o cursor fora do bloco try para evitar o erro UnboundLocalError
    try:
        # Adicionar db_name para se conectar ao banco correto
        config['database'] = db_name
        
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()  # Corrigido para cursor() e não curso()
    
        # Tente criar as tabelas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS keys (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                key_value VARCHAR(255) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        
        connection.commit()
        print("Tabelas criadas com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao criar as tabelas: {err}")

    finally:
        if cursor:
            cursor.close()  # Verifique se o cursor foi realmente criado
        if connection:
            connection.close()  # Verifique se a conexão foi estabelecida


if __name__ == "__main__":

    # create_database()    
    # create_table_one()
    print("Operação concluída.")

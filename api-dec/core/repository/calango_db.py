import sqlite3

# NOME DO BANCO
DB_NAME = 'db_calango_sec'

# NOMES DAS TABELAS
USERS = 'tb_users'
AUTH = 'tb_auth'


class CalangoDatabase:

    def __connection(self):
        print("Iniciando conexão")
        return self.__conn

    def close(self):
        print("Fechando conexão")
        self.__conn.close()

    # CRIAÇÃO DO BANCO E TABELAS
    def create_tables(self):
        try:
            cursor = self.__connection().cursor()

            cursor.execute(
                """
                CREATE TABLE tb_users (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL,
                    username TEXT NOT NULL, 
                    password TEXT NOT NULL
                );
                """
            )

            cursor.execute(
                """
                CREATE TABLE tb_auth (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    expiry_at TEXT,
                    token DATETIME NOT NULL,

                    FOREIGN KEY(user_id) REFERENCES tb_users(id)
                );
                """
            )

            print("Tabelas criadas com sucesso")

        except Exception as e:
            print(f'Erro ao criar tabelas: {e}')

        self.close()

    def execute_query(self, query: str = ''):

        if query == '':
            return

        print(query)

        conn = self.__connection()

        data = []

        print('BATENDO AQUI 1')

        try:

            print('BATENDO AQUI 2')

            cursor = conn.cursor()
            cursor.execute(query)

            print('BATENDO AQUI 3')

            print(cursor.fetchall())

            for linha in cursor.fetchall():
                data.append(linha)
                print(linha)
                print('BATENDO AQUI 4')

        except Exception as e:
            print(e)

        print('BATENDO AQUI 5')
        return data

    def get_data(self, table='', query=''):

        query = query if query != '' else f"SELECT * FROM '{table}';"

        print(query)

        with self.__connection() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)
                result.close()
        print("\n")

    def __init__(self):
        self.__conn = sqlite3.connect(f'{DB_NAME}.db')

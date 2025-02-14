import pymysql
import pymysql.cursors
import time


class Conn():
    def __init__(self, host="db_ecom", user="root", password="senha", database="db_ecom", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def create_connection(self):
        for _ in range(10):
            try:
                self.connection = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port,
                    cursorclass=pymysql.cursors.DictCursor,
                )
                print("Conexão estabelecida com sucesso!")
                return self.connection
            except Exception as e:
                print(f"Erro ao conectar ao DB: {e}")
                time.sleep(5)
        raise Exception("Não foi possível conectar ao MySQL após várias tentativas.")

    def commit(self):
        if self.connection:
            try:
                self.connection.commit()
                print("Commit realizado com sucesso!")
            except Exception as e:
                print(f"Erro ao realizar o commit: {e}")
        else:
            print("Nenhuma conexão aberta para realizar o commit.")
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexão fechada com sucesso.")
        else:
            print("Nenhuma conexão para fechar.")

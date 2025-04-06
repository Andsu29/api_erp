from connection.main import Conn
from querys.main import query_get_all_products, query_post_products, query_update_file


class Methods():
    def __init__(self):
        self.connection = Conn()

    def get_products(self):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_get_all_products()
                cursor.execute(query)
                data = cursor.fetchall()
                if data:
                    return data
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
        finally:
                self.connection.close_connection()
        
    def insert_product(self, titulo, descricao, preco, categoria, marca, modelo, codpro):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro)
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")
        finally:
            self.connection.close_connection()

    def insert_image(self, file, codPro):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_update_file()
                cursor.execute(query, (file, codPro))
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao adicionar imagem: {e}")
        finally:
            self.connection.close_connection()
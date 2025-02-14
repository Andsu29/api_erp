from connection.main import Conn
from querys.main import query_get_all_products, query_post_products


class Methods():
    def __init__(self):
        self.connection = Conn()

    def get_products(self):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_get_all_products()
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
        finally:
                self.connection.close_connection()
        
    def post_product(self, titulo):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_post_products(titulo)
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")
        finally:
                self.connection.close_connection()

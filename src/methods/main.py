from connection.main import Conn
from querys.main import query_get_all_products, query_post_products
import json


class Methods():
    def __init__(self):
        self.connection = Conn()

    def get_products(self):
        with self.connection.create_connection().cursor() as cursor:
            query = query_get_all_products()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        
    def post_product(self, titulo):
        with self.connection.create_connection().cursor() as cursor:
            query = query_post_products(titulo)
            cursor.execute(query)
            self.connection.commit()
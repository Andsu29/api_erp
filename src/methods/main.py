import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))
from setup.enviroments import DB1, DB2
from connection.main import Conn
from querys.main import query_get_all_products, query_post_products, query_update_file, query_delete_product, query_get_product, query_update_product


class Methods():
    def __init__(self):
        self.connection_db1 = Conn(DB1['host'], DB1['user'], DB1['password'], DB1['database'], DB1['port'])
        self.connection_db2 = Conn(DB2['host'], DB2['user'], DB2['password'], DB2['database'], DB2['port'])

    def get_products(self):
        try:
            with self.connection_db1.create_connection().cursor() as cursor:
                query = query_get_all_products()
                cursor.execute(query)
                data = cursor.fetchall()
                if data:
                    return data
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
        finally:
                self.connection_db1.close_connection()

    def get_product(self, id_produto):
        try:
            with self.connection_db1.create_connection().cursor() as cursor:
                query = query_get_product(id_produto)
                cursor.execute(query)
                data = cursor.fetchone()
                if data:
                    return data
        except Exception as e:
            print(f"Erro ao buscar produto: {e}")
        finally:
                self.connection_db1.close_connection()
        
    def insert_product(self, titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor):
        try:
            with self.connection_db1.create_connection().cursor() as cursor:
                query = query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor)
                cursor.execute(query)
                self.connection_db1.commit()
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")
        finally:
            self.connection_db1.close_connection()

    def insert_image(self, file, id_produto):
        try:
            with self.connection_db2.create_connection().cursor() as cursor:
                query = query_update_file()
                cursor.execute(query, (file, id_produto))
                self.connection_db2.commit()
        except Exception as e:
            print(f"Erro ao adicionar imagem: {e}")
        finally:
            self.connection_db2.close_connection()
    
    def remove_product(self, id_product):
        try:
            with self.connection_db1.create_connection().cursor() as cursor:
                query = query_delete_product()
                cursor.execute(query, id_product)
                self.connection_db1.commit()
        except Exception as e:
            print(f"Erro ao remover produto: {e}")
        finally:
            self.connection_db1.close_connection()
    
    def update_product(self, id_produto, titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor):
        try:
            with self.connection_db1.create_connection().cursor() as cursor:
                query = query_update_product(id_produto)
                values = (titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor)
                cursor.execute(query, values)
                self.connection_db1.commit()
        except Exception as e:
            print(f"Erro ao remover produto: {e}")
        finally:
            self.connection_db1.close_connection()
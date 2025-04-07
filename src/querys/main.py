def query_get_all_products():
    return """
    SELECT * FROM produtos
"""

def query_get_product(id_produto):
    return f"""
    SELECT * FROM produtos WHERE id = {id_produto}
"""

def query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro):
    return f"INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro) VALUES ('{titulo}', '{descricao}', {preco}, '{categoria}', '{marca}', '{modelo}', '{codpro}')"

def query_update_file():
    return f"""
    UPDATE produtos SET imagens = %s WHERE codPro = %s;
    """

def query_delete_product():
    return f"""
    DELETE FROM produtos WHERE id = %s;
"""
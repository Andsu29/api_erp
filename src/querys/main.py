


def query_get_all_products():
    return """
    SELECT * FROM produtos
"""

def query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro):
    return f"INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro) VALUES ('{titulo}', '{descricao}', {preco}, '{categoria}', '{marca}', '{modelo}', '{codpro}')"

def query_update_file():
    return f"""
    UPDATE produtos SET imagens = %s WHERE codPro = %s;
    """
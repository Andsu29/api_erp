def query_get_all_products():
    return """
    SELECT * FROM produtos
    """

def query_get_product(pid):
    return f"""
    SELECT * FROM produtos WHERE id = {pid}
    """

def query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro):
    return f"""
        INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro) VALUES ('{titulo}', '{descricao}', {preco}, '{categoria}', '{marca}', '{modelo}', '{codpro}')
    """

def query_update_file():
    return f"""
        UPDATE produtos SET imagens = %s WHERE id = %s;
    """

def query_delete_product():
    return f"""
        DELETE FROM produtos WHERE id = %s;
    """

def query_update_product(pid):
    return f"""
        UPDATE produtos SET titulo=%s, descricao=%s, preco=%s, categoria=%s, marca=%s, modelo=%s, codpro=%s WHERE id = {pid};
    """
def query_get_all_products():
    return """
    SELECT * FROM produtos
    """

def query_get_product(id_produto):
    return f"""
    SELECT * FROM produtos WHERE id = {id_produto}
    """

def query_post_products(titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor):
    return f"""
        INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro, qtd_estoque, cor) VALUES ('{titulo}', '{descricao}', {preco}, '{categoria}', '{marca}', '{modelo}', '{codpro}', '{qtd_estoque}', '{cor}')
    """

def query_update_file():
    return f"""
        UPDATE produtos SET imagens = %s WHERE pid = %s;
    """

def query_delete_product():
    return f"""
        DELETE FROM produtos WHERE id = %s;
    """

def query_update_product(id_produto):
    return f"""
        UPDATE produtos SET titulo=%s, descricao=%s, preco=%s, categoria=%s, marca=%s, modelo=%s, codpro=%s, qtd_estoque=%s, cor=%s WHERE id = {id_produto};
    """
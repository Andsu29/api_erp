


def query_get_all_products():
    return """
    SELECT * FROM produtos
"""

def query_post_products(titulo):
    return f"""
    INSERT INTO produtos (titulo) VALUES ('{titulo}')
"""

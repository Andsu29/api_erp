from flask import Flask, jsonify, request
from methods.main import Methods
import base64

app = Flask(__name__)
methods = Methods()

@app.route('/produtos', methods=['GET'])
def all_products():
    products = methods.get_products()
    produtos_formatados = []
    
    for product in products:
        imagem_base64 = None
        if product["imagens"]:
            imagem_base64 = base64.b64encode(product['imagens']).decode("utf-8")

        produtos_formatados.append(
            {
                "id":  product["id"],
                "titulo": product["titulo"],
                "publicado": product["publicado"],
                "descricao": product["descricao"],
                "preco": product["preco"],
                "categoria": product["categoria"],
                "marca": product["marca"],
                "modelo": product["modelo"],
                "codpro": product["codpro"],
                "imagens": imagem_base64
            })
    return jsonify(produtos_formatados)

@app.route('/produto/<id_produto>', methods=['GET'])
def get_product(id_produto: int):
    product = methods.get_product(id_produto)
    produto_formatado = []
    imagem_base64 = None

    if product["imagens"]:
        imagem_base64 = base64.b64encode(product['imagens']).decode("utf-8")

    produto_formatado.append(
            {
                "id":  product["id"],
                "titulo": product["titulo"],
                "publicado": product["publicado"],
                "descricao": product["descricao"],
                "preco": product["preco"],
                "categoria": product["categoria"],
                "marca": product["marca"],
                "modelo": product["modelo"],
                "codpro": product["codpro"],
                "imagens": imagem_base64
            })
    
    return jsonify(produto_formatado)

@app.route('/inserir_produto', methods=['POST'])
def post_product():
    data = request.json
    if data:
        titulo = data['titulo']
        descricao = data['descricao']
        preco = data['preco']
        categoria = data['categoria']
        marca = data['marca']
        modelo = data['modelo']
        codpro = data['codpro']
        
        methods.insert_product(titulo, descricao, preco, categoria, marca, modelo, codpro)
        return jsonify({"Sucesso": "Dados inseridos"}), 200
    else:
        return jsonify({'Erro': 'Erro ao adicionar produto'}), 400

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'Erro': 'Campo "file" não encontrado'}), 400

    if 'codPro' not in request.form:
        return jsonify({'Erro': 'Campo "codPro" não encontrado'}), 400
    
    file = request.files['file']
    codPro = request.form['codPro']

    if file.filename == '':
        return jsonify({'Erro': 'Nenhum arquivo enviado'}), 400

    methods.insert_image(file.read(), int(codPro))
    return jsonify({"Mensagem": "Imagem inserida"})

@app.route('/remover_produto/<id_produto>', methods=['DELETE'])
def delete_product(id_produto: int):
    if id_produto:
        methods.remove_product(id_produto)
        return jsonify({"Mensagem": "Produto Removido!"})
    else:
        return jsonify({"Mensagem": "ID não encontrado!"})
from flask import Flask, jsonify, request
from methods.main import Methods

app = Flask(__name__)
methods = Methods()

@app.route('/produtos', methods=['GET'])
def all_products():
    products = methods.get_products()
    return jsonify(products)

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
        print(titulo, descricao, preco, categoria, marca, modelo, codpro)
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

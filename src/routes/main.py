from flask import Flask, jsonify, request
from methods.main import Methods

app = Flask(__name__)
methods = Methods()

@app.route('/produtos', methods=['GET'])
def all_products():
    products = methods.get_products()
    return jsonify(products)

@app.route('/inserir_produto', methods=['POST'])
def insert_product():
    data = request.json
    if data:
        titulo = data['titulo']
        methods.post_product(titulo)
        return jsonify({"Mensagem": "Dados inseridos"}), 200
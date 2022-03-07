from shop_api.shop_api import __version__
from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

products = [
    {
        "id": 1,
        "name": "string",
        "description": "string",
        "category_id": 1
    },
    {
        "id": 2,
        "name": "string",
        "description": "string",
        "category_id": 1
    }
]


@app.route('/products', methods=['GET', 'POST'])
def set_products():
    if request.method == 'GET':
        return jsonify(products)

    elif request.method == 'POST':
        new_product = request.json
        new_id = products[-1]["id"] + 1
        new_product["id"] = new_id
        products.append(new_product)
        return jsonify(products[-1])


@app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def get_product(product_id):
    if request.method == 'GET':
        answer = jsonify(next(x for x in products if x['id'] == product_id))
        return answer
    elif request.method == 'PUT':
        edit_product = request.json
        products.remove(next(x for x in products if x['id'] == product_id))
        products.append(edit_product)
        return '200 OK'
    elif request.method == 'DELETE':
        products.remove(next(x for x in products if x['id'] == product_id))
        return '200 OK'


if __name__ == '__main__':
    app.run()


def test_version():
    assert __version__ == '0.1.0'

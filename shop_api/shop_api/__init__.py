__version__ = '0.1.0'

from flask import Flask, jsonify, request

app = Flask(__name__)

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
        return products[-1]


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    answer = jsonify(next(x for x in products if x['id'] == product_id))
    return answer


if __name__ == '__main__':
    app.run()

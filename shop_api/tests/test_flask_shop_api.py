from shop_api.shop_api import __version__
from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

categories = [
    {
        'id': 1,
        'name': 'first_category'
    },
    {
        'id': 2,
        'name': 'second_category'
    }
]

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
        "description": "desc",
        "category_id": 1
    }
]


def find_all_by_keys(keys, value):
    def find_category_id(query):
        for index, dict_ in enumerate(categories):
            if dict_['name'] == query:
                return dict_['id']

    def find_values(keys_, value_):
        for key_ in keys_:
            for index, dict_ in enumerate(products):
                if dict_[key_] == value_:
                    return dict_

    answer_array = [find_values(keys, value)]
    if find_category_id(value) is not None:
        key = ['category_id']
        answer_array.append(find_values(key, find_category_id(value)))
    return list(filter(None, answer_array))


@app.route('/products', methods=['GET', 'POST'])
def set_products():
    if request.method == 'GET':
        if request.args.get('query') is None:
            return jsonify(products)
        else:
            query = request.args.get('query')
            keys = ['name', 'description']
            answer = jsonify(find_all_by_keys(keys, query))
            return answer
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

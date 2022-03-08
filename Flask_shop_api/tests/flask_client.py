from test_flask_shop_api import app, client

response = client.get('/products/2')

print(f'GET ID#2: \n{response.get_json()}')

response = client.post('/products', json={"name": "POST",
                                          "description": "POST",
                                          "category_id": 1})

print(f'POST STATUS_CODE: {response.status_code}')
print(f'POST: \n{response.get_json()}')

response = client.put('/products/2', json={"id": 2,
                                           "name": "PUT",
                                           "description": "PUT",
                                           "category_id": 1})
print(f'PUT STATUS_CODE: {response.status_code}')

response = client.get('/products')

print(f'GET STATUS_CODE: {response.status_code}')
print(f'GET: \n{response.get_json()}')

response = client.delete('/products/3')

print(f'DELETE #3 STATUS_CODE: {response.status_code}')

response = client.get('/products')

print(f'GET STATUS_CODE: {response.status_code}')
print(f'GET: \n{response.get_json()}')

response = client.get('/products?query=PUTA')

print(f'GET QUERY STATUS_CODE: {response.status_code}')
print(f'GET QUERY: \n{response.get_json()}')

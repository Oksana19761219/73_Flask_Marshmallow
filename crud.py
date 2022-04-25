import requests
import json

# product = {'name': 'product2', 'price': 158, 'quantity': 10}
# r = requests.post('http://127.0.0.1:8000/', json=product)
# print(json.loads(r.text))


# r = requests.get('http://127.0.0.1:8000/')
# print(json.loads(r.text))

# r = requests.get('http://127.0.0.1:8000/1')
# print(json.loads(r.text))


# product3 = {'name': 'product2', 'price': 157, 'quantity': 100}
# r = requests.put('http://127.0.0.1:8000/1', json=product3)

r = requests.delete('http://127.0.0.1:8000/1')
print(json.loads(r.text))
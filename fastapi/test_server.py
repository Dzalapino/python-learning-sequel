import requests

print("index page:\n", requests.get("http://127.0.0.1:8000/").json())

print("\n### Get by id ###")
print("\nget by id = 0:\n", requests.get("http://127.0.0.1:8000/items/0").json())
# Q: (below) why when we got json with http error it doesnt have error status code
print("\nget by id = 69420:\n", requests.get("http://127.0.0.1:8000/items/69420").json())
# pydantic does validation for us
print("\nget by id = 'XD':\n", requests.get("http://127.0.0.1:8000/items/XD").json())

print("\n### Get by query parameter ###")
print("\nget by parameter name = 'harnold':\n", requests.get("http://127.0.0.1:8000/items?name=harnold").json())
print("\nget by parameter name = 'harnold' and price = '2.99':\n", requests.get("http://127.0.0.1:8000/items?name=harnold&price=2.99").json())
print("\nget by parameter count = 100:\n", requests.get("http://127.0.0.1:8000/items?count=100").json())

print("\n### Adding an item ###")

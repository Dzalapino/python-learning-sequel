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
# this should fail as there is no such category like blob
print("\nget by parameter category = blob:\n", requests.get("http://127.0.0.1:8000/items?category=blob").json())

print("\n### Adding an item ###")
print(
    requests.post(
        "http://127.0.0.1:8000/items/",
        json={"name": "new_item", "price": 420.69, "count": 10, "id": 4, "category": "tools"}
    ).json()
)
print("\nCheck if new item was added:\n", requests.get("http://127.0.0.1:8000/items/4").json())

print("\n### Updating new item ###")
print(requests.put("http://127.0.0.1:8000/items/4?count=9999").json())
print("\nCheck if new item was updated:\n", requests.get("http://127.0.0.1:8000/items/4").json())
print("\nSome fail updates because of validation:")
print(requests.put("http://127.0.0.1:8000/items/-1").json())
print(requests.put("http://127.0.0.1:8000/items/4?name=zdecydowanie_za_dluga_nazwa").json())
print(requests.put("http://127.0.0.1:8000/items/4?price=-0.1").json())
print(requests.put("http://127.0.0.1:8000/items/4?count=-1").json())

print("\n### Deleting new item ###")
print(requests.delete("http://127.0.0.1:8000/items/4").json())
print("\nCheck if new item was deleted:\n", requests.get("http://127.0.0.1:8000/items/4").json())
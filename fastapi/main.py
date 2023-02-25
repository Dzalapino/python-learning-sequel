from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# creating instance of FastAPI
app = FastAPI()

# simple model classes
class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

items = {
    0: Item(name = "harnold", price = 2.99, count = 100, id = 0, category = Category.CONSUMABLES),
    1: Item(name = "jakis kraficik", price = 7.50, count = 25, id = 1, category = Category.CONSUMABLES),
    2: Item(name = "talon na balon", price = 9.99, count = 2, id = 2, category = Category.TOOLS)
}

# FastAPI handles JSON serialization and deserialization for us
# We can simply use built-in python or Pydantic types, in this case dict[int, item]
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

# Path parameters can be specified with {} directly in the path (similar to f-string syntax)
# These parameters will be forwarded to the decorated function as keyword arguments.
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} doesn't exist.")
    return items[item_id]

# function parameters that are not path parameters can be specified as query parameters in the URL
# here we can query items like this /items?count=20
Selection = dict[
    str, str | int | float | Category | None
] # dictionary containing the user's query arguments

@app.get("/items")
def get_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item) -> bool:
        """Check if the item matches the query arguments from the outer scope."""
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category is category
            )
        )
    
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection
    }

@app.post("/items")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")
    items[item.id] = item
    return {"added": item}

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str | None = None,
    price: float | None = None,
    count: int | None = None
) -> dict[str, Item]:
    
    if item_id not in items:
        # Q: why here without raise and later with raise?
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    if all(info is None for info in (name, price, count)):
        # Q: what raise does?
        raise HTTPException(status_code=400, detail="No parameters provided for update.")
    
    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count
    
    return {"updated": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    
    item = items.pop(item_id)
    return {"deleted": item}
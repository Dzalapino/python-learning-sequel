import motor.motor_asyncio # MongoDB driver
from model import Todo

CONNECTION_STR = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STR)
database = client.TodoList
collection = database.todo

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def fetch_todo_by_title(title):
    document = await collection.find_one({"title": title})
    return document

async def add_todo(todo):
    document = todo
    await collection.insert_one(document)
    return document

async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    result = await collection.delete_one({"title": title})
    if result.deleted_count > 0:
        return True
    return False
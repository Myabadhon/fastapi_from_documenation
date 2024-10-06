from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    password: str
    email: str

@app.put("/item/{item_id}")
async def read_item(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result

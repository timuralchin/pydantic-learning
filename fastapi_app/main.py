from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, EmailStr


class Item(BaseModel):
    id: PositiveInt
    email: EmailStr


app = FastAPI()


@app.post('/item',  response_model=Item)
async def get_item(item: Item):
    return item


@app.get('/items',  response_model=list[Item])
async def get_item():
    return [Item(id=id, email='test@test.com') for id in range(1, 5)]

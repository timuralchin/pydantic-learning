from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str


app = FastAPI()


@app.post('/item',  response_model=Item)
async def get_item(item: Item):
    return item


@app.get('/items',  response_model=list[Item])
async def get_item():
    return [Item(id=id, name='test') for id in range(5)]

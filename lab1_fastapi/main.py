from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Liste des items
items = []

# Modèle Pydantic
class Item(BaseModel):
    text: str
    is_done: bool = False

# Route GET /
@app.get("/")
def root():
    return {"Hello": "World"}

# Route POST /items
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Route GET /items/{item_id}
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Route GET /items?limit=3
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id < len(items):
        items[item_id] = updated_item
        return updated_item
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        deleted = items.pop(item_id)
        return {"deleted": deleted}
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

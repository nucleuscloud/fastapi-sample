from typing import Optional
import fastapi
import myfile

app = fastapi.FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World from FastAPI sample"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/myfunction")
async def read_myfunction():
    return myfile.generate_message()
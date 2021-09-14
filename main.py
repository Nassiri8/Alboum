from fastapi import FastAPI
from handlers import item, user

app = FastAPI()

app.include_router(item.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
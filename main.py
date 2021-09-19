from fastapi import FastAPI
from handlers import item, user, admin, order, supplier

app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(supplier.router)
app.include_router(order.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Welcome"


product=[
    Product(id=1,name="phone",description="budget phone",price=11.2,quantity=1)
]

@app.get("/product")
def all_product():
    return product
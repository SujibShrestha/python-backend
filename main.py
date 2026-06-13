from fastapi import FastAPI
# from models import Product
from database import SessionLocal,engine
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine) 

@app.get("/")
def greet():
    return "Welcome"


products=[
    # Product(id=1,name="phone",description="budget phone",price=11.2,quantity=1),
    # Product(id=2,name="phone34",description="budget phone",price=11.2,quantity=1),
    # Product(id=3,name="phone23",description="budget phone",price=11.2,quantity=1)
]

def initDB():
    db = SessionLocal()
    try:
        db.add(models.Product(id=1, name="phone", description="budget phone", price=11.2, quantity=1))
        db.commit()
    finally:
        db.close()

initDB()

@app.get("/product")
def all_product(): 

    db = SessionLocal() 
    db.query()
    return products

@app.get("/product/{id}")
def getProductById(id:int):
    for product in products:
     if product.id == id:
        return product
    return product[id]

@app.post("/product")
def addProduct(product):
    products.append(product)
    return products

@app.put("/product/{id}")
def updateProduct(id:int,product):
   for i in range(len(products)):
      if products[i].id== id :
         products[i] = product
         return "Added Successfully"
    
   return 'No product found'




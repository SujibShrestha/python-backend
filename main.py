from fastapi import Depends,FastAPI
# from models import Product
from database import SessionLocal,engine
import models
from sqlalchemy.orm import Session

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

def getDB():
   db= SessionLocal()
   try:
      yield db
   finally:
      db.close()


@app.get("/product")
def all_product(db:Session = Depends(getDB)): 
    db_products = db.query(models.Product).all()
    return db_products

@app.get("/product/{id}")
def getProductById(id:int,db:Session= Depends(getDB)):
    db_products = db.query(models.Product).filter(models.Product.id == id).first()
    return db_products

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




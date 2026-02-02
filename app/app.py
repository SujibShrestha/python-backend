from fastapi import FastAPI

app = FastAPI() 

@app.get("/") # @ = decorator
def api():
    return {"message":"Api is running"} # dict = JSON
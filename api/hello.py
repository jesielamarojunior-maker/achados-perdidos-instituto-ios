from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Olá do back-end!"}

handler = Mangum(app)
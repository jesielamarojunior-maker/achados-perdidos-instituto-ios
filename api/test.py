from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Funcionando!", "status": "online", "service": "Achados e Perdidos IOS"}

@app.get("/test")
def test():
    return {"test": "OK", "message": "Endpoint de teste funcionando"}

# Handler para Vercel
handler = Mangum(app)
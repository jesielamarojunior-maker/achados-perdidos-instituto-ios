from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
from datetime import datetime
import uuid
from mangum import Mangum

app = FastAPI()

# Configurar CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de dados
class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    image: str
    found_at: str
    location: str
    created_at: Optional[str] = None

class Comment(BaseModel):
    id: Optional[str] = None
    item_id: int
    author: str
    text: str
    created_at: Optional[str] = None

class Claim(BaseModel):
    id: Optional[str] = None
    item_id: int
    claimer_name: str
    claim_date: Optional[str] = None

class LoginRequest(BaseModel):
    password: str

# Dados em memória (Vercel Serverless não persiste arquivos)
DEFAULT_DATA = {
    "items": [
        {
            "id": 1,
            "title": "Carteira de couro marrom",
            "description": "Carteira encontrada no pátio da escola. Contém documentos.",
            "image": "images/carteira-marrom-001.jpg",
            "found_at": "2024-10-20",
            "location": "Pátio principal",
            "created_at": "2024-10-20T10:30:00"
        },
        {
            "id": 2,
            "title": "Óculos de sol Ray-Ban",
            "description": "Óculos escuros encontrados na quadra esportiva.",
            "image": "images/oculos-rayban-002.jpg",
            "found_at": "2024-10-21",
            "location": "Quadra de esportes",
            "created_at": "2024-10-21T14:15:00"
        },
        {
            "id": 3,
            "title": "Chaveiro do Batman",
            "description": "Chaveiro com 3 chaves encontrado no corredor.",
            "image": "images/chaves-batman-003.jpg",
            "found_at": "2024-10-22",
            "location": "Corredor do 2º andar",
            "created_at": "2024-10-22T09:45:00"
        }
    ],
    "comments": {},
    "claimed_items": [],
    "claimed_data": {},
    "next_id": 4
}

# Variável global para armazenar dados (em memória)
_data_store = DEFAULT_DATA.copy()

def get_data():
    """Retorna dados atuais"""
    return _data_store

def save_data(data):
    """Salva dados na memória"""
    global _data_store
    _data_store = data
    return True

# ========== ENDPOINTS DOS ITEMS ==========

@app.get("/")
async def root():
    return {"message": "API Achados e Perdidos - Instituto da Oportunidade Social", "status": "online"}

@app.get("/items", response_model=List[Item])
async def get_items():
    """Buscar todos os items não reclamados"""
    data = get_data()
    available_items = []
    
    for item in data["items"]:
        if item["id"] not in data["claimed_items"]:
            available_items.append(item)
    
    return available_items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """Criar novo item"""
    data = get_data()
    
    # Gerar ID único
    item.id = data["next_id"]
    data["next_id"] += 1
    
    # Adicionar timestamp
    item.created_at = datetime.now().isoformat()
    
    # Adicionar à lista
    data["items"].append(item.dict())
    
    save_data(data)
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Deletar item"""
    data = get_data()
    
    # Remover item da lista principal
    data["items"] = [item for item in data["items"] if item["id"] != item_id]
    
    # Remover das listas de reclamados
    if item_id in data["claimed_items"]:
        data["claimed_items"].remove(item_id)
    
    if str(item_id) in data["claimed_data"]:
        del data["claimed_data"][str(item_id)]
    
    # Remover comentários do item
    if str(item_id) in data["comments"]:
        del data["comments"][str(item_id)]
    
    save_data(data)
    return {"message": "Item deletado com sucesso"}

# ========== ENDPOINTS DOS COMENTÁRIOS ==========

@app.get("/items/{item_id}/comments")
async def get_comments(item_id: int):
    """Buscar comentários de um item"""
    data = get_data()
    return data["comments"].get(str(item_id), [])

@app.post("/items/{item_id}/comments")
async def add_comment(item_id: int, comment: Comment):
    """Adicionar comentário a um item"""
    data = get_data()
    
    # Verificar se item existe
    item_exists = any(item["id"] == item_id for item in data["items"])
    if not item_exists:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    # Gerar ID único para comentário
    comment.id = str(uuid.uuid4())
    comment.item_id = item_id
    comment.created_at = datetime.now().isoformat()
    
    # Adicionar comentário
    if str(item_id) not in data["comments"]:
        data["comments"][str(item_id)] = []
    
    data["comments"][str(item_id)].append(comment.dict())
    
    save_data(data)
    return comment

# ========== ENDPOINTS DOS CLAIMS ==========

@app.post("/items/{item_id}/claim")
async def claim_item(item_id: int, claim: Claim):
    """Reclamar um item"""
    data = get_data()
    
    # Verificar se item existe e não foi reclamado
    item_exists = any(item["id"] == item_id for item in data["items"])
    if not item_exists:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    if item_id in data["claimed_items"]:
        raise HTTPException(status_code=400, detail="Item já foi reclamado")
    
    # Adicionar aos reclamados
    claim.item_id = item_id
    claim.claim_date = datetime.now().isoformat()
    
    data["claimed_items"].append(item_id)
    data["claimed_data"][str(item_id)] = claim.dict()
    
    save_data(data)
    return {"message": "Item reclamado com sucesso", "claim": claim}

@app.get("/claimed-items")
async def get_claimed_items():
    """Buscar items reclamados (admin)"""
    data = get_data()
    claimed_items = []
    
    for item in data["items"]:
        if item["id"] in data["claimed_items"]:
            claim_info = data["claimed_data"].get(str(item["id"]), {})
            claimed_items.append({
                **item,
                "claim_info": claim_info
            })
    
    return claimed_items

@app.post("/items/{item_id}/restore")
async def restore_item(item_id: int):
    """Devolver item ao feed"""
    data = get_data()
    
    if item_id in data["claimed_items"]:
        data["claimed_items"].remove(item_id)
    
    if str(item_id) in data["claimed_data"]:
        del data["claimed_data"][str(item_id)]
    
    save_data(data)
    return {"message": "Item devolvido ao feed"}

@app.post("/items/{item_id}/deliver")
async def confirm_delivery(item_id: int):
    """Confirmar entrega do item (remove definitivamente)"""
    data = get_data()
    
    # Remover completamente
    data["items"] = [item for item in data["items"] if item["id"] != item_id]
    
    if item_id in data["claimed_items"]:
        data["claimed_items"].remove(item_id)
    
    if str(item_id) in data["claimed_data"]:
        del data["claimed_data"][str(item_id)]
    
    if str(item_id) in data["comments"]:
        del data["comments"][str(item_id)]
    
    save_data(data)
    return {"message": "Item marcado como entregue"}

# ========== ENDPOINT DE AUTENTICAÇÃO ==========

@app.post("/auth/login")
async def login(login_request: LoginRequest):
    """Verificar senha do admin"""
    # Senha personalizada para Instituto da Oportunidade Social
    correct_password = "973439010"
    
    if login_request.password == correct_password:
        return {"success": True, "message": "Login realizado com sucesso"}
    else:
        raise HTTPException(status_code=401, detail="Senha incorreta")

# ========== ENDPOINT DE RESET ==========

@app.post("/reset")
async def reset_data():
    """Resetar dados para padrão original"""
    global _data_store
    _data_store = DEFAULT_DATA.copy()
    return {"message": "Dados resetados para padrão original"}

# Handler para Vercel com Mangum
handler = Mangum(app)
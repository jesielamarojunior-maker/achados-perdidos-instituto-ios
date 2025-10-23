from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from datetime import datetime
import uuid

app = FastAPI(title="Achados e Perdidos API", version="1.0.0")

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

# Arquivo de dados
DATA_FILE = "database.json"

def load_data():
    """Carrega dados do arquivo JSON"""
    if not os.path.exists(DATA_FILE):
        return {
            "items": [],
            "comments": {},
            "claimed_items": [],
            "claimed_data": {},
            "next_id": 1
        }
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {
            "items": [],
            "comments": {},
            "claimed_items": [],
            "claimed_data": {},
            "next_id": 1
        }

def save_data(data):
    """Salva dados no arquivo JSON"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False

# Inicializar com dados padrão se arquivo não existir
def init_default_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
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
        save_data(default_data)

# Inicializar dados padrão
init_default_data()

# ========== ENDPOINTS DOS ITEMS ==========

@app.get("/")
async def root():
    return {"message": "API Achados e Perdidos - Instituto da Oportunidade Social", "status": "online"}

@app.get("/api/items", response_model=List[Item])
async def get_items():
    """Buscar todos os items não reclamados"""
    data = load_data()
    available_items = []
    
    for item in data["items"]:
        if item["id"] not in data["claimed_items"]:
            available_items.append(item)
    
    return available_items

@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    """Criar novo item"""
    data = load_data()
    
    # Gerar ID único
    item.id = data["next_id"]
    data["next_id"] += 1
    
    # Adicionar timestamp
    item.created_at = datetime.now().isoformat()
    
    # Adicionar à lista
    data["items"].append(item.dict())
    
    if save_data(data):
        return item
    else:
        raise HTTPException(status_code=500, detail="Erro ao salvar item")

@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """Deletar item"""
    data = load_data()
    
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
    
    if save_data(data):
        return {"message": "Item deletado com sucesso"}
    else:
        raise HTTPException(status_code=500, detail="Erro ao deletar item")

# ========== ENDPOINTS DOS COMENTÁRIOS ==========

@app.get("/api/items/{item_id}/comments")
async def get_comments(item_id: int):
    """Buscar comentários de um item"""
    data = load_data()
    return data["comments"].get(str(item_id), [])

@app.post("/api/items/{item_id}/comments")
async def add_comment(item_id: int, comment: Comment):
    """Adicionar comentário a um item"""
    data = load_data()
    
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
    
    if save_data(data):
        return comment
    else:
        raise HTTPException(status_code=500, detail="Erro ao salvar comentário")

# ========== ENDPOINTS DOS CLAIMS ==========

@app.post("/api/items/{item_id}/claim")
async def claim_item(item_id: int, claim: Claim):
    """Reclamar um item"""
    data = load_data()
    
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
    
    if save_data(data):
        return {"message": "Item reclamado com sucesso", "claim": claim}
    else:
        raise HTTPException(status_code=500, detail="Erro ao reclamar item")

@app.get("/api/claimed-items")
async def get_claimed_items():
    """Buscar items reclamados (admin)"""
    data = load_data()
    claimed_items = []
    
    for item in data["items"]:
        if item["id"] in data["claimed_items"]:
            claim_info = data["claimed_data"].get(str(item["id"]), {})
            claimed_items.append({
                **item,
                "claim_info": claim_info
            })
    
    return claimed_items

@app.post("/api/items/{item_id}/restore")
async def restore_item(item_id: int):
    """Devolver item ao feed"""
    data = load_data()
    
    if item_id in data["claimed_items"]:
        data["claimed_items"].remove(item_id)
    
    if str(item_id) in data["claimed_data"]:
        del data["claimed_data"][str(item_id)]
    
    if save_data(data):
        return {"message": "Item devolvido ao feed"}
    else:
        raise HTTPException(status_code=500, detail="Erro ao restaurar item")

@app.post("/api/items/{item_id}/deliver")
async def confirm_delivery(item_id: int):
    """Confirmar entrega do item (remove definitivamente)"""
    data = load_data()
    
    # Remover completamente
    data["items"] = [item for item in data["items"] if item["id"] != item_id]
    
    if item_id in data["claimed_items"]:
        data["claimed_items"].remove(item_id)
    
    if str(item_id) in data["claimed_data"]:
        del data["claimed_data"][str(item_id)]
    
    if str(item_id) in data["comments"]:
        del data["comments"][str(item_id)]
    
    if save_data(data):
        return {"message": "Item marcado como entregue"}
    else:
        raise HTTPException(status_code=500, detail="Erro ao confirmar entrega")

# ========== ENDPOINT DE AUTENTICAÇÃO ==========

@app.post("/api/auth/login")
async def login(login_request: LoginRequest):
    """Verificar senha do admin"""
    # Senha personalizada para Instituto da Oportunidade Social
    correct_password = "973439010"
    
    if login_request.password == correct_password:
        return {"success": True, "message": "Login realizado com sucesso"}
    else:
        raise HTTPException(status_code=401, detail="Senha incorreta")

# ========== ENDPOINT DE RESET ==========

@app.post("/api/reset")
async def reset_data():
    """Resetar dados para padrão original"""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    
    init_default_data()
    return {"message": "Dados resetados para padrão original"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
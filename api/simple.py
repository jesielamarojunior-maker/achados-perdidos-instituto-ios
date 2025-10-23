from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import uuid

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Dados de exemplo para teste
        items_data = [
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
            }
        ]
        
        path = self.path
        
        # Headers CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        
        # Roteamento básico
        if path == '/' or path == '':
            response = {"message": "API Achados e Perdidos - Instituto da Oportunidade Social", "status": "online"}
        elif path == '/items':
            response = items_data
        elif path.startswith('/items/') and path.endswith('/comments'):
            response = []
        else:
            response = {"error": "Endpoint não encontrado"}
        
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
    
    def do_POST(self):
        # Headers CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        
        path = self.path
        
        if path == '/auth/login':
            # Ler dados da requisição
            content_length = int(self.headers['Content-Length']) if 'Content-Length' in self.headers else 0
            post_data = self.rfile.read(content_length).decode() if content_length > 0 else '{}'
            
            try:
                data = json.loads(post_data)
                password = data.get('password', '')
                
                if password == '973439010':
                    response = {"success": True, "message": "Login realizado com sucesso"}
                else:
                    self.send_response(401)
                    response = {"success": False, "message": "Senha incorreta"}
            except:
                self.send_response(400)
                response = {"success": False, "message": "Dados inválidos"}
        else:
            response = {"message": "Endpoint POST não implementado ainda"}
        
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
    
    def do_OPTIONS(self):
        # Resposta para preflight CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
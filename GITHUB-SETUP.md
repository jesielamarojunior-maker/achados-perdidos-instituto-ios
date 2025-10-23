# 🚀 COMANDOS PARA CRIAR REPOSITÓRIO GITHUB

## Nome sugerido do repositório:

**`achados-perdidos-instituto-ios`**

## Passo-a-passo completo:

### 1. Criar repositório no GitHub

1. Vá para **https://github.com**
2. Clique em **"New repository"** (botão verde)
3. **Repository name:** `achados-perdidos-instituto-ios`
4. **Description:** `Sistema web de achados e perdidos - Instituto da Oportunidade Social`
5. **Visibilidade:** Público (recomendado) ou Privado
6. **NÃO marcar** "Add a README file" (já temos)
7. **NÃO marcar** "Add .gitignore" (já temos)
8. **NÃO marcar** "Choose a license" (já configurado)
9. Clicar **"Create repository"**

### 2. Comandos no terminal (PowerShell)

```powershell
# Navegar para a pasta do projeto
cd "C:\Users\Participante IOS.DESKTOP-DHQGCTG\Documents\achados-perdidos-ios"

# Inicializar Git (se ainda não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "feat: sistema completo achados e perdidos IOS com backend FastAPI"

# Adicionar repositório remoto (SUBSTITUIR SEU_USUARIO pelo seu username GitHub)
git remote add origin https://github.com/SEU_USUARIO/achados-perdidos-instituto-ios.git

# Definir branch principal
git branch -M main

# Enviar para GitHub
git push -u origin main
```

### 3. Estrutura do repositório criado:

```
achados-perdidos-instituto-ios/
├── 📄 README.md              # Documentação principal
├── 🌐 index.html             # Página pública dos alunos
├── 🔐 admin.html             # Painel administrativo (senha: 973439010)
├── ⚡ api.js                 # Cliente JavaScript para API
├── 📊 items.json             # Dados iniciais
├── 🚀 vercel.json            # Configuração deploy Vercel
├── 📦 package.json           # Metadata do projeto
├── 🔧 .gitignore            # Arquivos ignorados
├── 📖 DEPLOY-GUIDE.md        # Guia completo de deploy
├── 🖼️ images/               # Pasta para fotos dos objetos
└── 🐍 backend/              # API Python FastAPI
    ├── main.py              # Servidor principal
    ├── requirements.txt     # Dependências Python
    ├── vercel.json         # Config específica backend
    └── Procfile           # Para outros serviços
```

### 4. Após criar no GitHub - Deploy Vercel:

1. **Vercel.com** → Login com GitHub
2. **New Project** → Import `achados-perdidos-instituto-ios`
3. **Deploy** automático! 🚀

### URLs finais:

- **Público:** `https://achados-perdidos-instituto-ios.vercel.app/`
- **Admin:** `https://achados-perdidos-instituto-ios.vercel.app/admin.html` (senha: 973439010)
- **API:** `https://achados-perdidos-instituto-ios.vercel.app/api/items`

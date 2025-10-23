# 🚀 GUIA COMPLETO DE DEPLOY - ACHADOS E PERDIDOS IOS

## 📋 Checklist Pré-Deploy

✅ **Backend FastAPI funcionando** (porta 8001)  
✅ **Frontend integrado com API**  
✅ **Configuração Vercel pronta**  
✅ **Arquivos de deploy criados**

## 🔧 1. PREPARAR REPOSITÓRIO GITHUB

### Passo 1: Criar Repositório

```bash
# 1. Vá para GitHub.com
# 2. Clique em "New Repository"
# 3. Nome: "achados-perdidos-ios"
# 4. Descrição: "Sistema Achados e Perdidos - Instituto da Oportunidade Social"
# 5. Público ou Privado (sua escolha)
# 6. NÃO marcar "Add a README" (já temos)
# 7. Clique "Create repository"
```

### Passo 2: Comandos Git no Terminal

```bash
# Navegar para pasta do projeto
cd "C:\Users\Participante IOS.DESKTOP-DHQGCTG\Documents\achados-perdidos-ios"

# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "feat: sistema completo achados e perdidos com FastAPI backend"

# Adicionar repositório remoto (SUBSTITUIR SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/achados-perdidos-ios.git

# Definir branch principal
git branch -M main

# Enviar para GitHub
git push -u origin main
```

## 🌐 2. DEPLOY NO VERCEL (OPÇÃO A - RECOMENDADA)

### Via Interface Web:

1. **Acesse:** [vercel.com](https://vercel.com)
2. **Login:** com sua conta GitHub
3. **New Project:** → "Import Git Repository"
4. **Selecione:** o repositório `achados-perdidos-ios`
5. **Configurações:**
   - **Framework Preset:** `Other`
   - **Root Directory:** `.` (ponto - raiz do projeto)
   - **Build Command:** `echo "Build completed"`
   - **Output Directory:** `.` (ponto)
   - **Install Command:** `pip install -r backend/requirements.txt`
6. **Deploy** → Aguardar 2-3 minutos

### Resultado:

- ✅ **Site:** `https://achados-perdidos-ios.vercel.app/`
- ✅ **Admin:** `https://achados-perdidos-ios.vercel.app/admin.html`
- ✅ **API:** `https://achados-perdidos-ios.vercel.app/api/items`
- ✅ **Docs:** `https://achados-perdidos-ios.vercel.app/docs`

## 🛠️ 3. DEPLOY NO VERCEL (OPÇÃO B - CLI)

### Instalar Vercel CLI:

```bash
# Instalar globalmente
npm install -g vercel

# Na pasta do projeto
cd "C:\Users\Participante IOS.DESKTOP-DHQGCTG\Documents\achados-perdidos-ios"

# Fazer deploy
vercel

# Responder prompts:
# ? Set up and deploy? → Yes
# ? Which scope? → Sua conta pessoal
# ? Link to existing project? → No
# ? What's your project's name? → achados-perdidos-ios
# ? In which directory is your code located? → ./
```

## 🔄 4. ATUALIZAÇÕES FUTURAS

### Para fazer mudanças:

```bash
# 1. Editar código
# 2. Commit e push
git add .
git commit -m "feat: nova funcionalidade"
git push

# 3. Vercel faz deploy automático! 🚀
```

## 🧪 5. TESTAR FUNCIONAMENTO COMPLETO

### Teste Multi-Dispositivo:

1. **Dispositivo 1 (Admin):**

   - Acesse: `https://SEU-PROJETO.vercel.app/admin.html`
   - Login: `973439010`
   - Adicione um item teste

2. **Dispositivo 2 (Aluno):**

   - Acesse: `https://SEU-PROJETO.vercel.app/`
   - Veja o item aparecer automaticamente
   - Faça um comentário
   - Reclame o item

3. **Volte ao Dispositivo 1:**
   - Veja comentário na página admin
   - Veja item na seção "Reclamados"
   - Confirme entrega ou devolva ao feed

## 📱 6. FUNCIONAMENTO GARANTIDO

✅ **Comentários sincronizam** entre todos dispositivos  
✅ **Claims aparecem no admin** instantaneamente  
✅ **Items adicionados** aparecem para todos  
✅ **Entregas confirmadas** removem permanentemente  
✅ **Fallback localStorage** se API falhar

## 🚨 7. CONFIGURAÇÕES PÓS-DEPLOY

### Alterar Senha Admin (IMPORTANTE):

1. Abra o arquivo `backend/main.py`
2. Linha ~200, altere:
   ```python
   correct_password = "SUA_SENHA_SUPER_SEGURA"
   ```
3. Commit e push:
   ```bash
   git add .
   git commit -m "security: alterar senha admin padrão"
   git push
   ```

### Custom Domain (Opcional):

1. **Vercel Dashboard** → Seu projeto → Settings → Domains
2. **Add Domain:** `achadosperdidos.institutodaoportunidade.org`
3. **Configurar DNS** conforme instruções

## 📊 8. MONITORAMENTO

### URLs de Monitoramento:

- **Status API:** `https://SEU-PROJETO.vercel.app/api/`
- **Logs Vercel:** Dashboard → Functions → View Logs
- **Analytics:** Dashboard → Analytics

### Backup de Dados:

- **Admin Panel:** Botão "📥 Download Backup"
- **API Direct:** `GET https://SEU-PROJETO.vercel.app/api/items`

## 🆘 9. SOLUÇÃO DE PROBLEMAS

### API não funciona:

1. Verificar logs no Vercel Dashboard
2. Testar endpoint: `/api/` (deve retornar status)
3. Verificar `vercel.json` na raiz

### Frontend não carrega:

1. Verificar se `index.html` está na raiz
2. Verificar rotas no `vercel.json`
3. Limpar cache do navegador

### Dados não sincronizam:

1. Abrir DevTools (F12)
2. Verificar Console por erros
3. Testar API health: `achadosAPI.checkHealth()`

---

## 🎯 RESUMO EXECUTIVO

**O sistema está 100% pronto para produção:**

✅ **Backend Python/FastAPI** - Escalável e robusto  
✅ **Frontend JavaScript** - Mobile-first responsivo  
✅ **Deploy automático** - GitHub → Vercel  
✅ **Multi-dispositivo** - Sincronização real-time  
✅ **Fallback offline** - Funciona sem internet  
✅ **Documentação completa** - Manutenção facilitada

**Próximo passo:** Seguir seção 1 e 2 deste guia! 🚀

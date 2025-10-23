# 📱 Achados e Perdidos - Instituto da Oportunidade Social

Um sistema web completo para gerenciar objetos perdidos e encontrados, desenvolvido especialmente para o Instituto da Oportunidade Social (IOS).

## ✨ Funcionalidades Avançadas

### 👥 Para os Alunos (Página Pública)

- **Feed Instagram-Style**: Visualização em cards dos objetos perdidos
- **Sistema de Comentários**: Alunos podem comentar para identificar items
- **Reclame seu Item**: Processo completo de reivindicação com nome completo
- **Busca Inteligente**: Filtros por título, descrição e local
- **Interface Mobile**: Design responsivo otimizado para celulares

### 🔐 Para Administração (Painel Admin)

- **Autenticação Segura**: Acesso protegido por senha
- **Gestão Completa**: Adicionar, editar e remover objetos
- **Items Reclamados**: Seção especial para gerenciar items reivindicados
- **Workflow de Entrega**: Confirmar entrega ou devolver ao feed
- **Backup Automático**: Sistema de backup em JSON

### 🎯 Sistema de Reivindicação

1. **Aluno encontra seu item** → comenta no post
2. **Aluno clica "Reclame este item"** → preenche nome completo
3. **Item sai do feed** → vai para seção "Reclamados" no admin
4. **Admin confirma identidade** → marca como "Entregue" ou "Devolver ao Feed"

## 🎨 Design Institucional

Projeto desenvolvido com as cores oficiais do IOS:

- **Roxo Institucional**: `#8B5A96` (elementos principais)
- **Laranja Vibrante**: `#FF8C42` (botões de ação)
- **Interface Limpa**: Fundo branco com detalhes em cinza

## 📁 Arquitetura do Sistema

```
achados-perdidos-ios/
├── index.html          # Interface pública dos alunos
├── admin.html          # Painel administrativo protegido
├── items.json          # Base de dados inicial
├── images/             # Repositório de fotos dos objetos
└── README.md           # Documentação completa
```

## 🚀 Guia de Uso Completo

### 🎓 Para Alunos (Interface Pública)

1. **Visualizar Feed**: Acesse `index.html` para ver todos os objetos
2. **Comentar**: Adicione comentários para ajudar na identificação
3. **Reclamar Item**:
   - Clique em "Reclame este item"
   - Preencha seu nome completo
   - Item sairá do feed automaticamente
4. **Buscar**: Use o campo de busca para filtrar objetos

### 👨‍💼 Para Administradores (Painel Admin)

1. **Login**: Acesse `admin.html`, senha: `973439010` (IOS)
2. **Adicionar Objeto**:
   - Preencha título, descrição, local e data
   - Adicione foto do objeto
   - Salve manualmente a imagem na pasta `images/`
3. **Gerenciar Items Ativos**: Visualize e remova objects do feed
4. **Gerenciar Items Reclamados**:
   - Veja quem reclamou cada item
   - Confirme entrega (remove definitivamente)
   - Devolva ao feed (se não retirado)

### 📸 Gerenciamento de Imagens

1. **Upload**: Selecione imagem no formulário admin
2. **Nomenclatura**: Sistema sugere nome automaticamente
3. **Salvamento**: Salve manualmente na pasta `images/` com nome sugerido
4. **Formatos**: JPG, PNG, GIF (recomendado: máx 2MB)

## 🔧 Instalação e Deploy

### 🏠 Servidor Local (Desenvolvimento/Teste)

```bash
# Usando Python (recomendado)
python -m http.server 8000

# Usando Node.js
npx http-server

# Usando PHP
php -S localhost:8000
```

Acesse: `http://localhost:8000`

### 🌐 Deploy em Produção

#### GitHub Pages (Gratuito)

```bash
# 1. Crie repositório no GitHub
# 2. Upload dos arquivos
git add .
git commit -m "Deploy inicial"
git push origin main

# 3. Configure Pages: Settings > Pages > Deploy from branch > main
# 4. Site disponível em: https://seuusuario.github.io/achados-perdidos-ios
```

#### Netlify (Recomendado)

1. **Arrastar e Soltar**: Arraste pasta para [netlify.com/drop](https://netlify.com/drop)
2. **GitHub Integration**: Conecte repositório para deploy automático
3. **Custom Domain**: Configure domínio personalizado se necessário
4. **HTTPS**: Habilitado automaticamente

#### Hospedagem Tradicional

1. **FTP Upload**: Envie arquivos via FileZilla ou painel de controle
2. **Configuração Web Server**: Certifique-se que serve arquivos estáticos
3. **SSL/HTTPS**: Configure certificado (recomendado)
4. **Domínio**: Configure DNS para apontar para servidor

### 🔒 Configurações de Segurança para Produção

#### Alterar Senha Admin

```javascript
// Em admin.html, linha ~120, altere:
if (password === 'SUA_SENHA_SUPER_SEGURA_AQUI') {
```

#### Configurações Recomendadas

- **HTTPS Obrigatório**: Para proteção de dados
- **Backup Regular**: Configure rotina de backup semanal
- **Monitoramento**: Verifique logs de acesso regularmente
- **Senha Forte**: Mínimo 12 caracteres com números e símbolos

## 🔄 Fluxo de Dados e Sincronização

### localStorage (Browser Database)

```javascript
// Estrutura de dados principal:
lostItems: [...] // Array de objetos perdidos
claimedItems: [...] // IDs dos items reclamados
claimedData: {...} // Dados dos reclamantes
comments: {...} // Comentários por item
```

### Sincronização Automática

- **Admin → Público**: Mudanças aparecem instantaneamente
- **Persistência**: Dados salvos no navegador permanentemente
- **Backup JSON**: Download manual para arquivamento
- **Reset**: Função para restaurar dados originais

## 📊 Relatórios e Estatísticas

### Métricas Disponíveis (via localStorage)

- Total de objetos cadastrados
- Objetos reclamados vs. não reclamados
- Histórico de comentários
- Locais com mais achados
- Estatísticas de entrega

### Exportação de Dados

```javascript
// No console do navegador (F12):
console.table(JSON.parse(localStorage.getItem("lostItems")));
console.table(JSON.parse(localStorage.getItem("claimedData")));
```

## 🆘 Troubleshooting e Manutenção

### Problemas Comuns

1. **Imagens não aparecem**:

   - Verifique se estão na pasta `images/`
   - Confirme nomes dos arquivos (sem espaços/acentos)

2. **Dados perdidos**:

   - Use função "Resetar para Original" no admin
   - Restaure backup JSON baixado anteriormente

3. **Site não carrega**:
   - Teste em modo incógnito (limpa cache)
   - Verifique se servidor local está rodando
   - Confirme que JavaScript está habilitado

### Manutenção Regular

- **Backup Semanal**: Baixe JSON de backup via admin
- **Limpeza de Imagens**: Remova fotos de items já entregues
- **Verificação de Links**: Teste todas as funcionalidades mensalmente
- **Atualização de Senha**: Altere senha admin trimestralmente

## 📱 Compatibilidade e Performance

### Navegadores Suportados

- **Chrome**: 80+ (recomendado)
- **Firefox**: 75+
- **Safari**: 13+
- **Edge**: 80+
- **Mobile**: iOS Safari 13+, Android Chrome 80+

### Performance Otimizada

- **Images**: Compressão automática via CSS
- **Cache**: Utiliza cache do navegador
- **Mobile**: Carregamento otimizado para 3G/4G
- **Offline**: Funciona offline após primeiro carregamento

## 📞 Suporte e Contato

### Para Problemas Técnicos

1. Verifique a seção de Troubleshooting acima
2. Teste em navegador diferente/modo incógnito
3. Confirme que seguiu todas as instruções de instalação
4. Verifique console do navegador (F12) para erros JavaScript

### Para Personalização

- **Cores**: Modifique variáveis CSS no início dos arquivos
- **Textos**: Altere strings diretamente no HTML
- **Layout**: Ajuste classes CSS conforme necessário
- **Funcionalidades**: Consulte comentários no código JavaScript

---

**Desenvolvido especialmente para Instituto da Oportunidade Social (IOS)** 💜🧡

_Sistema completo de achados e perdidos com interface moderna, segurança robusta e funcionalidades avançadas para uso institucional profissional._

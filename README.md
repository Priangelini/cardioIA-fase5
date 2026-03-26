# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Cap 1 - Assistente Cardiológico Inteligente: Experiência do Paciente

## 👨‍💻 Equipe de Desenvolvimento
### 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/luana-porto-pereira-gomes/">Luana Porto Pereira Gomes</a>
- <a href="https://www.linkedin.com/in/luma-x">Luma Oliveira</a>
- <a href="https://www.linkedin.com/in/priscilla-oliveira-023007333/">Priscilla Oliveira </a>
- <a href="https://www.linkedin.com/in/paulobernardesqs?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Paulo Bernardes</a>

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

---

# 📌 Sobre o Projeto

O CardioIA é um assistente virtual desenvolvido para simular um atendimento inicial na área de saúde cardiovascular.

Nesta fase, o projeto evoluiu para uma abordagem prática de IA conversacional, integrando:

- Interface de chat (frontend)
- Lógica de aplicação (backend)
- Motor de IA (IBM Watson Assistant)

O objetivo é oferecer uma experiência guiada, clara e acessível ao usuário.

---

# 🎯 Objetivo

Desenvolver um sistema capaz de:

- Simular um atendimento inicial ao paciente
- Coletar informações de saúde
- Interpretar dados informados
- Fornecer orientações básicas
- Permitir navegação fluida entre opções

---

# ⚙️ Arquitetura da Solução

O sistema é dividido em três camadas principais:

🔹 1. Frontend
Responsável pela interface com o usuário.
  - Exibição do chat
  - Captura de mensagens
  - Envio de requisições
    
🔹 2. Backend
Responsável pela comunicação com o Watson.
  - Processamento das requisições
  - Integração com API do Watson
  - Tratamento de respostas
    
🔹 3. Watson Assistant
Responsável pela inteligência conversacional.
  - Fluxos de conversa (Actions)
  - Regras de decisão
  - Respostas dinâmicas

---

# 🔄 Fluxo do Sistema

```text
Usuário → Frontend → Backend → Watson → Backend → Frontend → Usuário
```

---

# 🤖 Sobre o IBM Watson Assistant

O Watson Assistant foi utilizado como motor de IA conversacional.

- Actions: fluxos principais de conversa
- Steps: etapas dentro de cada fluxo
- Conditions: lógica condicional
- Subactions: navegação entre fluxos

No projeto, utilizamos:

- Estrutura modular de ações
- Navegação entre menus
- Condições baseadas em entrada do usuário
- Controle de fluxo com “Go to” e “End action”

---

# 🔄 Navegação do Assistente

O sistema foi estruturado com duas ações principais:

🟢 Oi (Entrada inicial)
  - Saudação inicial
  - Apresentação do sistema
  - Primeiro contato com o usuário
  
🟢 Menu (Navegação)
  Escolha de temas:
  - Dor no peito
  - Pressão arterial
  - Frequência cardíaca
  - Encerrar

Após cada resposta, o usuário retorna ao Menu, garantindo um fluxo contínuo e organizado.

---

# ❤️ Funcionalidades

### Frequência Cardíaca
- Entrada de bpm
- Classificação automática
- Orientação ao usuário

### Pressão Arterial
- Avaliação dos valores
- Classificação
- Retorno ao menu

### Dor no Peito
- Orientações iniciais
- Recomendação de avaliação médica

### Encerrar
- Exibe mensagem de despedida
- Finalização da conversa

---

## 📸 Demonstração

### 🔹 Menu principal
<p align="center">
  <img src="./assets/2-menu.png" width="50%">
</p>

### 🔹 Fluxo Frequência Cardíaca
<p align="center">
  <img src="./assets/3-fluxo.png" width="50%">
</p>

### 🔹 Fluxo Pressão Arterial
<p align="center">
  <img src="./assets/4-fluxo.png" width="50%">
</p>

### 🔹 Fluxo Encerramento
<p align="center">
  <img src="./assets/5-fluxo.png" width="50%">
</p>

### 🔹 Estrutura no Watson
<p align="center">
  <img src="./assets/1-actions.png" width="55%">
</p>

---

# 🧩 Tecnologias Utilizadas

## Frontend
- HTML
- CSS
- JavaScript
  
## Backend
- Python
- Flask

## IA
- IBM Watson Assistant
  
## Versionamento
- GitHub

---

# 🚀 Como Executar o Projeto

## 🧠Backend

### 1. Acesse a pasta Backend
```bash
cd backend
```
### 2.  Instale as dependências:
```bash
pip install -r requirements.txt
```
### 3.  Execute o servidor:
```bash
python app.py
```

## 💻Frontend

### 1. Acesse a pasta do frontend:
```bash
cd frontend
```

### 2. Abra o arquivo:
```bash
index.html
```

## 🌐 Acesso

Após iniciar:
- Backend: http://localhost:5000
- Frontend: abrir no navegador

---

## 🔐 Configuração do Watson Assistant

Para executar o projeto corretamente, é necessário configurar as credenciais do IBM Watson Assistant.

Crie um arquivo `.env` na pasta `backend` com as seguintes variáveis:

```env
WATSON_API_KEY=your_api_key_here
WATSON_URL=your_service_url_here
WATSON_ASSISTANT_ID=your_assistant_id_here
```

## 📌 Onde obter essas informações:

1. Acesse o IBM Cloud
2. Entre no serviço Watson Assistant
3. Vá em:
      Service credentials (para API Key e URL)
      Assistant settings (para Assistant ID)
   
---

# 🎥 Demonstração em Vídeo

[🔗 Clique aqui para assistir ao vídeo](         ) <br>

---

## 📁 Estrutura de pastas

```
cardioIA-fase5/
│
├── assets/
│   ├── 1-ações.png
│   ├── 2-menu.png
│   ├── 3-fluxo.png
│   ├── 4-fluxo.png
│   ├── 5-fluxo.png
│   └── logo-fiap.png
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── watson/
│   └── cardioia_watson_assistant.json
│
└── README.md
```

---

# 🗃 Histórico de lançamentos

* 0.5.0 - Assistente Conversacional com Watson
* 0.4.0 - Evolução do sistema
* 0.3.0 - Integração de dados
* 0.2.0 - Modelagem inicial

---

# 🏁 Conclusão

O CardioIA evoluiu de um sistema de análise de dados para um assistente inteligente interativo, demonstrando na prática como a IA pode melhorar a experiência do paciente.

A utilização do Watson Assistant permitiu:

- Navegação fluida
- Respostas dinâmicas
- Estrutura organizada de atendimento

---

# 📌 Observações

- Projeto com fins educacionais
- Não substitui avaliação médica
- As orientações são informativas

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

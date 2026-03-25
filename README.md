# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Cap 1 - Assistente Cardiológico Inteligente: Experiência do Paciente

## Beginner Coders

## 👨‍🎓 Integrantes:
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

## 📌 Sobre o Projeto

Este projeto representa a evolução do CardioIA ao longo das fases do curso de Inteligência Artificial da FIAP.

Nesta etapa, deixamos de apenas analisar dados e passamos a simular uma experiência real de atendimento ao paciente, utilizando um assistente conversacional.

A proposta foi criar um chatbot capaz de conduzir uma conversa simples, coletar informações básicas de saúde e responder de forma clara e organizada, como um primeiro contato em um atendimento médico.

O foco não está apenas na tecnologia, mas na experiência: fazer o usuário se sentir guiado, entendido e bem orientado.

---

## 🎯 Objetivo

Desenvolver um assistente virtual capaz de:

.  Auxiliar usuários com dúvidas cardiovasculares básicas
.  Simular um atendimento inicial inteligente
.  Melhorar a experiência do paciente com navegação fluida
.  Demonstrar aplicação prática de IA conversacional

---


## 🤖 Sobre o IBM Watson Assistant

O IBM Watson Assistant é uma plataforma de IA conversacional que permite criar chatbots inteligentes através de:

.  Actions: fluxos principais de conversa
.  Steps: etapas dentro de cada fluxo
.  Conditions: regras de decisão
.  Subactions: navegação entre fluxos

No projeto, utilizamos:

.  Estrutura modular de ações
.  Navegação entre menus
.  Condições baseadas em entrada do usuário
.  Controle de fluxo com “Go to” e “End action”

---

## ⚙️ Arquitetura da Solução

O sistema é composto por:

🤖 Watson Assistant → responsável pelo fluxo conversacional
💻 Frontend (chat) → interface de interação com o usuário
🧠 Lógica de decisão → implementada nos Steps do Watson

Fluxo geral:

Usuário → Menu → Escolha de tema → Entrada de dados → Resposta → Retorno ao Menu 

---


## 🔄 Fluxo de Navegação

O sistema foi estruturado com duas ações principais:

🟢 Oi (Entrada inicial)
  .  Saudação
  .  Apresentação do sistema
  .  Primeiro contato com o usuário
  
🟢 Menu (Navegação)
  .  Escolha de temas:
  .  Dor no peito
  .  Pressão arterial
  .  Frequência cardíaca
  .  Encerrar

Após cada resposta, o usuário retorna ao Menu, garantindo um fluxo contínuo e organizado.

---


## ❤️ Frequência Cardíaca

Fluxo:

  1. Usuário informa valor
  2. Sistema classifica:
    .  🔴 Alta (> 100 bpm)
    .  🟡 Normal (60–100 bpm)
    .  🔵 Baixa (< 60 bpm)
  3.  Retorna orientação
  4.  Redireciona para o Menu

---


## 🩺 Pressão Arterial

.  Avaliação de valores informados
.  Classificação do estado
.  Retorno ao Menu

---


## ⚠️ Dor no Peito

.  Orientações iniciais
.  Recomendações de atenção médica
.  Retorno ao Menu

---

## 🚪 Encerrar

.  Finaliza o atendimento
.  Exibe mensagem de despedida
.  Encerra a ação

---

## 🤖 Configuração do Watson Assistant

O arquivo de exportação do assistente está disponível em:

/watson/cardioia_watson_assistant.json

📥 Como importar no Watson:

1.  Acesse o IBM Watson Assistant
2.  Vá em Import/Export
3.  Clique em Import
4.  Selecione o arquivo JSON
   
O assistente será carregado com todos os fluxos

---

## 📸 Demonstração

###Menu principal




###Fluxo Frequência Cardíaca




###Fluxo Pressão Arterial




###Fluxo Encerramento



---


## 🚀 Como Executar o Projeto

1.  Importar o JSON no Watson (conforme instruções acima)
2.  Configurar o ambiente do Watson Assistant
3.  Integrar com frontend (se aplicável)
4.  Iniciar interação via chat

---

## 🧩 Tecnologias Utilizadas
.  IBM Watson Assistant
.  JavaScript / Frontend (se aplicável)
.  HTML / CSS
.  GitHub

---

## Links:
[🔗 Clique aqui para assistir ao vídeo](         ) <br>

---

## 📁 Estrutura de pastas


---

## 🗃 Histórico de lançamentos
0.5.0 - Fase 5 - Assistente Conversacional com Watson
0.4.0 - Evolução do sistema
0.3.0 - Integração de dados
0.2.0 - Modelagem inicial
Estrutura inicial do projeto

---

## 🏁 Conclusão

O CardioIA evoluiu de um sistema de análise de dados para um assistente inteligente interativo, demonstrando na prática como a IA pode melhorar a experiência do paciente.

A utilização do Watson Assistant permitiu:

.  Navegação fluida
.  Respostas dinâmicas
.  Estrutura organizada de atendimento

---


## 📌 Observações

.  Projeto com fins educacionais
.  Não substitui avaliação médica
.  As orientações são informativas

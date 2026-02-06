# Assistente Financeiro com IA

## Descrição do Projeto

Este projeto consiste na criação de um **Assistente Financeiro Digital**, guiado por princípios de **IA generativa, Python, dados e UX**, com foco em relacionamento financeiro e educação do usuário.

A solução permite interações em **linguagem natural**, fornecendo respostas claras, seguras e contextualizadas sobre temas financeiros, além de realizar **simulações simples** e **explicações de produtos financeiros**.

O objetivo é consolidar o aprendizado da trilha, aplicando boas práticas técnicas e de experiência do usuário.

---

## Objetivos

* Criar uma experiência digital orientada ao usuário
* Simular o uso de IA generativa em um contexto financeiro
* Aplicar conceitos de Python, lógica e organização de código
* Oferecer respostas educativas, claras e seguras
* Demonstrar persistência de contexto e entendimento de intenção

---

## Funcionalidades

*  Interação em linguagem natural
*  FAQs financeiros inteligentes
*  Simulações financeiras demonstrativas
*  Explicação de produtos financeiros
*  Persistência de contexto por usuário
*  Respostas seguras (sem aconselhamento financeiro definitivo)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** – criação da API
* **Uvicorn** – servidor local
* **JSON** – base de dados simples (FAQs)
* **VS Code** – ambiente de desenvolvimento

> A integração com APIs de IA generativa (ex: OpenAI) pode ser adicionada como evolução do projeto.

---

## 📁 Estrutura do Projeto

```
assistente-financeiro-ia/
│
├── app/
│   ├── main.py
│   ├── ia/
│   │   └── assistente.py
│   ├── services/
│   │   ├── faq_service.py
│   │   ├── simulacoes.py
│   │   └── produtos.py
│   ├── memory/
│   │   └── contexto.py
│   └── data/
│       └── faqs.json
│
├── .env
├── requirements.txt
└── README.md
```

---

## Como Executar o Projeto

### Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar a aplicação

```bash
uvicorn app.main:app --reload
```

### Acessar a documentação da API

```
http://127.0.0.1:8000/docs
```

---

## Exemplos de Perguntas

* "O que é CDI?"
* "O que é a taxa Selic?"
* "Simular juros de um investimento"
* "Me explique como funciona um cartão de crédito"
* "Como funciona um empréstimo pessoal?"

---

## Experiência do Usuário (UX)

O projeto foi desenvolvido com foco em:

* Linguagem simples e acessível
* Respostas objetivas e educativas
* Clareza nas simulações (valores demonstrativos)
* Segurança na comunicação financeira
* Redução de complexidade técnica para o usuário final

---

## Observações Importantes

* As simulações financeiras são **apenas demonstrativas**
* O assistente não fornece recomendações financeiras definitivas
* O objetivo é educacional e experimental

---

## Possíveis Evoluções

* Integração com IA generativa real (OpenAI, Azure, etc.)
* Criação de interface web (React ou HTML/CSS)
* Persistência de contexto em banco de dados
* Extração automática de valores a partir da pergunta
* Autenticação de usuários

---

## 👨‍💻 Autor

Projeto desenvolvido como parte de um **desafio educacional em IA, Python e UX**, com foco em soluções digitais para relacionamento financeiro.


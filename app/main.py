from fastapi import FastAPI
from app.ia.assistente import responder

app = FastAPI(title="Assistente Financeiro IA")

@app.post("/chat")
def chat(mensagem: str, usuario_id: str):
    resposta = responder(mensagem, usuario_id)
    return {"resposta": resposta}

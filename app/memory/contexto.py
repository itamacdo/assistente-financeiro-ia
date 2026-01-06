contextos = {}

def salvar_contexto(usuario_id, pergunta, resposta):
    if usuario_id not in contextos:
        contextos[usuario_id] = []

    contextos[usuario_id].append({
        "pergunta": pergunta,
        "resposta": resposta
    })

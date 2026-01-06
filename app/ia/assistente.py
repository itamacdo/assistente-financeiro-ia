from app.services.faq_service import buscar_faq
from app.services.simulacoes import simular
from app.services.produtos import explicar_produto
from app.memory.contexto import salvar_contexto

def responder(mensagem, usuario_id):
    mensagem_lower = mensagem.lower()

    if "simular" in mensagem_lower or "juros" in mensagem_lower:
        resposta = simular(mensagem_lower)

    elif "cartão" in mensagem_lower or "empréstimo" in mensagem_lower:
        resposta = explicar_produto(mensagem_lower)

    else:
        resposta = buscar_faq(mensagem_lower)

    salvar_contexto(usuario_id, mensagem, resposta)
    return resposta

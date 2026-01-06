import json

def buscar_faq(pergunta):
    with open("app/data/faqs.json", "r", encoding="utf-8") as f:
        faqs = json.load(f)

    for chave, resposta in faqs.items():
        if chave in pergunta:
            return resposta

    return "Não encontrei essa informação. Pode reformular?"

def explicar_produto(texto):
    if "cartão" in texto:
        return (
            "O cartão de crédito permite compras com pagamento futuro. "
            "É importante controlar o limite e evitar juros do rotativo."
        )

    if "empréstimo" in texto:
        return (
            "O empréstimo pessoal oferece crédito imediato, "
            "mas deve ser avaliado considerando taxas e prazos."
        )

    return "Produto não identificado."

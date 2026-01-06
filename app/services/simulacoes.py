def simular(texto):
    valor = 1000
    juros = 0.02
    meses = 12

    total = valor * ((1 + juros) ** meses)

    return (
        f"Simulação simples:\n"
        f"Valor inicial: R$ {valor}\n"
        f"Juros: 2% ao mês\n"
        f"Total após {meses} meses: R$ {total:.2f}"
    )

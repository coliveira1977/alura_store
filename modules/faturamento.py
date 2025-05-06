from modules.common import carregar_dados, URLS, NOMES_LOJAS, plt

def calcular_faturamento():
    # Carrega os dados usando o módulo common
    dataframes = carregar_dados(URLS)

    # Calcula o faturamento total
    faturamentos = [
        df["Preço"].sum() if df is not None else 0
        for df in dataframes
    ]

    # Exibe os resultados
    for nome, faturamento in zip(NOMES_LOJAS, faturamentos):
        valor_formatado = f"R$ {faturamento:,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
        print(f"Faturamento total {nome}: {valor_formatado}")

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(NOMES_LOJAS, faturamentos, color="blue")
    plt.title("Faturamento Total por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, faturamentos):
        valor_formatado = f"R$ {valor:,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            valor_formatado,
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
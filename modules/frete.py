from modules.common import carregar_dados, URLS, NOMES_LOJAS, plt

def calcular_media_frete():
    # Carrega os dados usando o módulo common
    dataframes = carregar_dados(URLS)

    # Calcula a média do frete
    medias_frete = [
        df["Frete"].mean() if df is not None else 0
        for df in dataframes
    ]

    # Exibe os resultados
    for nome, media in zip(NOMES_LOJAS, medias_frete):
        print(f"Média do frete {nome}: R$ {media:,.2f}".replace(".", ","))

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(NOMES_LOJAS, medias_frete, color="green")
    plt.title("Média do Valor do Frete por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Média do Frete (R$)")
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, medias_frete):
        valor_formatado = f"R$ {valor:,.2f}".replace(".", ",")
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            valor_formatado,
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
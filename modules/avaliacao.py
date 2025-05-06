from modules.common import carregar_dados, URLS, NOMES_LOJAS, plt

def calcular_media_avaliacao():
    # Carrega os dados usando o módulo common
    dataframes = carregar_dados(URLS)

    # Calcula a média de avaliação
    medias_avaliacao = [
        df["Avaliação da compra"].mean() if df is not None else 0
        for df in dataframes
    ]

    # Exibe os resultados
    for nome, media in zip(NOMES_LOJAS, medias_avaliacao):
        print(f"Média de avaliação {nome}: {media:.2f}")

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(NOMES_LOJAS, medias_avaliacao, color="orange")
    plt.title("Média de Avaliação das Compras por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Média de Avaliação")
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, medias_avaliacao):
        valor_formatado = f"{valor:.2f}".replace(".", ",")
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            valor_formatado,
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
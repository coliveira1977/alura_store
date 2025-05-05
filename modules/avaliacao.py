import pandas as pd
import matplotlib.pyplot as plt

def calcular_media_avaliacao():
    urls = [
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv",
    ]
    nomes_lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

    # Carrega os dados e calcula a média de avaliação
    medias_avaliacao = [
        pd.read_csv(url)["Avaliação da compra"].mean()
        for url in urls
    ]

    # Exibe os resultados
    for nome, media in zip(nomes_lojas, medias_avaliacao):
        print(f"Média de avaliação {nome}: {media:.2f}")

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(nomes_lojas, medias_avaliacao, color="orange")
    plt.title("Média de Avaliação das Compras por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Média de Avaliação")
    plt.ylim(0, 5)
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, medias_avaliacao):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{valor:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
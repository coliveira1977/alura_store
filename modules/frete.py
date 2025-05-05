import pandas as pd
import matplotlib.pyplot as plt

def calcular_media_frete():
    urls = [
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv",
    ]
    nomes_lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

    # Carrega os dados e calcula a média do frete
    medias_frete = [
        pd.read_csv(url)["Frete"].mean()
        for url in urls
    ]

    # Exibe os resultados
    for nome, media in zip(nomes_lojas, medias_frete):
        print(f"Média do frete {nome}: R$ {media:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(nomes_lojas, medias_frete, color="royalblue")
    plt.title("Média do Frete por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Média do Frete (R$)")
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, medias_frete):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
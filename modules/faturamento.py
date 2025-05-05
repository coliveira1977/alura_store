import pandas as pd
import matplotlib.pyplot as plt

def calcular_faturamento():
    urls = [
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv",
    ]
    nomes_lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

    # Carrega os dados e calcula o faturamento
    faturamentos = {
        nome: pd.read_csv(url)["Preço"].sum()
        for nome, url in zip(nomes_lojas, urls)
    }

    # Exibe os resultados
    for loja, valor in faturamentos.items():
        print(f"Faturamento {loja}: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Gera o gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(faturamentos.keys(), faturamentos.values(), color="mediumseagreen")
    plt.title("Faturamento das Lojas")
    plt.xlabel("Loja")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout()

    # Adiciona os valores no topo das barras
    for bar, valor in zip(bars, faturamentos.values()):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()
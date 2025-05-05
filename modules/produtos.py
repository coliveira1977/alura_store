import pandas as pd
import matplotlib.pyplot as plt

def calcular_faturamento_por_categoria():
    urls = [
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv",
    ]
    nomes_lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

    # Carrega os dados
    dados_lojas = [pd.read_csv(url) for url in urls]

    # Calcula o faturamento por categoria
    categorias = [df.groupby("Categoria do Produto")["Preço"].sum() for df in dados_lojas]
    df_categorias = pd.concat(categorias, axis=1)
    df_categorias.columns = nomes_lojas
    df_categorias = df_categorias.fillna(0)

    # Exibe os resultados
    print(df_categorias)

    # Gera gráficos de pizza
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    for ax, loja in zip(axs.flatten(), nomes_lojas):
        valores = df_categorias[loja]
        ax.pie(
            valores,
            labels=valores.index,
            autopct="%1.1f%%",
            startangle=90,
            counterclock=False,
        )
        ax.set_title(f"Participação das Categorias - {loja}")

    plt.tight_layout()
    plt.show()
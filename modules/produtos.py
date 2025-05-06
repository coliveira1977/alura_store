from modules.common import carregar_dados, URLS, NOMES_LOJAS, plt

def calcular_faturamento_por_categoria():
    # Carrega os dados usando o módulo common
    dataframes = carregar_dados(URLS)

    # Configura o layout para exibir 4 gráficos de pizza em subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.flatten()  # Transforma a matriz de eixos em uma lista para iteração

    for i, (df, nome_loja) in enumerate(zip(dataframes, NOMES_LOJAS)):
        if df is not None:
            # Calcula o faturamento por categoria
            faturamento_por_categoria = df.groupby("Categoria do Produto")["Preço"].sum()

            # Calcula o percentual de cada categoria
            total_faturamento = faturamento_por_categoria.sum()
            percentual_por_categoria = (faturamento_por_categoria / total_faturamento) * 100

            # Agrupa categorias com menos de 2% em "Outros"
            categorias_agrupadas = {}
            for categoria, percentual in percentual_por_categoria.items():
                if percentual < 2:
                    categorias_agrupadas["Outros"] = categorias_agrupadas.get("Outros", 0) + faturamento_por_categoria[categoria]
                else:
                    categorias_agrupadas[categoria] = faturamento_por_categoria[categoria]

            # Prepara os dados para o gráfico
            labels = list(categorias_agrupadas.keys())
            valores = list(categorias_agrupadas.values())

            # Gera o gráfico de pizza no subplot correspondente
            axes[i].pie(
                valores,
                labels=labels,
                autopct=lambda p: f"{p:.1f}%".replace(".", ","),  # Exibe apenas o percentual com vírgula como separador decimal
                startangle=90,
                colors=plt.cm.Paired.colors
            )
            axes[i].set_title(f"Faturamento por Categoria - {nome_loja}")

    # Ajusta o layout e exibe os gráficos
    plt.tight_layout()
    plt.show()
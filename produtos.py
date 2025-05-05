import csv
import pandas as pd
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

# Carrega os DataFrames das lojas usando list comprehension
dfs = [pd.read_csv(arquivo) for arquivo in arquivos]

# Calcula o agrupamento e soma por categoria para cada loja usando list comprehension
cats = [df.groupby('Categoria do Produto')['Preço'].sum() for df in dfs]

# Concatena os resultados em um único DataFrame, alinhando pelo índice (categoria)
df_categorias = pd.concat(cats, axis=1)
df_categorias.columns = nomes_lojas
df_categorias = df_categorias.fillna(0)

# Ordena pelo total de vendas (opcional)
df_categorias = df_categorias.loc[df_categorias.sum(axis=1).sort_values(ascending=False).index]

# Impressão formatada
print(f"{'Categoria':<25} | " + " | ".join([f"{loja:^15}" for loja in nomes_lojas]))
print("-" * (25 + 3 + 16 * len(nomes_lojas)))
for categoria, row in zip(df_categorias.index, df_categorias.values):
    print(f"{categoria:<25} | " + " | ".join(
        f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.').rjust(15)
        for valor in row
    ))

# Gráfico de pizza para cada loja
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
for ax, loja in zip(axs.flatten(), nomes_lojas):
    valores = df_categorias[loja]
    categorias_labels = df_categorias.index
    ax.pie(
        valores,
        labels=categorias_labels,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
    )
    ax.set_title(f'Participação das Categorias - {loja}')

plt.tight_layout()
plt.show()

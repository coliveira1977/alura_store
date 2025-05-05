import pandas as pd
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

# Carrega os DataFrames das lojas usando list comprehension
dfs = [pd.read_csv(arquivo) for arquivo in arquivos]

# Conta quantas vezes cada produto aparece em cada loja (cada linha = 1 unidade vendida)
produtos_por_loja = [df['Produto'].value_counts() for df in dfs]

# Soma total de produtos vendidos (todas as lojas)
produtos_total = sum(produtos_por_loja).groupby('Produto').sum() if len(produtos_por_loja) > 1 else produtos_por_loja[0]

# Função para obter mais e menos vendidos
def mais_menos_vendidos(produtos):
    return produtos.idxmax(), produtos.max(), produtos.idxmin(), produtos.min()

# Exibe mais e menos vendidos no total
mais_nome, mais_qtd, menos_nome, menos_qtd = mais_menos_vendidos(produtos_total)
print(f"Produto mais vendido (total): {mais_nome} - {mais_qtd} unidades")
print(f"Produto menos vendido (total): {menos_nome} - {menos_qtd} unidades\n")

# Exibe mais e menos vendidos por loja
for nome, produtos_loja in zip(nomes_lojas, produtos_por_loja):
    mais_nome, mais_qtd, menos_nome, menos_qtd = mais_menos_vendidos(produtos_loja)
    print(f"{nome}:")
    print(f"  Produto mais vendido: {mais_nome} - {mais_qtd} unidades")
    print(f"  Produto menos vendido: {menos_nome} - {menos_qtd} unidades\n")

# Função para preparar dados para o gráfico de pizza (apenas mais e menos vendidos)
def dados_pizza(produtos):
    mais_nome, mais_qtd, menos_nome, menos_qtd = mais_menos_vendidos(produtos)
    valores = [mais_qtd, menos_qtd]
    labels = [f'Mais vendido: {mais_nome}', f'Menos vendido: {menos_nome}']
    return valores, labels

# Gráfico de pizza para o total de todas as lojas
valores_total, labels_total = dados_pizza(produtos_total)
plt.figure(figsize=(6, 6))
plt.pie(valores_total, labels=labels_total, autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title('Produtos Mais e Menos Vendidos - Total de Todas as Lojas')
plt.tight_layout()
plt.show()

# Gráfico de pizza para cada loja
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
for ax, nome, produtos_loja in zip(axs.flatten(), nomes_lojas, produtos_por_loja):
    valores, labels = dados_pizza(produtos_loja)
    ax.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.set_title(f'Produtos Mais e Menos Vendidos - {nome}')
plt.tight_layout()
plt.show()

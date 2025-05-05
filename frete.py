import pandas as pd
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

# Calcula a média do frete para cada loja
medias_frete = [
    pd.read_csv(arquivo)['Frete'].mean()
    for arquivo in arquivos
]

# Exibe as médias formatadas
print(f"{'Loja':<8} | {'Média do Frete':>18}")
print("-" * 30)
for nome, media in zip(nomes_lojas, medias_frete):
    print(f"{nome:<8} | R$ {media:15,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

# Gráfico de barras
plt.figure(figsize=(8, 5))
bars = plt.bar(nomes_lojas, medias_frete, color='royalblue')
plt.title('Média do Frete por Loja')
plt.xlabel('Loja')
plt.ylabel('Média do Frete (R$)')
plt.tight_layout()

# Adiciona os valores no topo das barras, formatados em reais
for bar, valor in zip(bars, medias_frete):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.show()

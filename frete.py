import pandas as pd
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = [f'loja{i+1}' for i in range(len(arquivos))]

# Calcula a média do frete para cada loja (com list comprehension)
medias_frete = [pd.read_csv(arq)['Frete'].mean() for arq in arquivos]

# Exibe as médias formatadas
print(f"{'Loja':<8} | {'Média do Frete':>18}")
print("-" * 30)
[
    print(f"{loja:<8} | R$ {media:15,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    for loja, media in zip(nomes_lojas, medias_frete)
]

# Gráfico de barras com anotações
plt.figure(figsize=(8, 5))
bars = plt.bar(nomes_lojas, medias_frete, color='royalblue')
plt.title('Média do Frete por Loja')
plt.xlabel('Loja')
plt.ylabel('Média do Frete (R$)')
plt.tight_layout()

[
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
        ha='center',
        va='bottom',
        fontsize=10
    )
    for bar, valor in zip(bars, medias_frete)
]

plt.show()

import csv
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

def media_avaliacao(arquivo):
    with open(arquivo, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        avaliacoes = [float(row['Avaliação da compra']) for row in reader if row['Avaliação da compra'].replace('.', '', 1).isdigit()]
    return sum(avaliacoes) / len(avaliacoes) if avaliacoes else 0

# Calcula as médias usando list comprehension
medias_avaliacao = [media_avaliacao(arquivo) for arquivo in arquivos]

# Impressão formatada
print(f"{'Loja':<8} | {'Média de Avaliação':>18}")
print("-" * 30)
for nome, media in zip(nomes_lojas, medias_avaliacao):
    print(f"{nome:<8} | {media:18.2f}")

# Gráfico de barras
plt.figure(figsize=(8, 5))
bars = plt.bar(nomes_lojas, medias_avaliacao, color='orange')
plt.title('Média de Avaliação das Compras por Loja')
plt.xlabel('Loja')
plt.ylabel('Média de Avaliação')
plt.ylim(0, 5)
plt.tight_layout()

# Adiciona os valores no topo das barras
for bar, valor in zip(bars, medias_avaliacao):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{valor:.2f}',
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.show()
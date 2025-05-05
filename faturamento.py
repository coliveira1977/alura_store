import csv
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

def faturamento_loja(arquivo):
    with open(arquivo, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return sum(float(row['Preço'].replace(',', '.')) for row in reader if row['Preço'].replace('.', '', 1).isdigit())

# Calcula os faturamentos usando list comprehension
faturamentos = [faturamento_loja(arquivo) for arquivo in arquivos]

# Impressão formatada
print(f"{'Loja':<8} | {'Faturamento':>18}")
print("-" * 30)
for nome, valor in zip(nomes_lojas, faturamentos):
    print(f"{nome:<8} | R$ {valor:15,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

# Gráfico de barras
plt.figure(figsize=(8, 5))
bars = plt.bar(nomes_lojas, faturamentos, color='skyblue')
plt.title('Faturamento das Lojas')
plt.xlabel('Loja')
plt.ylabel('Faturamento (R$)')
plt.tight_layout()

# Adiciona os valores no topo das barras, formatados em reais
for bar, valor in zip(bars, faturamentos):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.show()
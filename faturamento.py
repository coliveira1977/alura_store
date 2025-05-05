import csv
import matplotlib.pyplot as plt

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']
faturamentos = []

print(f"{'Loja':<8} | {'Faturamento':>18}")
print("-" * 30)
for nome, arquivo in zip(nomes_lojas, arquivos):
    faturamento = 0
    with open(arquivo, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                faturamento += float(row['Preço'].replace(',', '.'))
            except Exception:
                pass  # Ignora linhas com erro de conversão
    faturamentos.append(faturamento)
    print(f"{nome:<8} | R$ {faturamento:15,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

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
import csv
from collections import defaultdict

arquivos = ['loja_1.csv', 'loja_2.csv', 'loja_3.csv', 'loja_4.csv']
nomes_lojas = ['loja1', 'loja2', 'loja3', 'loja4']

# Dicionário: {categoria: {loja1: valor, loja2: valor, ...}}
categorias = defaultdict(lambda: defaultdict(float))

for nome_loja, arquivo in zip(nomes_lojas, arquivos):
    with open(arquivo, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            categoria = row['Categoria do Produto']
            try:
                preco = float(row['Preço'].replace(',', '.'))
                categorias[categoria][nome_loja] += preco
            except Exception:
                pass  # Ignora linhas com erro de conversão

# Ordena as categorias pelo faturamento total (todas as lojas), ordem decrescente
categorias_ordenadas = sorted(
    categorias.items(),
    key=lambda item: sum(item[1].get(loja, 0) for loja in nomes_lojas),
    reverse=True
)

# Cabeçalho
header = f"{'Categoria':<25} | " + " | ".join([f"{loja:^15}" for loja in nomes_lojas])
print(header)
print("-" * len(header))

# Linhas da tabela
for categoria, valores in categorias_ordenadas:
    linha = f"{categoria:<25} | " + " | ".join(
        f"R$ {valores.get(loja, 0):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.').rjust(15)
        for loja in nomes_lojas
    )
    print(linha)

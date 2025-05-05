# Alura Store - Análise de Vendas

Este projeto realiza a análise de vendas de quatro lojas fictícias, utilizando dados em arquivos CSV. O objetivo é comparar o desempenho das lojas, analisar o faturamento por categoria de produto e apresentar visualizações gráficas para facilitar a tomada de decisão.

## Estrutura do Projeto

- `loja_1.csv`, `loja_2.csv`, `loja_3.csv`, `loja_4.csv`: Arquivos de dados de vendas de cada loja.
- `AluraStoreBr.ipynb`: Notebook principal para análise exploratória, cálculos e visualizações usando pandas e matplotlib.
- `faturamento.py`: Script para calcular e visualizar o faturamento total de cada loja, utilizando listas por compreensão e visualização gráfica.
- `produtos.py`: Script para calcular o faturamento por categoria de produto em cada loja, gerar tabelas e gráficos de pizza, utilizando pandas e listas.
- `avaliacao.py`: Script para calcular a média de avaliação das compras por loja e gerar gráficos de barras.
- `rascunho.py`: Script auxiliar para testes, cálculos diversos e experimentação de médias, somas e gráficos.

## Principais Funcionalidades

- **Cálculo do faturamento total por loja** com listas por compreensão e visualização em gráfico de barras.
- **Cálculo do faturamento por categoria de produto** para cada loja, com apresentação em tabela e gráficos de pizza.
- **Cálculo da média de avaliação das compras** por loja, com visualização em gráfico de barras.
- **Comparação entre lojas** de forma visual e tabular.
- **Visualização dos dados em gráficos de barras e pizza** com matplotlib.
- **Formatação dos valores em reais (R$)**.
- **Uso avançado de listas e pandas** para tornar o código mais eficiente, compacto e legível.

## Como Executar

1. **Clone o repositório e acesse a pasta do projeto:**
   ```bash
   git clone https://github.com/coliveira1977/alura_store
   cd alura_store
   ```

2. **Instale as dependências necessárias:**
   ```bash
   pip install pandas matplotlib
   ```

3. **Execute os scripts Python conforme desejado:**
   - Para ver o faturamento total das lojas:
     ```bash
     python faturamento.py
     ```
   - Para ver o faturamento por categoria e gráficos de pizza:
     ```bash
     python produtos.py
     ```
   - Para ver a média de avaliação das compras por loja:
     ```bash
     python avaliacao.py
     ```
   - Para testar médias, somas e gráficos diversos:
     ```bash
     python rascunho.py
     ```

4. **Ou abra o notebook no Jupyter:**
   ```bash
   jupyter notebook AluraStoreBr.ipynb
   ```

## Exemplos de Visualizações

- Gráfico de barras comparando o faturamento total das lojas.
- Gráficos de pizza mostrando a participação percentual de cada categoria de produto no faturamento de cada loja.
- Tabelas formatadas com valores em reais.

## Sobre os Dados

Cada arquivo CSV contém as seguintes colunas:
- Produto
- Categoria do Produto
- Preço
- Frete
- Data da Compra
- Vendedor
- Local da compra
- Avaliação da compra
- Tipo de pagamento
- Quantidade de parcelas
- lat
- lon

## Licença

Este projeto é apenas para fins educacionais.

---

Desenvolvido para o Challenge de Data Science da Alura.

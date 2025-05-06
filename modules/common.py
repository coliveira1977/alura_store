import pandas as pd
import matplotlib.pyplot as plt

# Constantes para URLs e nomes das lojas
URLS = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv",
]

NOMES_LOJAS = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

def carregar_dados(urls):
    
    dataframes = []
    for url in urls:
        try:
            df = pd.read_csv(url)
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao carregar o arquivo {url}: {e}")
            dataframes.append(None)
    return dataframes
import pandas as pd
import folium
from folium.plugins import HeatMap
import os

# Caminho da pasta onde estão os arquivos CSV
pasta_csv = 'csv_backup'

# Lista todos os arquivos CSV dentro da pasta
arquivos_csv = [os.path.join(pasta_csv, nome) for nome in os.listdir(pasta_csv) if nome.endswith('.csv')]

# Carrega todos os arquivos CSV em uma única lista de DataFrames
dfs = [pd.read_csv(arquivo) for arquivo in arquivos_csv]

# Concatena todos os DataFrames em um único DataFrame
df_total = pd.concat(dfs, ignore_index=True)

# Remove linhas com valores ausentes em latitude ou longitude
df_total = df_total.dropna(subset=['lat', 'lon'])

# Cria o mapa centralizado no Brasil
mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

# Cria a lista de coordenadas [latitude, longitude]
pontos = df_total[['lat', 'lon']].values.tolist()

# Adiciona o HeatMap ao mapa
HeatMap(pontos).add_to(mapa)

# Salva o mapa em um arquivo HTML
mapa.save("mapa_calor.html")

print("Mapa de calor gerado e salvo como 'mapa_calor.html'.")


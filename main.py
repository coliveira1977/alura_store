from modules.faturamento import calcular_faturamento
from modules.produtos import calcular_faturamento_por_categoria
from modules.avaliacao import calcular_media_avaliacao
from modules.frete import calcular_media_frete

def main():
    # Cálculo do faturamento total
    print("=" * 50)
    print("Iniciando cálculo do faturamento total...")
    print("O gráfico será gerado em uma janela separada.")
    calcular_faturamento()
    print("Cálculo do faturamento total concluído.")
    print("=" * 50)

    # Cálculo do faturamento por categoria
    print("=" * 50)
    print("Iniciando cálculo do faturamento por categoria...")
    print("O gráfico será gerado em uma janela separada.")
    calcular_faturamento_por_categoria()
    print("Cálculo do faturamento por categoria concluído.")
    print("=" * 50)

    # Cálculo da média de avaliação
    print("=" * 50)
    print("Iniciando cálculo da média de avaliação...")
    print("O gráfico será gerado em uma janela separada.")
    calcular_media_avaliacao()
    print("Cálculo da média de avaliação concluído.")
    print("=" * 50)

    # Cálculo da média do frete
    print("=" * 50)
    print("Iniciando cálculo da média do frete...")
    print("O gráfico será gerado em uma janela separada.")
    calcular_media_frete()
    print("Cálculo da média do frete concluído.")
    print("=" * 50)

if __name__ == "__main__":
    main()
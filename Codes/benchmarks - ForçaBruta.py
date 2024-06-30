# Componentes: Carlos Dias Maia, Ranier Pereira Melo

from ForçaBruta import encontrar_combinacao_otima
from carregarDados import carregar_dados_txt_para_dicionario
import glob
import time
D_minima = 1
results = []

for filepath in glob.glob("testes/Arquivos de Teste/scenario_n*_sim*.txt"):
    pontos = carregar_dados_txt_para_dicionario(filepath)

    # Salva os tempos de começo e fim da função
    tempo_inicio = time.time()
    melhor_custo, melhor_combinacao= encontrar_combinacao_otima(pontos, D_minima)
    tempo_final = time.time()

    # Salava resultados, caminho e tempo de execução em arquivo separado
    tempo_execucao = tempo_final - tempo_inicio
    results.append((filepath, tempo_execucao, melhor_combinacao, melhor_custo))
    print(f'Processed {filepath}: {tempo_execucao:.4f} seconds')

# Salva os resultados em arquivos separados
with open(r"testes/Resultados dos Testes/Tempos de execução - outut - Força Bruta.txt", 'w') as file:
    for result in results:
        filename, tempo_execucao, melhor_combinacao, melhor_custo= result
        file.write(f'{filename}, {tempo_execucao:.4f}, {melhor_combinacao}, {melhor_custo}\n')
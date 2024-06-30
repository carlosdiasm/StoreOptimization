# Componentes: Carlos Dias Maia, Ranier Pereira Melo

import random

def gera_cenarios_aleatorios(n, m):
    lojas = []
    for i in range(1, n + 1):
        for _ in range(m):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            custo = random.randint(500, 2000)
            lojas.append((i, x, y, custo))
    return lojas

# Gera 10 arquivos de texto para cada valor de n de 4 a 20
numero_simulacoes = 10
m = 2  # Numero de opções por franquia

for n in range(4, 21):
    for simulacao in range(1, numero_simulacoes + 1):
        scenario = gera_cenarios_aleatorios(n, m)
        filename = f'testes/Arquivos de Teste/scenario_n{n}_sim{simulacao}.txt'
        with open(filename, 'w') as file:
            for loja in scenario:
                file.write(f'{loja[0]} {loja[1]} {loja[2]} {loja[3]}\n')

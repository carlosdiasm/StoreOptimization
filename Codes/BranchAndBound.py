# Componentes: Carlos Dias Maia, Ranier Pereira Melo

from distancia import distancia_euclid
from carregarDados import carregar_dados_txt_para_dicionario
from plotSolucao import plotar_solucao

def eh_combinacao_valida(combinacao, distancia_minima):
    """Verificar se a combinação dos pontos respeita a distância mínima"""
    for i in range(len(combinacao)):
        for j in range(i + 1, len(combinacao)):
            if distancia_euclid(combinacao[i], combinacao[j]) < distancia_minima:
                return False
    return True

def encontrar_combinacao_otima(lojas, distancia_minima, loja_atual=1, combinacao_atual=None, custo_atual=0, melhor_custo_ate_agora=float('inf')):
    if combinacao_atual is None:
        combinacao_atual = []

    # Caso base: quando loja_atual está além do número de lojas
    if loja_atual > len(lojas):
        if eh_combinacao_valida(combinacao_atual, distancia_minima):
            return custo_atual, combinacao_atual
        else:
            return float('inf'), None

    # Limite Inferior: Calcular um limite inferior para o custo da solução parcial atual
    limite_inferior = custo_atual
    for loja in range(loja_atual, len(lojas) + 1):
        custo_minimo = min(opcao[2] for opcao in lojas[loja])
        limite_inferior += custo_minimo

    # Poda: Se o limite inferior exceder o melhor custo encontrado até agora, poda o ramo
    if limite_inferior > melhor_custo_ate_agora:
        return float('inf'), None

    custo_otimo = float('inf')
    combinacao_otima = None

    # Caso recursivo: explorar todas as opções para a loja atual
    for opcao in lojas[loja_atual]:
        novo_custo = custo_atual + opcao[2]
        nova_combinacao = combinacao_atual + [(opcao[0], opcao[1], opcao[2], loja_atual)]  # Incluir número da franquia

        # Recursão para a próxima loja
        custo, combinacao = encontrar_combinacao_otima(lojas, distancia_minima, loja_atual + 1, nova_combinacao, novo_custo, melhor_custo_ate_agora)

        # Atualizar o melhor custo encontrado até agora
        if custo < melhor_custo_ate_agora:
            melhor_custo_ate_agora = custo

        # Atualizar a solução ótima se uma melhor for encontrada
        if custo < custo_otimo:
            custo_otimo = custo
            combinacao_otima = combinacao

    # Se nenhuma combinação válida foi encontrada, tentar excluir a loja atual e recorrer
    if combinacao_otima is None:
        if loja_atual <= len(lojas):
            return encontrar_combinacao_otima(lojas, distancia_minima, loja_atual + 1, combinacao_atual, custo_atual, melhor_custo_ate_agora)
        else:
            return float('inf'), None

    return custo_otimo, combinacao_otima


def main():
    nome_arquivo = r"testes\Arquivos de Teste\scenario_n15_sim3.txt"  # nome do arquivo com os pontos
    lojas = carregar_dados_txt_para_dicionario(nome_arquivo)
    D_minima = 1  # Distancia euclidiana minima entre os pontos
    custo_otimo, combinacao_otima = encontrar_combinacao_otima(lojas, D_minima)
    print(f"Melhor custo: {custo_otimo}")
    print(f"Melhor combinção: {combinacao_otima}")
    plotar_solucao(combinacao_otima)

if __name__ == "__main__":
    main()


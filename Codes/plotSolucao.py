# Componentes: Carlos Dias Maia, Ranier Pereira Melo

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plotar_solucao(solucao):
    # Extrair coordenadas, custos e números das franquias da solução
    coordenadas_x = [local[0] for local in solucao]
    coordenadas_y = [local[1] for local in solucao]
    custos = [local[2] for local in solucao]
    franquias = [local[3] for local in solucao]

    # Carregar a imagem da loja
    imagem_loja = mpimg.imread("utils/StoreImage.png")
    tamanho_imagem = 50  # Tamanho da imagem

    plt.figure(figsize=(50, 50))
    ax = plt.gca()

    # Plotar a imagem em cada localização de loja e anotar com o custo e número da franquia
    for (x, y, custo, franquias) in solucao:
        ax.imshow(imagem_loja, extent=(x - tamanho_imagem/2, x + tamanho_imagem/2, y - tamanho_imagem/2, y + tamanho_imagem/2))
        plt.text(x, y - tamanho_imagem/2 , f'Custo: {custo}', fontsize=8, ha='center', va='top')
        plt.text(x, y + tamanho_imagem/2 , f'Franquia: {franquias}', fontsize=8, ha='center', va='bottom')

    # Exibir custo total no canto superior direito
    plt.text(590, 590, f'Custo total: {sum(custos)}', fontsize=10, ha='right', va='top')

    plt.title('Localização das Lojas')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.xlim(-100, 600)
    plt.ylim(-100, 600)
    plt.show()



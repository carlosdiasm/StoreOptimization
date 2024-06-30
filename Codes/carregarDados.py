# Componentes: Carlos Dias Maia, Ranier Pereira Melo

def carregar_dados_txt_para_dicionario(arquivo_txt):
  dados = {}
  with open(arquivo_txt, 'r') as f:
    for linha in f:
      # Divide a linha em partes usando espaços em branco
      partes = linha.split()

      # Extrai os dados da linha
      indice = int(partes[0])
      valor1 = int(partes[1])
      valor2 = int(partes[2])
      valor3 = int(partes[3])

      # Cria ou atualiza o dicionário com os dados
      if indice not in dados:
        dados[indice] = []
      dados[indice].append((valor1, valor2, valor3))

  return dados
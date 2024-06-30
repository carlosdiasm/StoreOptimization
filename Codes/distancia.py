# Componentes: Carlos Dias Maia, Ranier Pereira Melo

import math

def distancia_euclid(ponto1, ponto2):
    """Calcula a distancia entre 2 pontos usando a distancia euclidiana"""
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
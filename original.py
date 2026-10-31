
"""
UNIJORGE - Analise e Otimizacao de Sistemas
AV2 - Tema 1: Deteccao de duplicatas

Versao original: algoritmo de forca bruta.
"""


def tem_duplicata(lista):
    """
    Verifica se existem elementos repetidos.

    Tempo no pior caso: O(n²)
    Espaco auxiliar: O(1)
    """

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True

    return False


if __name__ == "__main__":
    exemplos = [
        [],
        [1],
        [1, 2, 3, 4],
        [1, 2, 3, 2],
        [5, 5],
        [-1, 0, 1, -1]
    ]

    for entrada in exemplos:
        print(f"Lista: {entrada}")
        print(f"Duplicata: {tem_duplicata(entrada)}")
        print("-" * 40)

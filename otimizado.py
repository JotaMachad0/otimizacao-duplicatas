
"""
UNIJORGE - Analise e Otimizacao de Sistemas
AV2 - Tema 1: Deteccao de duplicatas

Primeira otimizacao: estrutura de dados set.
"""


def tem_duplicata_otimizado(lista):
    """
    Verifica duplicatas utilizando hashing.

    Tempo esperado: O(n)
    Espaco auxiliar: O(n)

    Requer elementos hashable, como inteiros.
    """

    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return True

        vistos.add(elemento)

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
        print(
            "Duplicata:",
            tem_duplicata_otimizado(entrada)
        )
        print("-" * 40)

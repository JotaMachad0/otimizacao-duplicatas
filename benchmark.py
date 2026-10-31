
"""
Benchmark comparativo: algoritmo original x otimizado.

Mede tempos de execucao e salva os resultados
em um arquivo CSV.
"""

import csv
import platform
import statistics
import sys
import time
from pathlib import Path

from original import tem_duplicata
from otimizado import tem_duplicata_otimizado


TAMANHOS = [100, 500, 1000, 2000, 4000, 8000]
REPETICOES = 5

PASTA_RESULTADOS = (
    Path(__file__).resolve().parent / "resultados"
)


def medir_tempo(funcao, entrada):
    tempos = []

    for _ in range(REPETICOES):
        inicio = time.perf_counter()
        resultado = funcao(entrada)
        fim = time.perf_counter()

        if resultado is not False:
            raise AssertionError(
                "Resultado incorreto no benchmark"
            )

        tempos.append((fim - inicio) * 1000)

    return {
        "media": statistics.mean(tempos),
        "melhor": min(tempos),
        "desvio": statistics.stdev(tempos)
    }


def executar_benchmark():
    PASTA_RESULTADOS.mkdir(exist_ok=True)

    print("=" * 65)
    print("BENCHMARK - DETECCAO DE DUPLICATAS")
    print("=" * 65)
    print("Python:", sys.version.split()[0])
    print("Sistema:", platform.platform())
    print("Repeticoes:", REPETICOES)
    print("Cenario: listas sem duplicatas")
    print("=" * 65)

    resultados = []

    for n in TAMANHOS:
        entrada = list(range(n))

        original = medir_tempo(
            tem_duplicata,
            entrada
        )

        otimizado = medir_tempo(
            tem_duplicata_otimizado,
            entrada
        )

        ganho = (
            original["media"] / otimizado["media"]
            if otimizado["media"] > 0
            else float("inf")
        )

        linha = {
            "tamanho": n,
            "original_media_ms": original["media"],
            "original_melhor_ms": original["melhor"],
            "original_desvio_ms": original["desvio"],
            "otimizado_media_ms": otimizado["media"],
            "otimizado_melhor_ms": otimizado["melhor"],
            "otimizado_desvio_ms": otimizado["desvio"],
            "ganho_vezes": ganho
        }

        resultados.append(linha)

        print(
            f"N={n:5d} | "
            f"Original: {original['media']:.4f} ms | "
            f"Otimizado: {otimizado['media']:.4f} ms | "
            f"Ganho: {ganho:.2f}x"
        )

    destino = PASTA_RESULTADOS / "benchmark.csv"

    with destino.open(
        "w", newline="", encoding="utf-8"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=resultados[0].keys()
        )

        escritor.writeheader()
        escritor.writerows(resultados)

    print("=" * 65)
    print("Resultados salvos em:", destino)


if __name__ == "__main__":
    executar_benchmark()


"""
Gera graficos comparativos a partir do benchmark.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


PASTA_RESULTADOS = (
    Path(__file__).resolve().parent / "resultados"
)


def executar():
    arquivo_csv = PASTA_RESULTADOS / "benchmark.csv"

    if not arquivo_csv.exists():
        print("Execute benchmark.py primeiro.")
        return

    with arquivo_csv.open(
        encoding="utf-8", newline=""
    ) as arquivo:
        dados = list(csv.DictReader(arquivo))

    tamanhos = [
        int(linha["tamanho"])
        for linha in dados
    ]

    original = [
        float(linha["original_media_ms"])
        for linha in dados
    ]

    otimizado = [
        float(linha["otimizado_media_ms"])
        for linha in dados
    ]

    ganhos = [
        float(linha["ganho_vezes"])
        for linha in dados
    ]

    # Grafico 1: comparacao de tempos
    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanhos,
        original,
        marker="o",
        label="Original O(n²)"
    )

    plt.plot(
        tamanhos,
        otimizado,
        marker="o",
        label="Otimizado O(n) esperado"
    )

    plt.title("Comparacao de desempenho")
    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Tempo medio (ms)")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        PASTA_RESULTADOS / "comparacao_tempos.png",
        dpi=200
    )
    plt.close()

    # Grafico 2: ganho de desempenho
    plt.figure(figsize=(10, 6))

    plt.bar(
        [str(n) for n in tamanhos],
        ganhos
    )

    plt.title("Ganho de desempenho")
    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Aceleracao (vezes)")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        PASTA_RESULTADOS / "ganho_desempenho.png",
        dpi=200
    )
    plt.close()

    print("Graficos gerados com sucesso!")


if __name__ == "__main__":
    executar()

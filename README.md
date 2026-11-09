
# Otimizacao de Codigo - AV2

## UNIJORGE
Disciplina: Analise e Otimizacao de Sistemas

Professor: Igor Gonzalez

Tema 1: Deteccao de Duplicatas

## Objetivo

Comparar duas implementacoes de deteccao de
duplicatas em listas de numeros inteiros.

A primeira utiliza dois lacos aninhados,
enquanto a segunda utiliza hashing com set.

## Complexidade

Versao original:
- Tempo no pior caso: O(n²)
- Espaco auxiliar: O(1)

Versao otimizada:
- Tempo esperado: O(n)
- Espaco auxiliar: O(n)

## Arquivos

- original.py: implementacao inicial
- otimizado.py: primeira otimizacao
- testes.py: testes de corretude
- benchmark.py: medicoes de desempenho
- graficos.py: geracao de graficos
- requirements.txt: dependencias

## Como executar

Criar ambiente virtual no Windows:

    py -m venv .venv

Instalar dependencias:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Executar os testes:

    .\.venv\Scripts\python.exe testes.py

Executar o benchmark:

    .\.venv\Scripts\python.exe benchmark.py

Gerar os graficos:

    .\.venv\Scripts\python.exe graficos.py

## Metodologia

Foram definidos seis tamanhos de entrada:
100, 500, 1000, 2000, 4000 e 8000.

Cada algoritmo e executado cinco vezes para
cada tamanho de entrada.

As listas contem inteiros distintos para
representar o pior caso da versao original.

Sao calculados:
- Tempo medio
- Melhor tempo
- Desvio padrao
- Ganho de desempenho

## Resultados

Os resultados sao gerados automaticamente
na pasta resultados/.

O arquivo benchmark.csv contem os tempos.
Os arquivos PNG apresentam os graficos.

## Limitacoes

A implementacao otimizada exige elementos
hashable. As operacoes de set apresentam
tempo constante esperado, nao garantido.

Os resultados de desempenho dependem do
ambiente de execucao.


"""
Testes automatizados para validar as duas versoes.
"""

import random
import unittest

from original import tem_duplicata
from otimizado import tem_duplicata_otimizado


class TesteDuplicatas(unittest.TestCase):

    def verificar(self, entrada, esperado):
        self.assertEqual(tem_duplicata(entrada), esperado)
        self.assertEqual(
            tem_duplicata_otimizado(entrada),
            esperado
        )

    def test_lista_vazia(self):
        self.verificar([], False)

    def test_um_elemento(self):
        self.verificar([1], False)

    def test_sem_duplicatas(self):
        self.verificar([1, 2, 3, 4, 5], False)

    def test_com_duplicatas(self):
        self.verificar([1, 2, 3, 2, 5], True)

    def test_elementos_iguais(self):
        self.verificar([7, 7], True)

    def test_numeros_negativos(self):
        self.verificar([-1, 0, 1, -1], True)

    def test_lista_grande(self):
        entrada = list(range(1000))
        self.verificar(entrada, False)

        entrada.append(500)
        self.verificar(entrada, True)

    def test_casos_aleatorios(self):
        gerador = random.Random(42)

        for _ in range(100):
            tamanho = gerador.randint(0, 30)
            entrada = [
                gerador.randint(-20, 20)
                for _ in range(tamanho)
            ]

            esperado = len(entrada) != len(set(entrada))
            self.verificar(entrada, esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)

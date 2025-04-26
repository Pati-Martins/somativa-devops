import unittest
from src.main import *


class TestZombieDice(unittest.TestCase):

    def test_obter_num_jogadores(self):
        resultado = obter_num_jogadores()
        self.assertEqual(resultado, 3)

    def test_obter_nomes_jogadores(self):
        jogadores = obter_nomes_jogadores(2)
        self.assertEqual(len(jogadores), 2)
        self.assertEqual(jogadores[0][1], "João")
        self.assertEqual(jogadores[1][1], "Maria")

    def test_colocar_dados_copo(self):
        copo = colocar_dados_copo()
        self.assertEqual(len(copo), 13)  # 6 verdes + 4 amarelos + 3 vermelhos

    def test_pegar_dados_copo(self):
        def test_pegar_dados_copo(self):
            copo = [('C', 'P', 'C', 'T', 'P', 'C'), ('T', 'P', 'C', 'T', 'P', 'C')]
            copo_original = copo.copy()
            dado, novo_copo = pegar_dados_copo(copo)
            self.assertIn(dado, copo_original)

    def test_lancar_dados(self):
        dado = ('C', 'P', 'C', 'T', 'P', 'C')
        resultado = lancar_dados(dado)
        self.assertIn(resultado, ['C', 'P', 'T'])

    def test_pontuacao(self):
        # Testa algumas combinações básicas
        self.assertEqual(pontuacao(['C', 'P', 'T']), (1, 1, 1))
        self.assertEqual(pontuacao(['C', 'C', 'C']), (3, 0, 0))
        self.assertEqual(pontuacao(['T', 'T', 'T']), (0, 0, 3))

    def test_verificar_vitoria(self):
        # Testa com vencedor
        jogadores = [[0, "João", [13, 0]], [1, "Maria", [5, 0]]]
        self.assertTrue(verificar_vitoria(jogadores))

        # Testa sem vencedor
        jogadores = [[0, "João", [10, 0]], [1, "Maria", [5, 0]]]
        self.assertFalse(verificar_vitoria(jogadores))


if __name__ == '__main__':
    unittest.main()
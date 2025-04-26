import unittest
from unittest.mock import patch
from src.main import *
import pytest

@pytest.mark.asyncio
def test_obter_num_jogadores(self):
    with patch('builtins.input', return_value='2'):
        resultado = obter_num_jogadores()
        self.assertEqual(resultado, 2)

@pytest.mark.asyncio
def test_obter_nomes_jogadores(self):
    with patch('builtins.input', side_effect=['Alice', 'Bob']):
        jogadores = obter_nomes_jogadores(2)
        self.assertEqual(len(jogadores), 2)
        self.assertEqual(jogadores[0][1], 'Alice')
        self.assertEqual(jogadores[1][1], 'Bob')

    """def test_obter_jogadores(self):
        with patch('builtins.input', side_effect=['2', 'Ana', 'Bob']):
            num = obter_num_jogadores()
            jogadores = obter_nomes_jogadores(num)
            self.assertEqual(len(jogadores), 2)
            self.assertEqual(jogadores[0][1], 'Ana')"""

@pytest.mark.asyncio
def test_dados_no_copo(self):
    copo = []
    copo = colocar_dados_copo(copo)

    self.assertEqual(len(copo), 13)

    dado, novo_copo = pegar_dados_copo(copo)
    self.assertEqual(len(novo_copo), 12)

@patch('random.randint', return_value=0)
def test_lancar_dado(self, mock_rand):
    dado_verde = ('C', 'P', 'C', 'T', 'P', 'C')
    resultado = lancar_dados(dado_verde)
    self.assertEqual(resultado, 'C')

def test_pontuacao(self):
    c, p, t = pontuacao('C', 'P', 'T')
    self.assertEqual((c, p, t), (1, 1, 1))

@patch('random.randint', return_value=0)
def test_turno_simples(self, mock_rand):
    copo = []
    colocar_dados_copo(copo)

    dados = []
    for _ in range(3):
        dado, copo = pegar_dados_copo(copo)
        dados.append(dado)

    resultados = [lancar_dados(d) for d in dados]

    c, p, t = pontuacao(*resultados)
    self.assertGreaterEqual(c, 0)

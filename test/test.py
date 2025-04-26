from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio
import unittest

@pytest.mark.asyncio
def test_colocar_dados_copo():
    copo = []
    colocar_dados_copo(copo)
    assert len(copo) == 13

@pytest.mark.asyncio
def test_pegar_dados_copo():
    copo = [('C', 'P', 'C', 'T', 'P', 'C'), ('T', 'P', 'C', 'T', 'P', 'C')]
    dado, novo_copo = pegar_dados_copo(copo)
    assert len(novo_copo) == 1
    assert dado in [('C', 'P', 'C', 'T', 'P', 'C'), ('T', 'P', 'C', 'T', 'P', 'C')]

@pytest.mark.asyncio
def test_lancar_dados():
    dado = ('C', 'P', 'C', 'T', 'P', 'C')
    assert lancar_dados(dado) in ['C', 'P', 'T']

@pytest.mark.asyncio
def test_pontuacao():
    assert pontuacao('C', 'C', 'C') == (3, 0, 0)
    assert pontuacao('P', 'P', 'T') == (0, 2, 1)
    assert pontuacao('C', 'P', 'T') == (1, 1, 1)

@pytest.mark.asyncio
def test_pegar_dados_copo_vazio():
    assert pegar_dados_copo([]) == (0, [])

@pytest.mark.asyncio
def test_obter_num_jogadores():
    with patch("builtins.input", return_value="2"):
        assert obter_num_jogadores() == 2


#class TestCopoSimples(unittest.TestCase):
#    async def test_colocar_dados_copo(self):
#        copo = []
#        resultado = colocar_dados_copo(copo)
#
#        self.assertEqual(len(resultado), 13)
#
#        self.assertEqual(resultado.count(('C', 'P', 'C', 'T', 'P', 'C')), 6)
#        self.assertEqual(resultado.count(('T', 'P', 'C', 'T', 'P', 'C')), 4)
#        self.assertEqual(resultado.count(('T', 'P', 'T', 'C', 'P', 'T')), 3)
#
#
#if __name__ == '__main__':
#    unittest.main()
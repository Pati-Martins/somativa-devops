from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio
import unittest

@pytest.mark.asyncio
class TestCopoSimples(unittest.TestCase):
    async def test_colocar_dados_copo(self):
        copo = []
        resultado = colocar_dados_copo(copo)

        self.assertEqual(len(resultado), 13)

        self.assertEqual(resultado.count(('C', 'P', 'C', 'T', 'P', 'C')), 6)
        self.assertEqual(resultado.count(('T', 'P', 'C', 'T', 'P', 'C')), 4)
        self.assertEqual(resultado.count(('T', 'P', 'T', 'C', 'P', 'T')), 3)


if __name__ == '__main__':
    unittest.main()
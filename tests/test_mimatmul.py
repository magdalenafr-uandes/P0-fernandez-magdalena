"""Pruebas para la función mimatmul."""

import pytest

from src.mimatmul import mimatmul


def test_resultado_conocido():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado = mimatmul(A, B)
    esperado = [[19, 22], [43, 50]]
    assert resultado.tolist() == esperado


def test_dimensiones_incompatibles():
    A = [[1, 2, 3]]
    B = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        mimatmul(A, B)

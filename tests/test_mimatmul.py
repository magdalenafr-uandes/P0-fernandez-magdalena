"""Pruebas para la función mimatmul."""

import numpy as np
import pytest

from src.mimatmul import mimatmul


def test_resultado_conocido():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado = mimatmul(A, B)
    esperado = [[19, 22], [43, 50]]
    assert resultado.tolist() == esperado


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    resultado = mimatmul(A, B)
    esperado = [[58, 64], [139, 154]]
    assert resultado.shape == (2, 2)
    assert resultado.tolist() == esperado


def test_comparacion_con_numpy():
    rng = np.random.default_rng(2026)
    A = rng.random((3, 4))
    B = rng.random((4, 2))
    resultado = mimatmul(A, B)
    referencia = A @ B
    assert resultado.shape == referencia.shape
    np.testing.assert_allclose(resultado, referencia)


def test_dimensiones_incompatibles():
    A = [[1, 2, 3]]
    B = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        mimatmul(A, B)

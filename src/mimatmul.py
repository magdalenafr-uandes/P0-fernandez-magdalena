"""Multiplicación de matrices con ciclos explícitos de Python."""

import numpy as np


def mimatmul(A, B):
    """Multiplica dos matrices usando ciclos explícitos de Python."""
    A = np.asarray(A)
    B = np.asarray(B)

    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("A y B deben ser matrices de dos dimensiones")

    if A.shape[1] != B.shape[0]:
        raise ValueError(
            f"Dimensiones incompatibles: A {A.shape} y B {B.shape}"
        )

    filas, interno = A.shape
    columnas = B.shape[1]
    C = np.zeros((filas, columnas), dtype=float)

    for i in range(filas):
        for j in range(columnas):
            for k in range(interno):
                C[i, j] += A[i, k] * B[k, j]

    return C

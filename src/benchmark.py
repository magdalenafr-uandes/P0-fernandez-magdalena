"""Benchmark que compara mimatmul con NumPy (A @ B)."""

import csv
import time
from pathlib import Path

import numpy as np

from mimatmul import mimatmul


def escribir_resultados(filas, ruta):
    """Guarda los tiempos medidos en un archivo CSV."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["metodo", "N", "repeticion", "tiempo"])
        escritor.writerows(filas)


if __name__ == "__main__":
    rng = np.random.default_rng(2026)
    tamanos = [10, 20, 40, 80]
    repeticiones = 3
    filas = []

    for N in tamanos:
        A = rng.random((N, N), dtype=np.float64)
        B = rng.random((N, N), dtype=np.float64)

        mimatmul(A, B)
        A @ B

        for repeticion in range(1, repeticiones + 1):
            inicio = time.perf_counter()
            mimatmul(A, B)
            fin = time.perf_counter()
            filas.append(["mimatmul", N, repeticion, fin - inicio])

            inicio = time.perf_counter()
            A @ B
            fin = time.perf_counter()
            filas.append(["numpy", N, repeticion, fin - inicio])

    ruta_salida = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "benchmark_results.csv"
    )
    escribir_resultados(filas, ruta_salida)
    print(f"Benchmark guardado en {ruta_salida}")

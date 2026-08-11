"""Benchmark que compara mimatmul con NumPy (A @ B)."""

import csv
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from mimatmul import mimatmul


def escribir_resultados(filas, ruta):
    """Guarda los tiempos medidos en un archivo CSV."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["metodo", "N", "repeticion", "tiempo"])
        escritor.writerows(filas)


def leer_resultados(ruta):
    """Lee los tiempos del archivo CSV."""
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def promedios_por_metodo_y_n(filas):
    """Calcula el tiempo promedio de cada método para cada N."""
    acumulados = {}
    conteos = {}
    for fila in filas:
        clave = (fila["metodo"], int(fila["N"]))
        acumulados[clave] = acumulados.get(clave, 0.0) + float(fila["tiempo"])
        conteos[clave] = conteos.get(clave, 0) + 1
    return {
        clave: acumulados[clave] / conteos[clave] for clave in acumulados
    }


def generar_grafico(ruta_csv, ruta_figura):
    """Genera el gráfico del benchmark a partir del CSV."""
    filas = leer_resultados(ruta_csv)
    promedios = promedios_por_metodo_y_n(filas)
    metodos = sorted({clave[0] for clave in promedios})
    ruta_figura.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots()
    for metodo in metodos:
        puntos = sorted(
            (n, tiempo)
            for (metodo_i, n), tiempo in promedios.items()
            if metodo_i == metodo
        )
        ns = [punto[0] for punto in puntos]
        tiempos = [punto[1] for punto in puntos]
        ax.plot(ns, tiempos, marker="o", label=metodo)

    ax.set_yscale("log")
    ax.set_xlabel("N (tamaño de la matriz)")
    ax.set_ylabel("Tiempo de ejecución [s] (escala logarítmica)")
    ax.set_title("Benchmark: mimatmul vs NumPy")
    ax.legend()
    ax.grid(True, which="both")
    fig.savefig(ruta_figura, dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    rng = np.random.default_rng(2026)
    tamanos = [40, 80, 120, 160]
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

    ruta_figura = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "benchmark.png"
    )
    generar_grafico(ruta_salida, ruta_figura)
    print(f"Gráfico guardado en {ruta_figura}")

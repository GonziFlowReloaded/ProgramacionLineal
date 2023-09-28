from grafico import generar_grafico_asignaciones_ordenado_lado_a_lado
from simplex import resolver_problema_asignacion
import numpy as np


cost_matrix = np.array([[5, 2, 7, 3],
                        [3, 6, 6, 1],
                        [6, 1, 2, 4],
                        [4, 3, 6, 6]])

supply = np.array([80, 30, 60, 45])
demand = np.array([70, 40, 70, 35])

estado, asignaciones, costo_total = resolver_problema_asignacion(cost_matrix, supply, demand)

print(f"Estado: {estado}")
print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")

generar_grafico_asignaciones_ordenado_lado_a_lado(asignaciones)

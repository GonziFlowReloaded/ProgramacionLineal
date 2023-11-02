import numpy as np
from scipy.optimize import linear_sum_assignment

def vogel(cost_matrix, supply, demand):
    if np.sum(supply) != np.sum(demand):
        return "No se puede equilibrar la oferta y la demanda"

    row_indices, col_indices = linear_sum_assignment(cost_matrix)

    asignaciones = np.zeros_like(cost_matrix)
    costo_total = 0

    for i, j in zip(row_indices, col_indices):
        asignar = min(supply[i], demand[j])
        asignaciones[i][j] = asignar
        supply[i] -= asignar
        demand[j] -= asignar
        costo_total += cost_matrix[i][j] * asignar

    estado = "Solución factible" if np.sum(supply) == 0 and np.sum(demand) == 0 else "Solución no factible"

    return estado, asignaciones, costo_total
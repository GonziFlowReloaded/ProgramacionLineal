import numpy as np

def vogel(cost_matrix, supply, demand):
    if np.sum(supply) != np.sum(demand):
        return "No se puede equilibrar la oferta y la demanda"

    supply = supply.copy()
    demand = demand.copy()

    asignaciones = np.zeros_like(cost_matrix)
    costo_total = 0

    while np.sum(supply) > 0 and np.sum(demand) > 0:
        min_diff_row = []
        for i in range(len(supply)):
            if supply[i] > 0:
                min_cost = min(cost_matrix[i])
                next_min_cost = min(x for x in cost_matrix[i] if x > min_cost)
                min_diff_row.append(next_min_cost - min_cost)
            else:
                min_diff_row.append(0)

        min_diff_col = []
        for j in range(len(demand)):
            if demand[j] > 0:
                min_cost = min(cost_matrix[:, j])
                next_min_cost = min(x for x in cost_matrix[:, j] if x > min_cost)
                min_diff_col.append(next_min_cost - min_cost)
            else:
                min_diff_col.append(0)

        max_diff_row_index = np.argmax(min_diff_row)
        max_diff_col_index = np.argmax(min_diff_col)

        if min_diff_row[max_diff_row_index] >= min_diff_col[max_diff_col_index]:
            i = max_diff_row_index
            j = np.argmin(cost_matrix[i])
        else:
            j = max_diff_col_index
            i = np.argmin(cost_matrix[:, j])

        asignar = min(supply[i], demand[j])

        asignaciones[i][j] = asignar
        supply[i] -= asignar
        demand[j] -= asignar
        costo_total += cost_matrix[i][j] * asignar

    estado = "Solución factible" if np.sum(supply) == 0 and np.sum(demand) == 0 else "Solución no factible"

    return estado, asignaciones, costo_total
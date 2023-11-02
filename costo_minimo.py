import numpy as np

def costo_minimo(cost_matrix, supply, demand):
    # Verificar que la matriz de costos, suministros y demandas sean válidos
    if np.sum(supply) != np.sum(demand):
        return "No se puede equilibrar la oferta y la demanda"

    # Crear copias de las listas de suministro y demanda para evitar modificaciones inesperadas
    supply = supply.copy()
    demand = demand.copy()

    # Inicializar las asignaciones y el costo total
    asignaciones = np.zeros_like(cost_matrix)
    costo_total = 0

    # Iterar hasta que todas las demandas sean satisfechas
    while np.sum(demand) > 0:
        # Encontrar la celda de costo mínimo
        min_cost = np.inf
        min_i, min_j = -1, -1

        for i in range(len(supply)):
            for j in range(len(demand)):
                if supply[i] > 0 and demand[j] > 0:
                    if cost_matrix[i][j] < min_cost:
                        min_cost = cost_matrix[i][j]
                        min_i, min_j = i, j

        # Determinar la cantidad que se asignará
        asignar = min(supply[min_i], demand[min_j])

        # Realizar la asignación y actualizar suministros y demandas
        asignaciones[min_i][min_j] = asignar
        supply[min_i] -= asignar
        demand[min_j] -= asignar

        # Actualizar el costo total
        costo_total += min_cost * asignar

    # Verificar si se alcanzó una solución factible
    if np.sum(supply) == 0 and np.sum(demand) == 0:
        estado = "Solución factible"
    else:
        estado = "Solución no factible"

    return estado, asignaciones, costo_total
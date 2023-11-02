import numpy as np

def esquina_noroeste(cost_matrix, supply, demand):
    # Verificar que la matriz de costos, suministros y demandas sean válidos
    if np.sum(supply) != np.sum(demand):
        return "No se puede equilibrar la oferta y la demanda"

    # Crear copias de las listas de suministro y demanda para evitar modificaciones inesperadas
    supply = supply.copy()
    demand = demand.copy()

    # Inicializar las asignaciones y el costo total
    asignaciones = np.zeros_like(cost_matrix)
    costo_total = 0

    # Índices para recorrer la matriz
    i, j = 0, 0

    # Realizar las asignaciones desde la esquina noroeste
    while i < len(supply) and j < len(demand):
        asignar = min(supply[i], demand[j])

        # Realizar la asignación y actualizar suministros y demandas
        asignaciones[i][j] = asignar
        supply[i] -= asignar
        demand[j] -= asignar
        costo_total += cost_matrix[i][j] * asignar

        # Actualizar los índices
        if supply[i] == 0:
            i += 1
        else:
            j += 1

    # Verificar si se alcanzó una solución factible
    if np.sum(supply) == 0 and np.sum(demand) == 0:
        estado = "Solución factible"
    else:
        estado = "Solución no factible"

    return estado, asignaciones, costo_total
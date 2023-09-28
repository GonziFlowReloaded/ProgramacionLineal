import pulp
import numpy as np

def resolver_problema_asignacion(cost_matrix, supply, demand):
    lp_problem = pulp.LpProblem("AsignacionCostos", pulp.LpMinimize)
    
    num_supply, num_demand = cost_matrix.shape
    variables = pulp.LpVariable.dicts("X", [(i, j) for i in range(num_supply) for j in range(num_demand)], lowBound=0, cat=pulp.LpInteger)
    
    lp_problem += pulp.lpSum(cost_matrix[i][j] * variables[(i, j)] for i in range(num_supply) for j in range(num_demand)), "Costo_Total"
    
    for i in range(num_supply):
        lp_problem += pulp.lpSum(variables[(i, j)] for j in range(num_demand)) <= supply[i], f"Suministro_{i}"
    
    for j in range(num_demand):
        lp_problem += pulp.lpSum(variables[(i, j)] for i in range(num_supply)) >= demand[j], f"Demanda_{j}"
    
    lp_problem.solve()
    
    estado = pulp.LpStatus[lp_problem.status]
    
    asignaciones = []
    for i in range(num_supply):
        for j in range(num_demand):
            if variables[(i, j)].varValue > 0:
                asignaciones.append((i+1, j+1, variables[(i, j)].varValue))
    
    costo_total = pulp.value(lp_problem.objective)
    
    return estado, asignaciones, costo_total

# Datos de entrada
cost_matrix = np.array([[5, 2, 7, 3],
                        [3, 6, 6, 1],
                        [6, 1, 2, 4],
                        [4, 3, 6, 6]])

supply = np.array([80, 30, 60, 45])
demand = np.array([70, 40, 70, 35])

# Llamar a la función y obtener resultados
estado, asignaciones, costo_total = resolver_problema_asignacion(cost_matrix, supply, demand)

print("Estado:", estado)
print("Asignaciones:", asignaciones)

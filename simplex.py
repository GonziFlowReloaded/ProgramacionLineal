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

from grafico import generar_grafico_asignaciones_ordenado_lado_a_lado
from simplex import resolver_problema_asignacion
from costo_minimo import costo_minimo
from esquina_noroeste import esquina_noroeste
from voguel import vogel
import numpy as np


cost_matrix = np.array([[5,2,7,3],
                        [3,6,6,1],
                        [6,1,2,4],
                        [4,3,6,6],
                        ])

supply = np.array([80,30,60,45])
demand = np.array([70,40,70,35])

estado, asignaciones, costo_total = resolver_problema_asignacion(cost_matrix, supply, demand)
print('Simplex')
print(f"Estado: {estado}")
# print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")

print("-"*60)

estado, asignaciones, costo_total = costo_minimo(cost_matrix, supply, demand)
print('Costo Minimo')
print(f"Estado: {estado}")
# print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")

print("-"*60)

estado, asignaciones, costo_total = esquina_noroeste(cost_matrix, supply, demand)
print('Esquina Noroeste')
print(f"Estado: {estado}")
# print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")


print("-"*60)

estado = vogel(cost_matrix, supply, demand)
print('Vogel')
print(f"Costo Total: {estado}")
# print(f"Asignaciones: {asignaciones}")



# generar_grafico_asignaciones_ordenado_lado_a_lado(asignaciones)

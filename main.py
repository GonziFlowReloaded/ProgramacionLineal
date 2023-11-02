from grafico import generar_grafico_asignaciones_ordenado_lado_a_lado
from simplex import resolver_problema_asignacion
from costo_minimo import costo_minimo
from esquina_noroeste import esquina_noroeste
from voguel import vogel
import numpy as np


cost_matrix = np.array([[1.9, 1.8, 2.5, 2, 3, 5.5],
                        [3.5, 3.7, 2.4, 2.5, 1.9, 5.7]
                        ])

supply = np.array([2000, 1000])
demand = np.array([450,600,350,500,700,400])

estado, asignaciones, costo_total = resolver_problema_asignacion(cost_matrix, supply, demand)
print('Simplex')
print(f"Estado: {estado}")
print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")

print("-"*60)

estado, asignaciones, costo_total = costo_minimo(cost_matrix, supply, demand)
print('Costo Minimo')
print(f"Estado: {estado}")
print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")

print("-"*60)

estado, asignaciones, costo_total = esquina_noroeste(cost_matrix, supply, demand)
print('Esquina Noroeste')
print(f"Estado: {estado}")
print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")


print("-"*60)

estado, asignaciones, costo_total = vogel(cost_matrix, supply, demand)
print('Vogel')
print(f"Estado: {estado}")
print(f"Asignaciones: {asignaciones}")
print(f"Costo Total: {costo_total}")


# generar_grafico_asignaciones_ordenado_lado_a_lado(asignaciones)

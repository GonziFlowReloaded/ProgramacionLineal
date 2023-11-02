import networkx as nx
import matplotlib.pyplot as plt

def generar_grafico_asignaciones_ordenado_lado_a_lado(asignaciones):
    # grafiño
    G = nx.DiGraph()

    # nodos y arcos
    for asignacion in asignaciones:
        supply_node, demand_node, cantidad = asignacion
        G.add_edge(f"Centro de distribucion {supply_node}", f"Sucursal {demand_node}", capacity=cantidad)

    #se le asignan los nombres a los nodos
    pos = {}
    num_supply = max(asignacion[0] for asignacion in asignaciones)
    for i in range(1, num_supply + 1):
        pos[f"Centro de distribucion {i}"] = (-1, num_supply - i)

    num_demand = max(asignacion[1] for asignacion in asignaciones)
    for i in range(1, num_demand + 1):
        pos[f"Sucursal {i}"] = (1, num_demand - i)

    #dolor aaaaaaaaaaaaaaaaa
    capacities = nx.get_edge_attributes(G, 'capacity')
    capacities = {k: int(v) for k, v in capacities.items()}

    #aca no duele tanto, pq como q es la confi del grafikoooo
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities, font_size=8, label_pos=0.2)

    
    plt.title("Grafo de Asignaciones")
    plt.show()

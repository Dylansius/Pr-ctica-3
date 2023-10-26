import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def dijkstra(graph, start_node):
    shortest_distances = nx.single_source_dijkstra_path_length(graph, start_node, weight='weight')
    return shortest_distances

def main():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "E", 3)

    start_node = "A"
    shortest_distances = dijkstra(graph.graph, start_node)

    # Visualización del grafo
    pos = nx.spring_layout(graph.graph, seed=42)
    labels = {edge: graph.graph.get_edge_data(*edge)['weight'] for edge in graph.graph.edges()}
    nx.draw(graph.graph, pos, with_labels=True, node_size=800, node_color='skyblue')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=labels, font_color='red')
    plt.title("Grafo")

    plt.show()

    print("\nShortest distances from node", start_node, "to all other nodes:")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")

if __name__ == "__main__":
    main()

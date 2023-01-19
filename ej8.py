import networkx as nx
import itertools

def main():
    G = nx.Graph()

    planets = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'planeta1', 'planeta2', 'planeta3', 'planeta4', 'planeta5', 'planeta6', 'planeta7']
    G.add_nodes_from(planets)

    planet_pairs = list(itertools.combinations(planets, 2))
    for i, pair in enumerate(planet_pairs):
        G.add_edge(pair[0], pair[1], weight=i)

    

    T = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
    print(T.edges())



    path1 = nx.shortest_path(G, 'Tatooine', 'Dagobah', weight='weight')
    print("Shortest path from Tatooine to Dagobah:", path1)

    path2 = nx.shortest_path(G, 'Alderaan', 'Endor', weight='weight')
    print("Shortest path from Alderaan to Endor:", path2)

    path3 = nx.shortest_path(G, 'Hoth', 'Tatooine', weight='weight')
    print("Shortest path from Hoth to Tatooine:", path3)


    successors = nx.bfs_successors(G, 'Tatooine')
    print("All planets reachable from Tatooine:", list(successors))
    
main()
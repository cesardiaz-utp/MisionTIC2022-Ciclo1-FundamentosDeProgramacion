def dijkstra(unvisited: set, distances: dict, neighbours: dict, start: str) -> tuple:

    # Let distance of start vertex from start = 0. Let distance of all other vertices = infinity.
    known = { vertex: 0 if vertex == start else float('inf') for vertex in unvisited }

    # Let the previous node be unknown(none) for every vertex
    previous = {vertex: None for vertex in unvisited}

    # Repeat until there are no vertices left to visit
    while len(unvisited) > 0:

        # Visit the unvisited vertex with the smallest known distance from the start vertex
        distance, visit = min( [ (known[candidate], candidate) for candidate in unvisited] )
        # For the current vertex, calculate the distance from the visited vertex to each of its neighbours
        calculated = {neighbour: distance + distances[visit, neighbour] for neighbour in neighbours[visit]}

        # Update previous and known distances if the calculated distance is less than the known distance.
        previous.update( {vertex: visit if calculated[vertex] < known[vertex] else previous[vertex] for vertex in neighbours[visit]} )
        known.update( {vertex: calculated[vertex] if calculated[vertex] < known[vertex] else known[vertex] for vertex in neighbours[visit] })

        # Remove the current vertex (visited) from the unvisited set.
        unvisited.remove(visit)

    # Return the best known distances and their corresponing previous nodes
    return known, previous



unvisited = {'A', 'B', 'C', 'D', 'E', 'C'}

distances = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
             ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}

neighbours = {
                'A': ['B', 'D'],
                'B': ['A', 'D', 'C'],
                'C': ['B', 'E'],
                'D': ['A', 'B', 'E'],
                'E': ['D', 'B', 'C']
              }

minimas, predecesores = dijkstra(unvisited, distances, neighbours, 'A')
minimas, predecesores = sorted(minimas.items()), sorted(predecesores.items())
print('Distancias minimas: \n {} \nPredecesores: \n {}'.format(minimas, predecesores))

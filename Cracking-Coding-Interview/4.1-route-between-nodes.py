# Route Between Nodes: Given a directed graph, design an algorithm to find 
# out whether there is a route between two nodes.
# Inputs -- list: Each list within the list indicates where the index node is connected to.
E.g.,
# nodes:           0     1   2     3
# connected to = [[1,2],[3],[1,3],[]]

def route_between_nodes(graph, source, destination):
    results = []
    # Queue
    q = []
    # Enq
    q.append([source])
    while len(q) > 0:
        # Deq
        popped = q.pop(0)
        # Visit
        last_node = popped[-1]
        if last_node == destination:
            results.append(popped)
        nodes = graph[last_node]
        # Enq children
        for node in nodes:
            q.append(popped+[node])
    return results
# Test
graph = [[1,2],[3],[1,3],[]]
route_between_nodes(graph, 2, 0)

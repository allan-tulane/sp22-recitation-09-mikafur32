from collections import deque
from heapq import heappush, heappop 

num_edges_visited = 0
frontier = {}
previous_source = ""

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    #shortest_shortest_path(graph, graph[edge_name])
    global num_edges_visited
    global frontier
    global previous_source

    for i in graph[source]:
        num_edges_visited += 1
        #graph[edges].update(edges)

        edge_name = i[0]
        if edge_name in frontier and frontier[edge_name][0] > num_edges_visited:
            frontier.update({edge_name: (num_edges_visited, +i[1])})
            continue
            #if frontier[edge_name][1] < num_edges_visited:

        elif edge_name in frontier and frontier[edge_name][0] < num_edges_visited:
            continue
        frontier.update({edge_name: (num_edges_visited, +i[1])})

        print("Source is " + str((edge_name)))#str(graph[k[0]].values()))
        print(i)
        print(num_edges_visited)

        previous_source = previous_source + source
        shortest_shortest_path(graph, edge_name)
        if source != previous_source[num_edges_visited-1]:
            source = previous_source

        num_edges_visited -= 1#frontier[edge_name]
        print(num_edges_visited)


    return frontier
    #for value in graph

graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)},
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
print(shortest_shortest_path(graph, 's'))

'''
graph = {
                's': {('a', 1), ('b', 4)},
                'a': {}, # 'a': {'b'},
                'b': {('c',6)},
                'c': {('d',2)},
                'd': {('b', 3)}
            }
print(shortest_shortest_path(graph, 's'))
'''


def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """



def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'

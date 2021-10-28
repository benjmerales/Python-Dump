graph = {'A' : ['B', 'C'],
         'B' : ['C', 'D',],
         'C' : ['D'],
         'D' : ['C'],
         'E' : ['F'],
         'F' : ['C'] }

def has_key(graph, key):
    for i in graph:
        if i == key:
            return True
    return False
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not has_key(graph, start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

print(find_path(graph, 'A', 'A'))

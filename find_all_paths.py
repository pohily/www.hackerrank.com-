def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

graph = {1: [3, 2], 2: [4, 1], 3: [1, 6, 4], 4:[2, 3, 5], 5:[4], 6:[3]}
start = 5
end = 6

print(find_all_paths(graph, start, end, path=[]))

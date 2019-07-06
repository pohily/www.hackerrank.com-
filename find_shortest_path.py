def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        used = [start]
        if start == end:
            return path
        
        longest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                used.append(node)
                if newpath:
                    if not longest or len(newpath) > len(longest):
                        longest = newpath
                        
        used.append(end)
        return longest

graph = {1: [3, 2], 2: [4, 1], 3: [1, 6, 4], 4:[2, 3, 5], 5:[4, 6], 6:[5, 3]}
start = 1
end = 6

print(find_shortest_path(graph, start, end, path=[]))

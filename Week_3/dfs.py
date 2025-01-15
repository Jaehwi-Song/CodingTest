def dfs(graph, v, visited) :
    # 방문 처리 (스택의 최상단에 추가해 기준 점으로 사용)
    visited[v] = True
    print(v, end=" ")

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
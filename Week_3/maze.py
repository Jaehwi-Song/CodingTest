"""
N x M 크기의 직사각형 형태의 미로를 탈출해야 합니다
모험가의 시작 위치는 (1, 1)이며, 출구는 (N, M)이고, 한 번에 한 칸씩 이동 가능
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시
모험가가 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
(시작 칸과 마지막 칸을 모두 포함)

입력 조건 : 첫째 줄에 두 정수 N, M (4 <= N, M <= 200)
          다음 N개의 줄에는 각각 M개의 정수 (0 또는 1)로 미로의 정보가 주어짐
          (시작과 끝은 항상 1)
출력 조건 : 최소 이동 칸의 개수 출력
"""
from collections import deque

def bfs(graph, n, m) :
    x, y = 0, 0
    queue = deque([(x,y)])
    while x != n - 1 or y != m - 1:
        x, y = queue.popleft()

        if (y + 1) <= m - 1 and graph[x][y + 1] == 1:
            graph[x][y + 1] += graph[x][y]
            queue.append((x, y + 1))
        if (x + 1) <= n - 1 and graph[x + 1][y] == 1:
            graph[x + 1][y] += graph[x][y]
            queue.append((x + 1, y))
        
        print(queue)

n, m = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int, input())))

bfs(graph, n, m)
print(graph)
print(graph[n - 1][m - 1])
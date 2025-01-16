"""
N x M 크기의 얼음 틀이 있을 때,
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1,
얼음 틀 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수 구하기

입력 조건 : 첫 번째 줄에 얼음 틀의 세로 길이 N, 가로 길이 M (1 <= N, M <= 1,000)
          두 번째 줄부터 N + 1번째 줄까지 얼음틀의 형태
          (구멍 뚫린 부분은 0, 그렇지 않은 부분은 1)
출력 조건 : 한 번에 만들 수 있는 아이스크림의 개수 출력
"""

def dfs(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1

        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)

        return True
    
    return False

n, m = map(int, input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

result = 0

for i in range(n) :
    for j in range(m) :
        if dfs(i, j) :
            result += 1

print(result)
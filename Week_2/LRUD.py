"""
여행가 A는 N x N 크기의 정사각형 공간에서 이동
가장 왼쪽 위 좌표는 (1, 1)이고, 가장 오른쪽 아래 좌표는 (N, N)
여행자는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)
N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시.

입력 조건 : 첫째 줄에는 공간의 크기 N (1 <= N <= 100), 
          둘째 줄에는 여행가가 이동할 계획서 내용 (1 <= 이동 횟수 <= 100)
출력 조건 : A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백 기준으로 구분해 출력
"""

"""
# 방법 1 (나의 풀이)
dim = int(input())

behaviors = list(input().split())
current_x = 1
current_y = 1

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우 x좌푯값
dy = [0, 0, -1, 1] # 상, 하, 좌, 우 y좌푯값

for action in behaviors:
    if action == 'U' :
        idx = 0
    elif action == 'D':
        idx = 1
    elif action == 'L':
        idx = 2
    else:
        idx = 3

    tmp_pos_x = current_x + dx[idx]
    tmp_pos_y = current_y + dy[idx]

    if 1 <= tmp_pos_x <= dim and 1 <= tmp_pos_y <=dim :
        current_x = tmp_pos_x
        current_y = tmp_pos_y
    else :
        continue

print(current_x, current_y)
"""

# 방법 2
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for type in range(len(move_types)):
        if move_types[type] == plan:
            nx = x + dx[type]
            ny = y + dy[type]
    
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue

    x, y = nx, ny

print(x, y)
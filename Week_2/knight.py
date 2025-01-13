"""
왕실 정원 : 8 x 8 좌표 평면
정원의 특정한 한 칸에 나이트가 서있고, 나이트는 L자 형태로만 이동 가능
단, 정원 밖으로는 나갈 수 없음 (장기의 말 느낌)
나이트의 이동 방법 :
1. 수평 2칸 + 수직 1칸
2. 수직 2칸 + 수평 1칸

나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수 출력
행 위치는 1 ~ 8로 표현 / 열 위치는 a ~ h로 표현

입력 조건 : 나이트의 위치 좌표 (열과 행으로 구성)
출력 조건 : 나이트가 이동할 수 있는 경우의 수 출력
"""

""" 방법 1 (나의 코드)
pos = input()
pos_x = int(pos[1])

y_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9
}
pos_y = y_dict[pos[0]]

dx = [-2, 2, -1, 1] # 수직 이동 (2칸 좌,우 / 1칸 좌,우)
dy = [-1, 1, -2, 2]
count = 0

for x_idx in range(len(dx)) :
    if x_idx % 2 == 0 :
        moving = [x_idx, x_idx + 1]

    else :
        moving = [x_idx, x_idx - 1]
    
    for y_idx in moving :
        temp_pos_x = pos_x + dx[x_idx]
        temp_pos_y = pos_y + dy[y_idx]

        if 1 > temp_pos_x or temp_pos_x > 8 or 1 > temp_pos_y or temp_pos_y > 8 :
            continue

        count += 1

print(count)"""

# 방법 2
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 0

for step in steps:
    nx = row + step[1]
    ny = column + step[0]

    if 1 > nx or nx > 8 or 1 > ny or ny > 8 :
        continue

    count += 1

print(count)
# N 명의 모험가는 각각 공포도를 가짐 
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 함.
# N 명의 모험가 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값 구하기
# 이때 모든 모험가가 그룹에 포함될 필요는 없음.

# 입력 조건 : 첫 줄에 모험가의 수 N, 둘째 줄에 모험가의 공포도 값 (N 이하의 자연수)
# 출력 조건 : 여행을 떠날 수 있는 그룹 수의 최댓값 출력
N = int(input())
data = list(map(int, input().split()))
data.sort()  # 공포도 오름차순으로 sorting

result = 0
count = 0

for i in data : # 공포도를 낮은 순서로 확인
    count += 1
    if count >= i : # 모집된 멤버 수가 공포도를 충족하는 경우, 떠나자 !
        result += 1
        count = 0

print(result)


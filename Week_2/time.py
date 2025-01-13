"""
정수 N이 입력 되면, 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중
3이 하나라도 포함되는 모든 경우의 수를 구하기

입력 조건 : 첫째 줄에 정수 N 입력 (0 <= N <= 23)
출력 조건 : 3을 포함한 모든 경우의 수 출력
"""
end_time = int(input())
count = 0

for hour in range(end_time + 1) :
    for min in range(60) :
        for sec in range(60) :
            if '3' in str(hour) + str(min) + str(sec) :
                count += 1

print(count)

# 문제의 조건 1 : N에서 1을 뺍니다.
# 문제의 조건 2 : N을 K로 나눕니다. (나누어 떨어지는 경우만 적용 가능)
# N을 1로 만들기 위해 적용해야 할 최소한의 조건의 반복 횟수 찾기

## 입력 조건 : N(1 <= N <= 100,000), K (2 <= K <= 100,000)
## 출력 조건 : 조건 1, 2 수행 횟수의 최솟값

# # method 1
# N, K = map(int, input().split())
# count = 0

# while N != 1 :
#     if N % K == 0 :
#         N /= K
#     else :
#         N -= 1

#     count += 1

# print(count)

# method 2
N, K = map(int, input().split())
result = 0

while True:
    target = (N // K) * K # K로 나누어떨어질 수 있는 값
    result += (N - target) # 1로 뺴줘야 하는 값
    N = target
    if N < K :
        break
    result += 1  # 나누기 연산 횟수 고려
    N //= K  # 나누기 연산 수행

result += (N - 1) # K로 더 이상 안 나누어 떨어지는 나머지 1될 때까지 빼주기
print(result)
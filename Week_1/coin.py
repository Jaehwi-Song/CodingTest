# 동전 개수가 최소가 되는 거스름돈 구하는 문제 (Greedy Algorithm 예제)

n = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
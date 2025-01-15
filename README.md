# CodingTest

## 1주차 : 코딩테스트 개요 및 그리디 알고리즘 ##
코딩테스트 시 **Python** 기준

테스트 환경에서는 **1초에 2000만번** 연산을 수행한다고 생각
+ N이 500일 때, O(N^3)
+ N이 2000일 때, O(N^2)
+ N이 100,000일 때, O(NlogN)
+ N이 10,000,000일 때, O(N)

### Greedy Algorithm ###
현재 상황에서 당장 가장 좋은 것만 고르는 방법 (이렇게 구한 결과가 최적의 해가 되는지 정당 성 분석이 중요)

**Greedy Algorithm 예제**
1. 동전 거스름돈 문제 (거스름 돈의 동전 개수가 최소가 되도록)
2. 1이 될 때까지 (임의의 수 N을 1로 만드는 최소한의 연산 수 구하기)
3. 주어진 숫자를 최대로 만들기 (각 숫자 사이에 + 또는 x를 사용해 가장 큰 수 만들기)
4. 모험가 길드를 최대로 만들기 (공포도를 충족하며 최대가 되는 모험가 길드 수 찾기)

## 2주차 : 구현 (Implementation) && 완전 탐색(Brute Force) ##
구현 : 풀이를 떠올리는 건 쉽지만 소스코드로 옮기기는 어려운 문제 

**구현 예제**
1. 상하좌우 문제 (여행자가 상하좌우로 움직인 최종 좌표 구하기)
2. 시각 문제 (00시 00분 00초부터 N시 59분 59초까지 3을 포함하는 시각 찾기)
3. 왕국 정원 기사 문제 (체스판 위에서 나이트가 움직일 수 있는 경우의 수 계산)
4. 문자열 정렬 하기 (주어진 문자열에 대해 문자열을 오름차순으로 출력하고, 숫자의 경우 더하기)

## 3주차 : DFS & BFS ##
스택(Stack) : LIFO(선입후출)형 자료구조, python에서는 list를 사용해 append, pop으로 구현 가능

큐(Queue) : FIFO(선입선출)형 자료구조, python에서는 deque을 사용해 append, popleft로 구현 가능

재귀 함수(Recursive function) : 함수 내부에서 반복적으로 함수를 호출하는 함수

DFS(Depth First Search) : Tree 구조에서 깊이 있는 값들을 우선적으로 탐색 (보통 stack or 재귀 함수 사용)


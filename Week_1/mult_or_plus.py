# 각 자리 숫자(0 ~ 9)로 이루어진 문자열 S에 대해 
# 숫자 사이에 x 또는 + 연산자를 넣어 가장 큰 수 만들기
# 단, 모든 연산은 왼쪽에서부터 이루어진다고 가정

# 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어짐 (1 <= S의 길이 <= 20)
# 출력 조건 : 입력으로 만들 수 있는 가장 큰 수 출력

# # method 1 
# S = input()
# result = 0

# for idx in range(len(S)):
#     if idx == 0 :   
#         val1 = int(S[idx])
#         val2 = int(S[idx + 1])

#         if (val1 <=1 or val2 <= 1) :
#             result = val1 + val2
#         else :
#             result = val1 * val2
#     else :
#         val2 = int(S[idx + 1])
#         if (result <= 1 or val2 <= 1) :
#             result += val2
#         else :
#             result *= val2
    
#     if (idx + 1) == len(S) - 1 :
#         break

# print(result)

# method 2
S = input()

result = int(S[0])

for i in range(1, len(S)) :
    val = int(S[i])

    if (result <= 1 or val <= 1) : # 수가 0 또는 1 인 경우 +를, 그 외의 경우 x를 수행
        result += val
    else :
        result *= val

print(result)

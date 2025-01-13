"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어지면,
모든 알파벳을 오름차순으로 정렬해 출력 + 모든 숫자를 더한 값을 이어서 출력

입력 조건 : 첫째 줄에 하나의 문자열 S가 주어짐 (1 <= S의 길이 <= 10000)
출력 조건 : 정답 출력
"""

input_data = input()
char_list =[]
sum = 0

for char in input_data :
    """ 방법 1
    if 'A' <= char <= 'Z' :
        char_list.append(char)
    """
    # 방법 2
    if char.isalpha():
        char_list.append(char)
    else :
        sum += int(char)
if sum == 0 :
    print ("".join(sorted(char_list)))
else :
    print("".join(sorted(char_list)) + str(sum))

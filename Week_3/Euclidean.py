"""
두 개의 자연수에 대한 최대공약수 구하기

유클리드 호제법 : 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R
A와 B의 최대공약수는 B와 R의 최대 공약수와 같다 
"""
a, b = map(int, input().split())

def euclideanGCD(a, b) :
    if b == 0 :
        return a
    
    return euclideanGCD(b, a % b)

print(euclideanGCD(a, b))
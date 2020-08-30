# https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())
for i in range(1,N+1):
    if i < (N + 1) / 2:
       print(((2 * i - 1) * ".|.").center(M,"-"))
    elif i == (N + 1) / 2:
       print("WELCOME".center(M,"-"))
    elif i > (N + 1) / 2:
       print(((2 * (N - i) + 1) * ".|.").center(M,"-"))

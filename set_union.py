#https://www.hackerrank.com/challenges/py-set-union/problem

l = []

eng_number = int(input())
eng_set = list(input().split())
french_number = int(input())
french_set = list(input().split())

for i in eng_set:
        l.append(i)

for i in french_set:
        l.append(i)

s = set(l)
print(len(s))i

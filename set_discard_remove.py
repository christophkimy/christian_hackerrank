#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    separated = input().split()

    if separated[0] == 'pop':
        s.pop()

    elif separated[0] == 'remove':
        s.remove(int(separated[1]))
    
    elif separated[0] == 'discard':
        s.discard(int(separated[1]))

print(sum(s))

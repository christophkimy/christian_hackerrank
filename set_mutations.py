#https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
A = set(input().split())
n = int(input())

for i in range(n):
    cmd = (input().split())[0]
    B = set(input().split())

    if cmd == "intersection_update":
        A.intersection_update(B)
    elif cmd == "difference_update":
        A.difference_update(B)
    elif cmd == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif cmd == "update":
        A.update(B)

new_list = map(int, A)
print(sum(new_list))


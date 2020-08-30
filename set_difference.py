#https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

a_num = input()
a_set = set(input().split())
b_num = input()
b_set = set(input().split())


print(len(a_set.difference(b_set)))

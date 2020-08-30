#https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

a_count = int(input())
a_set = set(map(int, input().split()))
b_count = int(input())
b_set = set(map(int, input().split()))

new_set = a_set.symmetric_difference(b_set)
asc_set = sorted(new_set)

for i in asc_set:
    print(i)

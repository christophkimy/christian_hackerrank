#https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

names = raw_input()
full_set = set()

for i in range(int(names)):
    full_set.add(raw_input())

print len(full_set)
